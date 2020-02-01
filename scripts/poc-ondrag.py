import turtle

screen = turtle.Screen()
ball = screen.turtles()[0]

def ondrag_handler(x, y):
    print('Whoa ' + str(x) + ', ' + str(y))

#screen.bgcolor('black')

ball.ondrag(ondrag_handler)

screen.listen()
screen.mainloop()  # screen.mainloop() preferred but not in Python 2
