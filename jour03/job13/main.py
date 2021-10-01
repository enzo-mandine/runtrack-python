import math
import matplotlib.pyplot as plt
import re

file = open('data.txt', 'r')
read = file.read()
file.close()
firstLetter = re.findall(r"\b[a-zA-Z]", read, re.MULTILINE)
count = {}
result = {}

for i in range(ord('a'), ord('z') + 1):
    count.update({chr(i): 0})

for j in firstLetter:
    count[j.lower()] += 1

for k in count:
    count[k] = (count[k] * 100) / len(re.findall(r"\w+", read))

for i in sorted(count.items(), key=lambda kv: [kv[1], kv[0]], reverse=True):
    result.update({i[0]: i[1]})

plt.bar(result.keys(), result.values())
plt.show()
