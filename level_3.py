import re

text = "".join(line.strip() for line in open("equality.txt"))

finds = re.findall(r'(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])',text)

print("".join(word[3] for word in finds))