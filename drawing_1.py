from turtle import *
from random import randint, uniform

def draw_random_spiral():

    bgcolor('black')
    x=1
    speed(0)
    
    while x < 400:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        colormode(255)
        pencolor(r, g, b)
        pensize(randint(1, 3))
        fd(50 + x)
        rt(uniform(80, 100))
        x = x + 1

    exitonclick()

def draw_white_spiral():

    bgcolor('black')
    x=1
    speed(0)
    
    while x < 400:
        colormode(255)
        pencolor(255, 255, 255)
        fd(50 + x)
        rt(90.991)
        x = x + 1

    exitonclick()

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for random spiral, 2 for white spiral, 0 to exit)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 0:
            print("\nThank you! Bye.")
            break
        if a == 1:
            draw_random_spiral()
        elif a == 2:
            draw_white_spiral()
        else:
            print("Please input the value in [0,1,2]")
    except:
        print("Please input the value in [0,1,2]")