import string


def allowedLetters():
    allowed = []
    for letter in string.ascii_lowercase:
        allowed.append(letter)

    return allowed


def returnError(word, allowed):
    if len(word.split(' ')) > 1:
        return print('veuillez renseigner un mot unique')

    for letter in word:
        if not letter.islower():
            return print('veuillez renseigner un mot en minuscule')
        try:
            allowed.index(letter)
        except ValueError:
            return print('veuillez renseigner un mot sans caractères spéciaux')


def nextWord(word):
    allowed = allowedLetters()
    returnError(word, allowed)

    i = len(word) - 1
    word = list(word)
    while i >= 0:
        curr = word[i]
        prev = word[i - 1]
        if curr > prev:
            word[i] = prev
            word[i - 1] = curr
            if len(word) - i > 3:
                x = (len(word)) - i + 1
                y = (len(word)) + 1
                result = word[0:x]
                toSort = word[x:y]
                toSort.sort()

                return print(''.join(result) + ''.join(toSort))

            return print(''.join(word))

        i = i - 1

    return print(word)


nextWord(input('choose a word: '))
