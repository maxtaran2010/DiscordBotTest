import game


def keys(inpt):
    for_key = ''
    if inpt == '⬆':
        for_key = 'w'
    if inpt == '⬇':
        for_key = 's'
    if inpt == '➡':
        for_key = 'd'
    if inpt == '⬅':
        for_key = 'a'
    key3 = [game.key('inpt')]
    return key3