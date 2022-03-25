# Snake Game

## Preview

![Circles]()


## Alumnos
Guillermo A01633790.
Roger A01620778.

## Instructions

```python
### THE COMMANDS ARE CASE SENSITIVE ###
# Undo
onkey(undo, 'u')
# Change Direction
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

```

## Funciones Guillermo

###  Mover la comida cada 3 pasos 

Esta función toma la posición inicial y final como el diametro. Procede a dibujar un circulo rellenado. <br>
Para obtener la circunferencia solamente, presiona `u` cuando el círculo este terminado.
```python
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

```

## Funciones Roger A01620778

### cambiar de color cada inicio de juego


```python
colors= ["black","red","green","blue","purple","yellow""blue"]
inex = randrange(0, len(colors)-1)
ine2 = randrange(0, len(colors)-1)
colorchoice  = colors[inex]
colorchoice2  = colors[inex-1]

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
        square(body.x, body.y, 9, colorchoice)

    square(food.x, food.y, 9, colorchoice2 )
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

```


## Colabs
### Guillermo Tafoya Milo
https://colab.research.google.com/drive/1KCIxfg9JsIIqshGDUJ83YhDpcLZAyZ74?usp=sharing
### Rogelio Sariñana Hernández
https://colab.research.google.com/drive/15LRPjMu89zDxggigDnmXgY4b5D5I4TnQ?usp=sharing
