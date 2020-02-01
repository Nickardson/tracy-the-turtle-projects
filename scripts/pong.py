# Pong!
import urllib.request
import turtle
import random

paddle_width = 50
paddle_height = 10
paddle_separation = 150

player_id = 'home'
player_is_home = True
network_tick = 10
network_tick_interval = 10

p2_current_x = 0
p2_last_x = 0

ball_current_x = 0
ball_current_y = 0
ball_last_x = 0
ball_last_y = 0
ball_velocity_x = 0
ball_velocity_y = 0

is_left_pressed = False
is_right_pressed = False

home_score = 32
away_score = 9876

turtle.tracer(1000, 0)  # ultra speed


SCALE = 1  # arbitrarily scale digits larger or smaller

CURSOR_SIZE = 25  # maximum dimension of our custom turtle cursor

# space from start of one digit to the next
SPACING = CURSOR_SIZE * 1.25 * SCALE

DIGITS = {  # which segments to turn on encoded as bits
    '0': 0b1111110,
    '1': 0b0110000,
    '2': 0b1101101,
    '3': 0b1111001,
    '4': 0b0110011,
    '5': 0b1011011,
    '6': 0b1011111,
    '7': 0b1110000,
    '8': 0b1111111,
    '9': 0b1111011,
    'A': 0b1110111,
    'B': 0b0011111,
    'C': 0b1001110,
    'D': 0b0111101,
    'E': 0b1001111,
    'F': 0b1000111,
}


def display_number(turtle, number):
    for digit in str(number):
        bits = DIGITS[digit]

        for bit in range(7):
            if 2 ** bit & bits:
                position = turtle.position()
                segments[bit](turtle)
                turtle.stamp()
                turtle.setheading(0)
                turtle.setposition(position)

        turtle.forward(SPACING)


def segment_A(turtle):  # top
    turtle.setheading(90)
    turtle.sety(turtle.ycor() + 20 * SCALE)


def segment_B(turtle):  # right upper
    turtle.setposition(turtle.xcor() + 10 * SCALE, turtle.ycor() + 10 * SCALE)


def segment_C(turtle):  # right lower
    turtle.setposition(turtle.xcor() + 10 * SCALE, turtle.ycor() - 10 * SCALE)


def segment_D(turtle):  # bottom
    turtle.setheading(90)
    turtle.sety(turtle.ycor() - 20 * SCALE)


def segment_E(turtle):  # left lower
    turtle.setposition(turtle.xcor() - 10 * SCALE, turtle.ycor() - 10 * SCALE)


def segment_F(turtle):  # left upper
    turtle.setposition(turtle.xcor() - 10 * SCALE, turtle.ycor() + 10 * SCALE)


def segment_G(turtle):  # center
    turtle.setheading(90)


segments = [segment_G, segment_F, segment_E,
            segment_D, segment_C, segment_B, segment_A]


def ping(url):
    r = urllib.request.urlopen('http://127.0.0.1:8080/pong/api/' + url)
    response = r.read()
    return response


def pong(url, data):
    return ping(url + '?data=' + str(data))


def login():
    global player_id
    global player_is_home
    player_id = ping('login')
    player_is_home = player_id == 'home'
    print('Welcome, ' + player_id + ' team!')


screen = turtle.Screen()
bgcolor("black")

# Ping-pong ball
ball = screen.turtles()[0]
ball.color("white")
ball.shape("circle")
ball.penup()

screen.register_shape("paddle", ((-paddle_width / 2, 0), (paddle_width / 2, 0),
                                 (paddle_width / 2, paddle_height), (-paddle_width / 2, paddle_height)))


screen.register_shape("paddle", ((-paddle_width / 2, 0), (paddle_width / 2, 0),
                                 (paddle_width / 2, paddle_height), (-paddle_width / 2, paddle_height)))


screen.register_shape('segment', ((-10.5, 0), (-8, 2.5),
                                  (8, 2.5), (10.5, 0), (8, -2.5), (-8, -2.5)))  # <=>


def create_paddle():
    paddle = turtle.Turtle()
    paddle.setheading(90)
    paddle.shape("paddle")
    paddle.penup()
    return paddle


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


def interpolate(x, y, a):
    return y * a + x * (1 - a)


screen.update()


def network():
    # Send where we're at, and get back the other player's posiion
    global p2_current_x
    global p2_last_x
    global ball_current_x
    global ball_current_y
    global ball_last_x
    global ball_last_y
    global ball_velocity_x
    global ball_velocity_y

    p2_last_x = p2_current_x
    ball_last_x = ball_current_x
    ball_last_y = ball_current_y

    # Returns EnemyX,BallX,BallY,BallVelocityX,BallVelocityY
    move_result = pong('move', {'player': player_id, 'x': p1.xcor()})
    move_results = move_result.split(',')

    p2_current_x = int(move_results[0])
    ball_current_x = int(move_results[1])
    ball_current_y = int(move_results[2])
    ball_velocity_x = int(move_results[3])
    ball_velocity_y = int(move_results[4])


def draw_score():
    digits.clear()
    digits.setposition(-175, -170)
    display_number(digits, str(home_score if player_is_home else away_score))
    
    digits.setposition(-175, 170)
    display_number(digits, str(away_score if player_is_home else home_score))
    digits.hideturtle()


def game_loop():
    global network_tick

    network_interpolation = (network_tick_interval -
                             network_tick) / float(network_tick_interval)

    velocity = get_movement_direction() * 5
    p1_pos = p1.xcor() + velocity
    p1_pos = max(-200 + paddle_width / 2, min(200 - paddle_width / 2, p1_pos))
    p1.setposition(p1_pos, p1.ycor())

    p2_pos = interpolate(p2_last_x, p2_current_x, network_interpolation)
    p2.setposition(p2_pos, p2.ycor())

    ball_pos_x = interpolate(
        ball_last_x, ball_current_x, network_interpolation)
    ball_pos_y = interpolate(
        ball_last_y, ball_current_y, network_interpolation)
    ball.setposition(ball_pos_x, ball_pos_y)

    draw_score()

    # l00p
    screen.update()
    screen.ontimer(game_loop, 1 / 30)

    network_tick = network_tick - 1
    if network_tick <= 0:
        network_tick = network_tick_interval
        network()


login()

# Ready Player One
p1 = create_paddle()
p1.setposition(0, -paddle_separation)
p1.color("lightblue" if player_is_home else "red")
# Ready Player Two
p2 = create_paddle()
p2.setposition(0, paddle_separation)
p2.right(180)
p2.color("red" if player_is_home else "lightblue")


digits = turtle.Turtle('segment', False)
digits.speed('fastest')
digits.color('white')
digits.shape('segment')
digits.penup()

game_loop()
