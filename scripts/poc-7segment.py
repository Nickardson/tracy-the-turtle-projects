from turtle import Screen, Turtle

screen = Screen()
screen.setup(950, 200)
screen.register_shape('segment', ((-14.5, 0), (-12, 2.5), (12, 2.5), (14.5, 0), (12, -2.5), (-12, -2.5)))  # <=>

SCALE = 1.75  # arbitrarily scale digits larger or smaller

CURSOR_SIZE = 25  # maximum dimension of our custom turtle cursor

SPACING = CURSOR_SIZE * 1.25 * SCALE  # space from start of one digit to the next

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

segments = [segment_G, segment_F, segment_E, segment_D, segment_C, segment_B, segment_A]

digits = Turtle('segment', False)
digits.speed('fastest')
digits.shape('segment')
digits.penup()

digits.setx(SPACING - screen.window_width() / 2)

display_number(digits, "0123456789ABCDEF")
