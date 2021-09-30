import math

import matplotlib.pyplot as plt
import re

file = open('data.txt', 'r')
read = file.read()
file.close()
read = read.lower()
wordCount = len(re.findall(r"\w+", read))
count = {}
percent = {}
for i in range(ord('a'), ord('z') + 1):
    count.update({chr(i): 0})
    percent.update({chr(i): 0})

for occurence in read:
    for letter in count.keys():
        if occurence == letter:
            count[letter] += 1
            break

for i in range(ord('a'), ord('z') + 1):
    count.update({chr(i): math.floor((100 * count[chr(i)]) / wordCount)})

result = {}
for item in sorted(count.items(), key=lambda kv: [kv[1], kv[0]], reverse=True):
    i = item[0]
    v = item[1]
    result.update({i: v})

plt.bar(result.keys(), result.values())
plt.show()
