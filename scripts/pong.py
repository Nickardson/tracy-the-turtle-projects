# Pong!
import urllib.request
import turtle
import random

paddle_width = 50
paddle_height = 10

is_left_pressed = False
is_right_pressed = False

turtle.tracer(1000, 0)  # ultra speed


def ping(url):
    r = urllib.request.urlopen('http://127.0.0.1:8080/pong/api/' + url)
    response = r.read()
    return response

# data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# data = data.encode('ascii')
# 'url', data


def login():
    print('Welcome, user ' + ping('login'))


screen = turtle.Screen()
bgcolor("black")

# Ping-pong ball
ball = screen.turtles()[0]
ball.color("white")
ball.shape("circle")
ball.penup()

screen.register_shape("paddle", ((-paddle_width / 2, 0), (paddle_width / 2, 0),
                                 (paddle_width / 2, paddle_height), (-paddle_width / 2, paddle_height)))


def create_paddle():
    paddle = turtle.Turtle()
    paddle.setheading(90)
    paddle.color("red")
    paddle.shape("paddle")
    paddle.penup()
    return paddle


login()


def left():
    global is_left_pressed
    global is_right_pressed
    is_left_pressed = True
    is_right_pressed = False


def right():
    global is_left_pressed
    global is_right_pressed
    is_left_pressed = False
    is_right_pressed = True


def stop():
    global is_left_pressed
    global is_right_pressed
    is_left_pressed = False
    is_right_pressed = False


screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(stop, "Up")
screen.onkey(stop, "Down")
screen.listen()


def get_movement_direction():
    direction = 0
    if is_left_pressed:
        direction = direction - 1
    if is_right_pressed:
        direction = direction + 1
    return direction


screen.update()


def game_loop():
    velocity = get_movement_direction() * 5
    p1_pos = p1.position()
    p1.setposition(p1_pos[0] + velocity, p1_pos[1])

    # l00p
    screen.update()
    screen.ontimer(game_loop, 1 / 30)


# Ready Player One
p1 = create_paddle()
# Ready Player Two
p2 = create_paddle()

game_loop()
