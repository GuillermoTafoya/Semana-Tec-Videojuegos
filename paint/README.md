# Paint Game

## Preview

![Circles](./assets/CIRCLES%20N%20COLORS.png)

## Instructions
```python
### THE COMMANDS ARE CASE SENSITIVE ###

# Undo
onkey(undo, 'u')

# Change Color
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('purple'), 'P')

# Change Shape
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
```
