import turtle
import random

screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()
screen.setup(width=1.0, height=1.0)

def turtle_one():
    turtle1 = turtle.Turtle()
    turtle1.shape("turtle")
    turtle1.color("pink") 
    turtle1.setheading(90)
    turtle1.penup()
    turtle1.goto(-width/2 + 30, -height/2 + 30)
    turtle1.pendown()  
    return turtle1
    
def turtle_two():
    turtle2 = turtle.Turtle()
    turtle2.shape("turtle")
    turtle2.color("purple")
    turtle2.setheading(90)
    turtle2.penup()
    turtle2.goto(0, -height/2 + 30)
    turtle2.pendown()
    return turtle2
     
def turtle_three():
    turtle3 = turtle.Turtle()
    turtle3.shape("turtle")
    turtle3.color("light blue")
    turtle3.setheading(90)
    turtle3.penup()
    turtle3.goto(width/2 - 30, -height/2 + 30)
    turtle3.pendown()
    return turtle3

t1 = 50
t2 = 25
t3 = 12
stop_y = height / 2 - 50 
winner_declared = False

def move_turtle1():
    global winner_declared
    if not winner_declared:
        move = random.choice([t1, t2, t3])
        if turtle1.ycor() + move >= stop_y:
            turtle1.goto(turtle1.xcor(), stop_y)
            winner_declared = True
            print("Pink Turtle wins!")
        else:
            turtle1.forward(move)
        if not winner_declared:
            screen.ontimer(move_turtle1, 100)

def move_turtle2():
    global winner_declared
    if not winner_declared:
        move = random.choice([t1, t2, t3])
        if turtle2.ycor() + move >= stop_y:
            turtle2.goto(turtle2.xcor(), stop_y)
            winner_declared = True
            print("Purple Turtle wins!")
        else:
            turtle2.forward(move)
        if not winner_declared:
            screen.ontimer(move_turtle2, 100)

def move_turtle3():
    global winner_declared
    if not winner_declared:
        move = random.choice([t1, t2, t3])
        if turtle3.ycor() + move >= stop_y:
            turtle3.goto(turtle3.xcor(), stop_y)
            winner_declared = True
            print("Light blue Turtle wins!")
        else:
            turtle3.forward(move)
        if not winner_declared:
            screen.ontimer(move_turtle3, 100)

user_choice = input("Welcome to the Turtle racing game! How many turtles do you want to race? Pick a number between 2 and 3: ")
        
if user_choice == "2":
    turtle1 = turtle_one()
    turtle2 = turtle_two()
    move_turtle1()
    move_turtle2()
elif user_choice == "3":
    turtle1 = turtle_one()
    turtle2 = turtle_two()
    turtle3 = turtle_three()
    move_turtle1()
    move_turtle2()
    move_turtle3()

screen.mainloop()

