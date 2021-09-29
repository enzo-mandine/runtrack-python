def draw_rect():
    w = int(input('Width : '))
    h = int(input('Height : '))

    for i in range(h):
        if i == 0 or i == (h - 1):
            for j in range(w):
                if j == 0:
                    print('|', end='')
                elif j == (w - 1):
                    print('|')
                else:
                    print('-', end='')
            continue
        else:
            for j in range(w):
                if j == 0:
                    print('|', end='')
                elif j == (w - 1):
                    print('|')
                else:
                    print(' ', end='')
            continue


draw_rect()
# C'est moche mais ca marche mdr #
