import re
import string
import matplotlib.pyplot as plt
import numpy as np


def sort(data):
    sortedData = {}
    for i in data:
        sortedData.update({i: {}})
        # sorted(data[i].items(), key=lambda kv: [kv[1], kv[0]], reverse=True)
        # print(i, sorted(data[i].items(), key=lambda kv: [kv[1], kv[0]], reverse=True))
        for j in sorted(data[i].items(), key=lambda kv: [kv[1], kv[0]], reverse=True):
            # print(i, j[0], j[1])
            sortedData[i].update({j[0]: j[1]})
    return sortedData


file = open('data.txt', 'r')
read = file.read()
file.close()
data = re.findall(r"[a-zA-Z][a-zA-Z]", read, re.I)
result = {}
abc = list(string.ascii_lowercase)

for i in abc:
    result.update({i: {'total': 0}})
    for j in abc:
        result[i].update({j: 0})

for i in data:
    result[i[0].lower()][i[1].lower()] += 1
    result[i[0].lower()]['total'] += 1

for i in abc:
    total = result[i]['total']
    result[i].pop('total')
    for j in abc:
        if result[i].get(j) != 0:
            result[i].update({j: result[i][j] * 100 / total})

result = sort(result)
for i in abc:
    plt.title(i)
    for j in result[i]:
        plt.bar(j, result[i][j])
    plt.show()
