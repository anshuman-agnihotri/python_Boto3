import re
text = "this is the python program"
pattern = r"python"
search = re.search(pattern, text)
if search:
    print("pattern found:", search.group())
else:
    print("pattern not found")