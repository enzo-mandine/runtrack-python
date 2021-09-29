string = input('Renseignez une chaîne de caractères : ')

file = open('output.txt', 'w')

file.write(string)
file.close()