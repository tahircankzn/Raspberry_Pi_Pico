x = 2
y = -1*(x**2)+320
print(320+x,480-y)



for x in range(-320,321,1):
    y = -1*(x**2)+320
    if 480-y <= 480:
        print(x,320+x,480-y)

    """if 480-y > 0:
        print(i,320+i,480-y)
        break"""