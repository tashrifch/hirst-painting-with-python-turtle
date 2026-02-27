from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ['CornflowerBlue', 'DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray', 'SeaGreen']


def draw_shape(shape):
    angle = 360/shape
    

    for lines in range(shape):
        tim.forward(100)
        tim.left(angle)


for shapes in range(3,11):
    draw_shape(shapes)
    tim.color(random.choice(colors))



screen = Screen()
screen.exitonclick()




