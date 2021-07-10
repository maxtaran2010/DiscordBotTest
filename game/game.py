def key(inpt):
    y = 0
    x = 0
    cords = []
    if inpt == 'w':
        y = y+1
    if inpt == 's':
        y = y-1
    if inpt == 'd':
        x = x+1
    if inpt == 'a':
        x = x-1
    cords.append(x)
    cords.append(y)
    return cords
