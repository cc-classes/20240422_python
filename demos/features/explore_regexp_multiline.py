"""regex demo"""

import re


content = """apple
banana
apple
Banana
banana
apple
avocado
"""

# r = re.compile(r"^apple", re.MULTILINE)
# r = re.compile(r"[a-z]*a$", re.MULTILINE)
r = re.compile(r"[a-z]*a$", re.MULTILINE | re.IGNORECASE)

print(list(r.finditer(content)))
