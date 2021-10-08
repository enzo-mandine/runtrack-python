import re
import time
import numpy as np


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


def route(maze, goal):
    i, j = goal
    k = maze[i][j]
    the_path = [(i, j)]
    while k > 1:
        if i >= 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            the_path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            the_path.append((i, j))
            k -= 1
        elif i <= len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            the_path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            the_path.append((i, j))
            k -= 1
    return the_path


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
start = 0, 0
end = len(mapping) - 1, len(mapping[0]) - 1

m = []
for i in range(0, len(mapping)):
    m.append([])
    for j in range(0, len(mapping[i])):
        m[i].append(0)

i, j = start
m[i][j] = 1

k = 0
chronoStart = time.time()
while m[end[0]][end[1]] == 0:
    k += 1
    make_step(k)
route = route(m, end)
chronoEnd = time.time()
print("start: ", start, "end: ", end)
print('This maze took only', str(chronoEnd - chronoStart)[0:5], 's to resolve')
print(route[::-1])
