import re
text = "banana, orange, apple, sweets, biscuits"
pattern = r","
split_results = re.split(pattern, text)
print("split results:", split_results)