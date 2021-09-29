def draw_trig(h):
    for height in range(1, h):
        print(' ' * (int(h - height)), end='')
        print("/", end='')
        print(" " * (height * 2 - 2), end='')
        print("\\")
    print("/", end='')
    print("_" * (h * 2 - 2), end='')
    print("\\")

draw_trig(4)