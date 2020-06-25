"""Read the Basic Application Level Confidentiality Profile and Options from
table E.1-1 here:
http://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html

and convert them to idiscore python code that generates the basic profile
and all profile options
"""
from pathlib import Path
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from pydicom.tag import Tag

from idiscore.core import Rule, RuleSet
from idiscore.operations import (
    Clean,
    Empty,
    GenerateUID,
    Keep,
    Operator,
    Remove,
    Replace,
)


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


class ActionCodes:
    """The codes in table E1-1 denoting what to do with a tag

    Links to a matching idicore operation
    """

    # I want to assign only one instance to each code
    replace = Replace()
    empty = Empty()
    remove = Remove()
    keep = Keep()
    clean = Clean()
    uid = GenerateUID()

    ALL = {
        "D": replace,  # replace with dummy
        "Z": empty,  # replace with zero length
        "X": remove,  # remove
        "K": keep,  # keep
        "C": clean,  # clean
        "U": uid,  # replace with consistent UID
        "Z/D": empty,  # Z unless D is required for consistency
        "X/Z": remove,  # X unless Z is required for consistency
        "X/D": remove,  # X unless D is required for consistency
        "X/Z/D": remove,  # X unless Z or D is required for consistency
        "X/Z/U*": remove,  # X unless Z or U is required for consistency
    }

    @classmethod
    def get_operation(cls, code: str) -> Operator:
        if code in cls.ALL:
            return cls.ALL[code]
        else:
            raise ValueError(f"Unknown actioncode '{code}'")


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
    with open(path, "r") as f:
        text = f.read()
    return text


def get_html_cached() -> str:
    """Get html for the table from cache, or refresh cache if it does not exist"""
    cache_path = Path("/tmp/dicomtable.html")
    if not cache_path.exists():
        save_html_online(cache_path)
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


table = parse_nema_dicom_table(get_html_cached())

# create basic confidentiality profile as RuleSet
rules = []
for row in table.rows:
    column_name = "Basic Prof."
    # for this row, create a rule

    action_code = row[column_name]
    if action_code == "":
        continue  # no action code, so no rule is defined for this row
    else:
        try:
            tag = Tag(row["Tag"].replace(",", "")[1:-1])  # (0010,0010) -> 00100010
        except ValueError as e:
            print(f"Error processing {row['Tag']}. Skipping this. Error was:{e}")
            continue

        operation = ActionCodes.get_operation(action_code)
        rules.append(Rule(tag, operation))

# Map table contents to functions
basic_profile = RuleSet(name="Basic Profile", rules=rules)

# TODO: Basic profile does NOT explicitly Keep() any tag. This is a problem as
# idiscore assumes any tag without a rule is removed. This would remove all
# tags currently. Either make basic profile 'special' in some way or solve
# differently.


# create each confidentiality profile option as RuleSet


test = 1
