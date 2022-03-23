"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle2(start, end):
    """Draw circle taking the end position as the diameter."""
    if start.y > end.y:
        start.y,end.y = end.y,start.y
    if start.x > end.x:
        start.x,end.x = end.x,start.x
    
    x2 = end.x
    x1 = start.x
    y2 = end.y
    y1 = start.y
    up()
    radius = ((y2-y1)**2+(x2 - x1)**2)**(1/2) / 2
    goto((x2+x1)/2, (y2+y1)/2 - radius)
    down()
    begin_fill()
    circle(radius) # distance between start and end
    end_fill()

def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO

def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
### THE COMMANDS ARE CASE SENSITIVE ###
# Undo
onkey(undo, 'u')
# Color changes
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
<<<<<<< Updated upstream
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('purple'), 'P')

# Shapes
=======
onkey(lambda: color('purple'), 'P')
onkey(lambda: color('yellow'), 'Y')
>>>>>>> Stashed changes
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()