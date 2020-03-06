tracer(40, 0)
pensize(3)

penup()
setposition(0, -20)
pendown()

right(30) # different turns mix up the angles a lot

color('skyblue')
for step in range(2000):
    forward(5)
    right(distance(0, 0) / 14)

color('aquamarine')
for step in range(2000):
    forward(20)
    right(distance(0, 0) / 36)
    
color('teal')
for step in range(2000):
    forward(20)
    right(10 - distance(0, 0) / 15)
