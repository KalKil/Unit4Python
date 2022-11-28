from turtle import *

from random import randint, choice as rand_choice

speed(0)

colors = ['red', 'blue', 'green', 'gray', 'brown', 'orange', 'pink', 'cyan']

for i in range(100):
    penup()
    setposition(randint(-200, 200),randint(-200, 200))
    pendown()

    #color(rand_choice(colors))
    pencolor(rand_choice(colors))
    fillcolor(rand_choice(colors))
    pensize(3)
    
    begin_fill()
    circle(randint(10,50), steps=randint(4,10))
    end_fill()
    

done()