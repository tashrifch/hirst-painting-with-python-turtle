from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ['CornflowerBlue', 'DarkOrchid','IndianRed','DeepSkyBlue','LightSeaGreen','wheat','SlateGray', 'SeaGreen']

rightLeft = ["right","left"]
forBack = ["forward","backward",]
tim.speed("fastest")


#anther way to do it is with tim.setheading and giving it the angles 0 90 180 270

for num in range(100):
    tim.color(random.choice(colors))
    tim.pensize(5)


    righ_Or_Left = random.choice(rightLeft)
    forward_Or_Backward = random.choice(forBack)

    if righ_Or_Left == "right":
        tim.right(90)
    else:
        tim.left(90)

    if forward_Or_Backward == "forward":
        tim.forward(10)
    elif forward_Or_Backward == "backward":
        tim.back(10)
    
    




screen = Screen()
screen.exitonclick()