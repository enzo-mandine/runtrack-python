def skywalker(array):
    sort = []

    for note in array:
        if note >= 40:
            part = note % 5
            if part >= 3:
                note = note + (5 - part)
        sort.append(note)

    return print(sort)


students = [10, 4, 8, 47, 87, 82, 83, 78]

skywalker(students)
