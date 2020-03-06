tracer(20, 0)
pensize(3)

penup()
setposition(0, -20)
pendown()

right(10)
color('pink')
for step in range(5000):
    forward(5)
    right(distance(0, 0) / 25)
