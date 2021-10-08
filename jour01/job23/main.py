def draw_rect():
    w = int(input('Width : '))
    h = int(input('Height : '))

    hor = '--' * (w - 1) + '\n'
    emptyRow = '|' + '  ' * (w - 2) + '|' + '\n'
    print(hor + (h - 2) * emptyRow + hor)
    return True


draw_rect()
