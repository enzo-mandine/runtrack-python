import re

file = open('data.txt', 'r')
read = file.read()
file.close()
regex = re.findall(r"\w+", read)
count = len(regex)
