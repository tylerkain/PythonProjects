from turtle import Turtle, Screen
import random


def turtle_race():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)

    user_bet = screen.textinput(title="Make Your Bet", prompt=" Which Turtle Win the Race: ")
    print(user_bet)
    colors = ["red", "blue", "green", "indigo", "yellow", "orange", "violet"]
    y_position = [-100, -80, -60, -40, -20, 0]
    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-330, y=y_position[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtles in all_turtles:
            if turtles.xcor() > 230:
                is_race_on = False
                winning_color = turtles.pencolor()
                if winning_color == user_bet:
                    print(f" Winner is {winning_color}")
                else:
                    print(f"Winner: {winning_color}")

            distance = random.randint(0, 10)
            turtles.forward(distance)

    screen.exitonclick()


turtle_race()

