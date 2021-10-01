def power(base, a):
    if a != 0:
        return base * power(base, (a - 1))
    else:
        return 1


print(power(int(input('Entrez un entier: ')), int(input('Entrez un exposant: '))))
