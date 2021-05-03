"""Jinja templates. Putting these in a separate module because indentation is
difficult when inlining templates inside classes and functions
"""
import os

from jinja2.environment import Environment

idiscore_description_txt = """IDISCore instance description

idiscore lib version: {{ idiscore_lib_version }}

Bouncers:
{% for x in bouncer_descriptions %}* {{ x }}
{% endfor %}
{{ profile_description }}
"""

profile_description_txt = """Profile '{{ profile_name }}'
Rule sets:
{% for x in rule_set_names %}{{ x }}
{% endfor %}

All rules, Alphabetically:
{% for x in rule_strings_by_name %}{{ x }}
{% endfor %}

All rules, by tag:
{% for x in rule_strings_by_tag %}{{ x }}
{% endfor %}
"""

idiscore_description_rst = """{{ 'IDISCore instance description'|make_h1 }}

idiscore lib version: {{ idiscore_lib_version }}


{{ 'Bouncers:'|make_h2 }}

{% for x in bouncer_descriptions %}* {{ x }}
{% endfor %}

{{ profile_description }}
"""

profile_description_rst = """{% filter make_h2 %}Profile '{{ profile_name }}'
{% endfilter %}

{{ 'Rule sets:'|make_h3 }}

{% for x in rule_set_names %}{{ x }}
{% endfor %}

{{ 'All rules, alphabetically:'|make_h3 }}

{% for x in rule_strings_by_name %}* {{ x }}
{% endfor %}

{{ 'All rules, by tag:'|make_h3  }}

{% for x in rule_strings_by_tag %}* {{ x }}
{% endfor %}
"""


def make_h1(text):
    bar = "=" * len(text)
    return os.linesep.join([bar, text, bar])


def make_h2(text):
    bar = "=" * len(text)
    return os.linesep.join([text, bar])


def make_h3(text):
    bar = "-" * len(text)
    return os.linesep.join([text, bar])


jinja_env = Environment()
jinja_env.filters["make_h1"] = make_h1
jinja_env.filters["make_h2"] = make_h2
jinja_env.filters["make_h3"] = make_h3
