import colorgram
import turtle as t
import random as r


colors = colorgram.extract('spot_painting.jpg', 50)

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()




#print(tuple(colors[1].rgb))

colorTuple = []
for color in colors[4:]:
    colorTuple.append(tuple(color.rgb))

tim.penup()
xCor = -200
yCor = -200


for row in range (10):
    tim.teleport(xCor, yCor+(row*50))
    for _ in range(10):
        tim.fillcolor(r.choice(colorTuple))
        tim.begin_fill()
        tim.circle(10, steps=100)
        tim.end_fill()
        tim.forward(30)
    




screen = t.Screen()
screen.exitonclick()


