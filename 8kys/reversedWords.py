def reverse_words(s):
    word = s.split()
    space = ' '
    reverse = word[::-1]
    normal = space.join(reverse)
    return normal
