import re

file = open('domains.xml', 'r')
read = file.read()
file.close()
regex = re.findall(r"[.][a-z A-Z 0-9]{2,}.*(?=\<)", read)

count = len(regex)

print(count)