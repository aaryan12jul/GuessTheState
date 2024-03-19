# Imports
import pandas
from turtle import Screen, Turtle
from time import sleep

def create_text(state):
    # Creates Turtle With Text
    guess = Turtle()
    guess.hideturtle()
    guess.color("black")
    guess.up()
    
    # Sets Position and Text of Turtle Based on Position Parameter which is the Index of the List
    row = csv[csv.state == state]
    guess.setpos(row.x.item(), row.y.item())
    guess.write(f"{row.state.item()}")
    
    # Updating Correct States Gussed
    global guessedStates
    guessedStates.append(row.state.item())

def exit():
    # Checks For Any States Not In Gussed States and Adds it To List
    outputCSV = [state for state in states if state not in guessedStates]
    # Creates CSV file out of Output List
    output = pandas.DataFrame(outputCSV)
    output.to_csv("States_Missed.csv")

# Setting Up Screen 
screen = Screen()
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")
screen.title("Guess the States")

# Setting Up Variables
csv = pandas.read_csv("50_states.csv")
states = csv.state.to_list()
guessedStates = []

# Game Loop
while True:
    # If You Have Guessed All The States
    if len(guessedStates) >= 50:
        guess = Turtle()
        guess.hideturtle()
        guess.color("black")
        guess.up()
        guess.setpos(0, 0)
        guess.write(f"You Win!", font=("Courier", 18, "normal"))
        break
    else:
        # Gets User Input For State
        guess = screen.textinput(f"{len(guessedStates)}/50 States Correct", "Enter a Name of a State | Type 'exit' to end game.").title()
        if guess == 'Exit':
            break
        
        # Checks For If The State Entered Is A Valid State
        for state in states:
            if guess.title() == state and guess.title() not in guessedStates:
                # Creates On Screen Text If State Is Valid
                create_text(state)
        
        # Wait One Second Before Next Iteration
        sleep(1)

# When Game Is Over, Run Exit Function
exit()