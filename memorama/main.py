"""Memory, puzzle game of number pairs.
Exercises:
1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from tkinter import X
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ["Aguascalientes"," Baja California", "Baja California Sur", "Campeche"," Coahuila", "Colima"," Chiapas", "Chihuahua"," Durango", "Distrito Federal"," Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León"," Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz"," Yucatán","Zacatecas"]*2
state = {'mark': None}
hide = [True] * 64
taps = 0
writer = Turtle()
writer.hideturtle()
#Display Autors
def info_alumnos():
    
    x = -240
    y = 230
    writer.up()
    writer.goto(x,y)
    writer.color('red')
    writer.write('Guillermo Tafoya Milo A01633790', align='left', font=('Arial', 10, 'normal'))
    writer.goto(x,y-20)
    writer.color('blue')
    writer.write('Rogelio Zaid Sariñana Hernández A01620778', align='left', font=('Arial', 10, 'normal'))

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200



def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global taps
    taps += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

writer2 = Turtle()
writer2.hideturtle()
def draw():
    """Draw image, number of taps and tiles."""
    writer2.clear()
    writer2.up()
    writer2.goto(40, 220)
    writer2.color('green')
    writer2.write('Taps: ' + str(taps), align='left', font=('Arial', 10, 'normal'))


    clear()
    goto(0, 0)
    shape(car)
    stamp()
    win()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 10, 'normal'))

    update()
    ontimer(draw, 100)

def win():
    """Display winning message."""
    if sum(hide) == 0:
        clear()
        writer.clear()
        writer2.clear()
        write('Ganaste un auto!!, Felicidades', align='center', font=('Arial', 20, 'normal'))


shuffle(tiles)
setup(500, 500, 370, 0)
info_alumnos()
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()