# Question: Build a classic 'Snake, Water, Gun' game with random computer choices and input validation.

import random
try:
    computer = random.choice([1, 2, 3])

    youstr = input("Enter Your Choice: ")

    choices = {"s": 1,"w": 2,'g': 3}

    you = choices[youstr]

    reverse_choice = {1: 'Snake', 2: "Water", 3: "Gun"}

    print(f'You Choose {reverse_choice[you]}\nComputer Choose {reverse_choice[computer]}')
    if computer == you:
        print('Draw 🎭')
    elif computer == 1 and you == 2:
        print('You Lose')
    elif computer == 2 and you == 1:
        print('You Won')
    elif computer == 1 and you == 3:
        print('You Won')
    elif computer == 3 and you == 1:
        print('You Lose')
    elif computer == 2 and you == 3:
        print('You Won')
    elif computer == 3 and you == 2:
        print('You Lose')
    else:
        print('Something Wronge')
except KeyError:
    print('Wronge Choice')