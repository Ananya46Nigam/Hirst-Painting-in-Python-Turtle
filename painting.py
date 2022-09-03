import turtle as turtle_module
import random
import colorgram as c
# colours = c.extract("image.jpg", 40)
# print(colours)
# after printing on console copy these colours and make color_list

turtle_module.colormode(255)#since I am using rgb color values

toto = turtle_module.Turtle()#turtle of name toto created

toto.speed("fastest")#speed of moving turtle

toto.penup()#to make the line/path invisible

toto.hideturtle()#to make the turtle itself invisible

#using colorgram module
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
toto.setheading(225)#direction angle of turtle
toto.forward(300)
toto.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):#to make 100 dots and +1 as range does not contain the last integer
    toto.dot(20, random.choice(color_list))
    toto.forward(50)
# dimension is 10X10
    if dot_count % 10 == 0:# make 10 dots per line
        toto.setheading(90)
        toto.forward(50)
        toto.setheading(180)
        toto.forward(500)
        toto.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()