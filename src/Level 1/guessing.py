import random 

def play():
    print('\n****************************')
    print('Welcome to the guessing game')
    print('****************************\n')

    num_secret = random.randrange(1, 101)
    score = 1000

    print("Level (1): 20 attempts")
    print("Level (2): 10 attempts")
    print("Level (3): 05 attempts\n")

    level_str = input("Choose level: ")

    level = int(level_str)

    if(level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5

    for round in range(1, attempts + 1):

        print("Try {} of {}".format(round, attempts))

        num_user_str = input("Enter a number between 1 to 100: ")

        print("You typed: ", num_user_str)

        num_user = int(num_user_str)

        if(num_user < 1 or num_user > 100):
            print("Number out of valid range")
            continue

        smoller = (num_user < num_secret)
        bigger = (num_user > num_secret)
        right = (num_user == num_secret)

        if (right):
            print("You're right!\n")
            break
        else:
            if(smoller):
                print("You missed! Your number was smoller than the secret number!\n")
            elif(bigger):
                print("You missed! Your number was bigger than the secret number!\n")

        lost_points = abs(num_secret - num_user)
        score = score - lost_points

    print("\nThe secret number is: {}\n".format(num_secret))

    print("--------------------")
    print("GAME OVER")
    print("--------------------")
    print("Your final score: {}".format(score))
    print("--------------------")


if(__name__ == "__main__"):
    play()