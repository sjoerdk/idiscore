"""Jinja templates. Putting these in a separate module because indentation is
difficult when inlining templates inside classes and functions
"""


idiscore_description = """IDISCore instance description

idiscore lib version: {{ idiscore_lib_version }}

Bouncers:
{% for x in bouncer_descriptions %}* {{ x }}
{% endfor %}
{{ profile_description }}
"""

profile_description = """Profile '{{ profile_name }}'
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
