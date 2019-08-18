t= "\n      “If you tell the truth, you don't have to remember anything.”\n  "

import re

s=re.search(r'\w.*?\.',t)
print(s.group())

print(t.rstrip())