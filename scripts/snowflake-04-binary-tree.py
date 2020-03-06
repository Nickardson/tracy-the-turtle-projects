turtle.tracer(20, 0)  # ultra speed
speed(0)

def create_branch(more):
    branch_size = 5 + 5 * more
    angle = 5 * more
    distance = 0

    forward(distance)

    right(angle)
    forward(branch_size)
    if more > 1:
        create_branch(more - 1)
    backward(branch_size)
    left(angle)

    left(angle)
    forward(branch_size)
    if more > 1:
        create_branch(more - 1)
    backward(branch_size)
    right(angle)

    backward(distance)
    

pensize(5)

color('red')
create_branch(6)
right(360 / 3)

color('green')
create_branch(6)
right(360 / 3)

color('blue')
create_branch(6)
right(360 / 3)
