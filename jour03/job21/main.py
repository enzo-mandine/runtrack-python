import matplotlib.pyplot as plt
import re

file = open('data.txt', 'r')
read = file.read()
file.close()
data = re.findall(r"[a-zA-Z][a-zA-Z]", read, re.I)
result = {}
i = ord('a')
while i <= ord('z'):
    j = ord('a')
    result.update({chr(i): {}})
    while j <= ord('z'):
        result[chr(i)].update({chr(j): 0})
        j += 1
    i += 1

for i in data:
    result[i[0].lower()][i[1].lower()] += 1

print(result)
