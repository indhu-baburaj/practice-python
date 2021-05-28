import turtle
import random

elsa = turtle.Turtle()
turtle.Screen().bgcolor("honeydew")

colours = ["turquoise","deep pink", "orange","red", "violet","navy","maroon"]

elsa.color(random.choice(colours))

for i in range(80):
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)

    elsa.right(15)
    elsa.color(random.choice(colours))
