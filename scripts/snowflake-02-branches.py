speed(0)

arms = 8
branches = 4

pensize(5)
color('lightblue')

for arm in range(arms):
    for branch in range(branches):
        forward(25)
    
        right(45)
        forward(25)
        backward(25)
        left(45)
    
        left(45)
        forward(25)
        backward(25)
        right(45)

    backward(25 * branches)
    
    right(360 / arms)
