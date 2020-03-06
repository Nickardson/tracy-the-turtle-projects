arms = 6

pensize(4)
color('lightblue')

for arm in range(arms):
    forward(100)
    
    right(45)
    forward(25)
    backward(25)
    left(45)

    left(45)
    forward(25)
    backward(25)
    right(45)

    backward(100)
    
    right(360 / arms)
