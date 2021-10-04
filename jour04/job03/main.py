def power(base, a):
    if a == 0:
        return 1

    return base * power(base, (a - 1))


print(power(int(input('Entrez un entier: ')), int(input('Entrez un exposant: '))))
