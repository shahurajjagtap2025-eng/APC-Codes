import re

text = "Hello 123 Python 456"

# Search for digits
result = re.findall(r'\d+', text)

print(result)
