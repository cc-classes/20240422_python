"""regex capture groups demo"""

import re

content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# r = re.compile(r"<span>(.*)</span>")
# r = re.compile(r"<b>(.*?)</b>")
r = re.compile(r"<b>(?P<data>.*?)</b>")

# r = re.compile(r"<span>(.*)</span>")
# r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"^(?P<op_name>[a-z]*) (?P<op_value>[0-9\.]*)")

for match in r.finditer(content):
    # print(match.groups())
    print(match.groupdict())
