text = "".join(line.strip() for line in open("ocr.txt"))

occ = {}
for char in text:
    occ[char] = occ.get(char,0)+1

ave = sum(occ.values())//len(occ)

print("".join(char for char in text if occ[char] < ave))