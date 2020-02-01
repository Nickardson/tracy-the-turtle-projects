import turtle
import random
turtle.tracer(1000, 0) # ultra speed

screen = turtle.Screen()

# we want a snake!
snake = screen.turtles()[0]
snake.color("green")
snake.penup()

# and a fruit
fruit = turtle.Turtle()
fruit.color("red")
fruit.shape("circle")
fruit.penup()

segments = 1 # how many segments is our snake, and how fast?
trail = [] # where have we been?

def game_loop():
  global segments

  snake.forward(20) # move forward

  # if we hit ourselves, game over!
  if (any(snake.distance(p[0]) < 1 for p in trail)):
    segments = 1
    snake.setposition(0, 0)
    bgcolor((random.random() * 128 + 127, random.random() * 128 + 127, random.random() * 128 + 127))

  # remember the trail
  trail.append((snake.pos(), snake.heading()))
  while (len(trail) > segments):
    trail.pop(0)

  # draw the snake
  snake.clear()
  for location in trail:
    snake.setposition(location[0])
    snake.setheading(location[1])
    snake.stamp()
  
  # eat the fruit if we hit it
  if (snake.distance(fruit.pos()) < 20):
    fruit.setposition(random.randint(-9, 9) * 20, random.randint(-9, 9) * 20)
    segments += 2

  turtle.update()
  screen.ontimer(game_loop, 1000 / (segments / 10 + 5))

# controls
def up():
  snake.setheading(90)
def right():
  snake.setheading(0)
def down():
  snake.setheading(270)
def left():
  snake.setheading(180)

screen.onkey(up, "Up")
screen.onkey(right, "Right")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.listen()

game_loop()
