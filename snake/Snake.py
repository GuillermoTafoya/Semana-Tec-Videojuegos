"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
framerate = 0

writer = Turtle()
def info_alumnos():
    writer.up()
    writer.goto(-60,190)
    writer.color('red')
    writer.write('Guillermo Tafoya Milo A01633790', align='left', font=('Arial', 10, 'normal'))
    writer.goto(-60,170)
    writer.color('blue')
    writer.write('Rogelio Zaid Sariñana Hernández A01620778', align='left', font=('Arial', 10, 'normal'))
    writer.goto(-60,250)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

from random import choice
directions = [vector(0, 10), vector(10, 0), vector(0, -10), vector(-10, 0)]
def moveFoodOneStepAtRandom():
    """Move food one step at random."""
    global food
    tries = 0
    # While the direction is not valid, keep choosing a new direction.
    f = food.copy()
    direction = choice(directions)
    f.move(direction)
    while not inside(f) or f in snake:
        direction = choice(directions)
        f.move(direction)
        if tries == 4:
            break
        tries += 1

    food = f

def move():
    """Move snake forward one segment."""
    global framerate
    head = snake[-1].copy()
    head.move(aim)
    # Make the food move slower than the snake.
    if framerate == 3:
        moveFoodOneStepAtRandom()
        framerate = 0
    else:
        framerate += 1

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
info_alumnos()
hideturtle()

tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()