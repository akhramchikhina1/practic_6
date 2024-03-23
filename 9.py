import turtle
import math
x1 = float(input('Введите координаты х окружности: '))
y1 = float(input('Введите координаты у окружности: '))
r1 = float(input('Введите радиус окружности: '))
x2 = float(input('Введите координаты х окружности: '))
y2 = float(input('Введите координаты у окружности: '))
r2 = float(input('Введите радиус окружности: '))
turtle.penup()
turtle.goto(x1, y1 - r1)
turtle.pendown()
turtle.pencolor('black')
turtle.circle(r1)
turtle.penup()
turtle.goto(x2, y2 - r2)
turtle.pendown()
turtle.pencolor('black')
turtle.circle(r2)
turtle.penup()


dist= math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if dist > r1 + r2:
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write("Окружности лежат одна вне другой, не касаясь")
elif dist == r1 + r2:
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write("Окружности имеют внешнее касание")
elif dist < (r1 + r2) and dist > (abs(r1 - r2)):
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write("Окружности пересекаются")
elif dist == abs(r1 - r2):
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write("Окружности имеют внутреннее касание")
elif dist < abs(r1 - r2):
    turtle.pendown()
    turtle.pencolor('red')
    turtle.write("Одна окружность лежит внутри другой, не касаясь")
turtle.done()