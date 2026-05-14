import turtle
import math
import time 
import random
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Heart for name")
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.attributes('-topmost', True)
pen = turtle.Turtle()
pen.speed(0) 
pen.color("hotpink") 
pen.pensize(1)


screen.tracer(0, 0)


pen.penup()
pen.goto(-380, 350) 
pen.pendown()
pen.write("name", font=("Arial", 36, "bold"))
pen.penup()

center_x = 0
center_y = 0

num_lines = 1500

 
for i in range(num_lines):
    t = random.uniform(0, 2 * math.pi)
    
    
    hx = 16 * math.sin(t) ** 3
    hy = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    
    scale = 18
    hx *= scale
    hy *= scale
    
    pen.goto(center_x, center_y)
    pen.pendown()
    
    pen.goto(hx, hy)
    pen.penup()
    
    screen.update()
    
    time.sleep(0.005) 

pen.hideturtle()

turtle.done()
