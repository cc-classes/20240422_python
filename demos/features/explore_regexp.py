"""regex demo"""

# reasons for using a regular expression
# detect if there is a match
# extract data (find some kind of info or split data into parts)
# replace or substitute data in the original text

# common data sources for a regex
# 1. text file on the file system
# 2. output of running other programs (subprocesses)

import re

# content = "as busy as a bee b d"

# r = re.compile(r"b[a-z]?")

# match the regular expression from the start of the content
# print(r.match(content))

# searches the string for the first match
# print(r.search(content))

# returns a list of the matches
# print(r.findall(content))

# returns all matches as match objects
# print(list(r.finditer(content)))

content = "red|green;blue:yellow"

r = re.compile(r"\||;|:")
print(r.split(content))
print(r.sub(",", content))

# content = "red|green;blue:yellow"
r = re.compile(r"[|;:]")
print(r.split(content))
print(r.sub(",", content))
