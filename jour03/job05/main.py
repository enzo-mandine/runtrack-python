import matplotlib.pyplot as plt

file = open('data.txt', 'r')
read = file.read()
file.close()
read = read.lower()
count = {}
for i in range(ord('a'), ord('z') + 1):
    count.update({chr(i): 0})

for occurence in read:
    for letter in count.keys():
        if occurence == letter:
            count[letter] = count[letter] + 1

print(count)

plt.bar(count.keys(), count.values())
plt.show()
