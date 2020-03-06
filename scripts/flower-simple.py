speed(0)
pensize(5)

# Stem
color('green')
right(90)
forward(200)
backward(200)

# Petals
petals = 8
color('red')
for petal in range(petals):
    begin_fill()
    circle(25)
    end_fill()
    
    backward(50)
    left(360 / petals)
