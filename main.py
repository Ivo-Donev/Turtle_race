
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=530, height=430)
colors = ["red", "orange", "blue", "brown", "green", "purple", "pink"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
is_race_on = False

for turtle_i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_i])
    new_turtle.goto(-250, y_positions[turtle_i])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle will win the race? Enter a color:")
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won!, The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost!, The {winning_color} turtle is the winner!")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)

screen.exitonclick()
