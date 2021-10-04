import re
import time
import numpy as np

file = open('maze.mz', 'r')
read = file.read()
file.close()
lab = re.split(r"\n", read)
mapping = []
for row in lab:
    if len(row) > 0:
        mapping.append(list(row))

mapping = np.array(mapping, dtype=object)
mapping = np.where(mapping == '#', 1, mapping)
mapping = np.where(mapping == '.', 0, mapping)

start = 1, 1
end = len(mapping) - 1, len(mapping[0]) - 1

m = []
for i in range(len(mapping)):
    m.append([])
    for j in range(len(mapping[i])):
        m[-1].append(0)

i, j = start
m[i][j] = 1


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if int(m[i][j]) == k:
                if i > 0 and m[i - 1][j] == 0 and mapping[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and mapping[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and mapping[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and mapping[i][j + 1] == 0:
                    m[i][j + 1] = k + 1


k = 0
chronoStart = time.time()
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
chronoEnd = time.time()

print('This maze took only', str(chronoEnd - chronoStart), 's to resolve')

for row in m:
    print(row)
