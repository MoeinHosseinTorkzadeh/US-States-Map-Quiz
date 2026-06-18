import turtle
from turtle import Turtle,Screen
import pandas as pd



def write_state(text,file_path):
    """Gets the coordinate of correct state entered by user and write the name of it on the map"""
    pointer = Turtle()
    pointer.penup()
    pointer.hideturtle()
    coordinate = find_coordinate( user_input= text, dataset= file_path)
    if not coordinate:
        return
    else:
        pointer.goto(coordinate)
        pointer.write(f'{text}', font=("Arial", 12, "bold"), align="center")
def find_coordinate(user_input, dataset):
    """Based on the dataset of US states, it will go through the csv file and returns the coordinates of corresponding state (x,y)"""
    states = pd.read_csv(f'{dataset}')
    us_states_dic = states.to_dict()

    for key,value in us_states_dic.items():
        if key == "state":
            for code,stat in us_states_dic['state'].items():
                if user_input == stat:
                    x_coor = states.x[code]
                    y_coor = states.y[code]
                    location_tuple= (x_coor,y_coor)
                    correct_guess(user_input)
                    return location_tuple
def correct_guess(country):
    """Adds the correct state to the already guessed list"""
    already_guessed.append(country)
# Setting up the screen
screen= Screen()
screen.title('U.S. States Game')
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.screensize(725,491)
game_is_on=True
already_guessed = [] # Already guessed states will be stored here

#! Tip_________Type Exit to get the .csv file of missed states____________
while game_is_on:
    try:
        # getting the user input
        answer_state=screen.textinput(title=f"{len(already_guessed)}/50 States Correct",prompt="What's another state's name?").title()
        if answer_state == "Exit":
            states_of_us= pd.read_csv('50_states.csv')
            all_states = states_of_us.state.to_list()
            missed_states = list(set(all_states) - set(already_guessed))
            missed_states_dic = {
                "Missed States":missed_states
            }
            new_data = pd.DataFrame(missed_states_dic)
            new_data.to_csv("Missed States.csv")
            game_is_on = False


        elif answer_state not in already_guessed:
            write_state(text=answer_state, file_path='50_states.csv')
            print(already_guessed)
            if len(already_guessed) == 50:
                end = Turtle()
                end.color("green")
                end.hideturtle()
                end.write('You Successfully Guessed all States', font=("Arial", 50, "bold"), align="center")
                game_is_on = False
    except AttributeError:
        end = Turtle()
        end.color("red")
        end.hideturtle()
        end.write('Game Finished', font=("Arial", 50, "bold"), align="center")
        game_is_on = False
screen.mainloop()

