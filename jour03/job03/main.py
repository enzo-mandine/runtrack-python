import re

nbr = int(input('Choississez un nombre entier : '))
if nbr == 0:
    print('Oops, vous avez choissis ' + str(nbr) + ' !')
else:
    print('Vous avez choissis le nombre : ', nbr)
    file = open('data.txt', 'r')
    read = file.read()
    file.close()
    regex = re.findall(r"\b\w{" + str(nbr) + "}\\b", read)
    result = len(regex)
    print('data.txt contien', result, 'fois un mot de', nbr, 'lettres')
