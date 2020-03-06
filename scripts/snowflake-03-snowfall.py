import random

speed(0)

size = 25

def snowflake(arms, branches, size):
    pensize(size / 5)
    for arm in range(arms):
        for branch in range(branches):
            forward(size)
        
            right(45)
            forward(size)
            backward(size)
            left(45)
        
            left(45)
            forward(size)
            backward(size)
            right(45)
    
        backward(size * branches)
        
        right(360 / arms)

while True:
    color('lightblue')
    pendown()
    
    arms = random.randint(5, 9)
    branches = random.randint(2, 8)
    size = random.randint(10, 30)
    snowflake(arms, branches, size)
    penup()

    turtle.tracer(10, 0)  # ultra speed

    dot(1000, 255, 255, 255, 0.2)
    
    setposition(random.randint(-150, 150), random.randint(-150, 150))
    left(random.randint(0, 360))
