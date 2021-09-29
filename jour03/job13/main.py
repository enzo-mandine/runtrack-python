import matplotlib.pyplot as plt

file = open('data.txt', 'r')
read = file.read()
file.close()
read = read.lower()
count = {}
percent = {}
for i in range(ord('a'), ord('z') + 1):
    count.update({chr(i): 0})
    percent.update({chr(i): 0})

for occurence in read:
    for letter in count.keys():
        if occurence == letter:
            count[letter] = count[letter] + 1


result = []

for i in count:
    print(i)
# plt.bar(count.keys(), count.values()) x = count.values() plt.hist(x, bins=None, range=None, density=False,
# weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None,
# log=False, color=None, label=None, stacked=False)
# plt.show()
