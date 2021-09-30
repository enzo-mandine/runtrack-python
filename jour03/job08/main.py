import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors, pyplot
from matplotlib.ticker import PercentFormatter

file = open('data.txt', 'r')
read = file.read()
file.close()
read = read.lower()
count = {}
words = read.split()
wordsAmount = len(words)
result = {}
resultData = []
valuesData = []

for word in words:
    index = len(word)
    count.update({int(index): 0})

for word in words:
    index = len(word)
    count[index] += 1

j = len(count.keys()) + 1
total = 0
for i in range(1, j):
    valuesData.append(count[i])
    percent = ((count[i] * 100) / wordsAmount)
    result.update({i: percent})
    resultData.append(percent)
    total += percent

# plt.hist(result.values(), bins=len(result.keys()), range=(.1, 19))
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = result.keys()
sizes = result.values()
# only "explode" the 2nd slice (i.e. 'Hogs')
explode = (.1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1, .1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=range(0, 19), rotatelabels=True, autopct='%1.1f%%', shadow=False, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal')

plt.show()
