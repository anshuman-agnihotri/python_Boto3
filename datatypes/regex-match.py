import re
text = "python easy to use"
pattern = r"python"
match = re.match(pattern, text)
if match:
    print("match found:", match)
else:
    print("match not found")