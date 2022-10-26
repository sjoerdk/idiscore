"""Read the Basic Application Level Confidentiality Profile and Options from
table E.1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html

and convert them to python that can be saved in public_dicom.py
"""
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from jinja2 import Template
from pydicom.tag import Tag


from idiscore.dicom import ActionCode, ActionCodes
from idiscore.identifiers import (
    PrivateTags,
    RepeatingGroup,
    RepeatingTag,
    SingleTag,
    TagIdentifier,
)
from idiscore.nema_parsing import E1_1_METHOD_INFO, RawNemaRuleSet


class Table:
    """A simple table that expects headers and rows to be in the same
    order

    There seems to be no really lightweight implementation for this?
    """

    def __init__(self, headers: List[str], rows: List[Dict] = None):
        """Headers and each row should have the same length"""
        if not rows:
            rows = []
        self.headers = headers
        self.rows = rows

    def add_row(self, row: List):
        """Add row, assume row is the same order as headers"""
        row_dict = {}
        for header, value in zip(self.headers, row):
            row_dict[header] = value
        self.rows.append(row_dict)


class ConfidentialityProfileTable(Table):
    """The table E1-1
    http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html'
    containing all the confidentiality profile options
    """

    expected_header_names = [
        "Attribute Name",
        "Tag",
        "Retd. (from PS3.6)",
        "In Std. Comp. IOD (from PS3.3)",
        "Basic Prof.",
        "Rtn. Safe Priv. Opt.",
        "Rtn. UIDs Opt.",
        "Rtn. Dev. Id. Opt.",
        "Rtn. Inst. Id. Opt.",
        "Rtn. Pat. Chars. Opt.",
        "Rtn. Long. Full Dates Opt.",
        "Rtn. Long. Modif. Dates Opt.",
        "Clean Desc. Opt.",
        "Clean Struct. Cont. Opt.",
        "Clean Graph. Opt.",
    ]

    def __init__(self, headers: List[str], rows: List[Dict] = None):
        if not headers == self.expected_header_names:
            raise ValueError(
                f"Header names for this table seem to be different then"
                f"expected. Expected {self.expected_header_names}, but "
                f"got {headers}. I'm not sure this table contains"
                f"the right info"
            )

        super().__init__(headers=headers, rows=rows)


def get_html_online() -> str:
    url = (
        "http://dicom.nema.org/medical/dicom/current/"
        "output/chtml/part15/chapter_E.html"
    )
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(
            f"Got response code {resp.status_code} when trying to load {url}"
        )
    return resp.text


def save_html_online(path: str):
    with open(path, "w") as f:
        f.write(get_html_online())
    print(f"saved to {path}")


def load_html(path) -> str:
    print(f"loading from {path}")
    with open(path) as f:
        text = f.read()
    return text


def get_html_cached(force_refresh: bool = False) -> str:
    """Get html for the table from cache, or refresh cache if it does not exist"""
    cache_path = Path("/tmp/dicomtable.html")
    if not cache_path.exists() or force_refresh:
        save_html_online(str(cache_path))
    return load_html(cache_path)


def parse_nema_dicom_table(html: str) -> Table:
    """Parse the table in
    'http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html'
    as it was around june 2020 into a clean table
    """

    # parse the html to get to the main table
    soup = BeautifulSoup(html, "html.parser")
    main_table_element = soup.select("div.table-contents table")[0]
    header_elements = main_table_element.findAll("th")
    header_names = [x.text.replace("\n", "") for x in header_elements]
    rows = main_table_element.findAll("tr")

    # create a kind of clean table out of the contents of the nema table
    main_table = ConfidentialityProfileTable(headers=header_names)
    for row in rows[1:]:  # first row is empty. Exclude
        column_elements = row.findAll("td")
        column_values = [x.text.replace("\n", "") for x in column_elements]
        main_table.add_row(column_values)

    return main_table


class RowParseError(Exception):
    pass


def parse_tag_string(tag_string) -> Optional[TagIdentifier]:
    """Parse a string containing a tag identifier to proper object
    Can handle:
    * (0010,100e) regular tags
    * (60xx,00xx) repeater tags
    * (ffff,dddd) unique outlyer denoting 'private tags'

    Raises
    ------
    RowParseException
        When tag string cannot be parsed
    """
    try:
        return SingleTag(
            Tag(tag_string.replace(",", "")[1:-1])
        )  # format as Tag() input
    except ValueError:
        # this might be a repeater tag with x's in it. Try that next
        pass
    try:
        return RepeatingGroup(RepeatingTag(tag_string))
    except ValueError:
        # This was not a repeater tag. Still some options left. Continue.
        pass
    if tag_string == "(gggg,eeee) where gggg is odd":
        # unique 'private tags' tag. there is special handling for this in idiscore
        # so no rule is needed for this
        return PrivateTags()
    else:
        raise RowParseError(
            f"Could not parse '{tag_string}' as regular tag or repeater tag"
        )


def parse_row(
    column_name: str, row: Dict[str, str]
) -> Optional[Tuple[TagIdentifier, ActionCode]]:
    """Parse row from DICOM table into a Rule

    Most rules are regular
    DICOM tag -> action rules
    but there are a few exceptions like repeater tags
    (50xx,xxxx) -> action

    Parameters
    ----------
    column_name: str
        Name of the column to read for action code
    row: Dict
        Dict of column_name: column_value representing one row in DICOM table

    Returns
    -------
    Tuple[TagIdentifier, ActionCode]]
        If row could be parsed as a rule
    None
        If row can be safely assumed to contain no rule

    Raises
    ------
    RowParseException
        When row cannot be parsed
    """
    # get values
    key = row[column_name]
    if key == "":
        return None  # no action code key, so no rule is defined for this row

    action_code = ActionCodes.get_code(key)

    identifier = parse_tag_string(row["Tag"])
    if not identifier:
        # this can be skipped
        return None
    else:
        return identifier, action_code


def extract_actions(
    table: Table, column_name: str
) -> List[Tuple[TagIdentifier, ActionCode]]:
    """Go through all DICOM tags listed in table, check the action designated
    in given column (K for keep, X for delete, etc)
    """
    actions = []
    for row in table.rows:
        tuple = parse_row(column_name=column_name, row=row)
        if tuple:  # could be None if this row can be skipped
            actions.append(tuple)
    return actions


# parse actual DICOM webpage content into clean table
table = parse_nema_dicom_table(get_html_cached(force_refresh=False))

# Now print python code that will recreate each profile
heading = """
\"\"\"Public DICOM information auto-generated from generate_public_dicom.py

Information from table E.1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html
\"\"\"

from idiscore.nema import ActionCodes, RawNemaRuleSet
from idiscore.identifiers import SingleTag, RepeatingGroup, PrivateTags
"""

profile_template_text = """
{{profile_name}} = \\
    RawNemaRuleSet(
        name="{{ profile_verbose_name }}",
        code="{{ profile_code }}",
        rules=[{% for rule in rules %}
               ({{rule.0}}, {{rule.1}}){% if not loop.last %},{% endif%}  # {{rule.2}}{% endfor %}
               ]
    )

"""
profile_template = Template(profile_template_text)

content = heading

for profile in E1_1_METHOD_INFO:
    if profile.table_header is None:
        continue  # Options like 'clean Pixel data' are not in table. skip.
    raw_list = RawNemaRuleSet(
        name=profile.full_name,
        code=profile.code,
        rules=extract_actions(table=table, column_name=profile.table_header),
    )

    content += profile_template.render(
        profile_name=profile.short_name,
        profile_verbose_name=profile.full_name,
        profile_code=profile.code,
        rules=[
            (x.as_python(), f"ActionCodes.{y.var_name}", x.name())
            for x, y in raw_list.rules
        ],
    )

print(content)
