from turtle import *
import turtle
CoderMohit = turtle.Screen()

CoderMohit.bgcolor('white')


for angle in range (0,360,15):
    setheading(angle)
    forward(100)
    write(str(angle)+'`')
    backward(100)

CoderMohit.mainloop()