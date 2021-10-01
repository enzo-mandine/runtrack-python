def factoriel(nbr):
    if nbr == 0:
        return 1
    else:
        return nbr * factoriel(nbr - 1)


result = int(input("Renseignez un nombre entier: "))
print(factoriel(result))
