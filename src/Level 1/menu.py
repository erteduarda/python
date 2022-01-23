from tkinter import E
import guessing
import force

def menu():
    print('****************************')
    print('***********Games************')
    print('****************************\n')

    print("Game 1: Guessing")
    print("Game 2: Force")

    game_str = input("Select Game: ")
    game = int(game_str)

    if(game == 1):
        guessing.play()
    else:
        force.play()

if(__name__ == "__main__"):
    menu()