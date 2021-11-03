# This is rock-paper-scissors game
# The user inputs R, P, or S, and the "computer" outputs R, P, or S.
# 
# Ideas: scoreboard?
import random, time

answers = ('r', 'p', 's')

print("Choose rock (r), paper (p), or scissors (s) - or quit (q).")
userChoice = input("Player Choice: ")

while (userChoice != 'q'):

    time.sleep(0.25)

    rand = random.randint(0, 2)
    compChoice = answers[rand]
    print('Computer Choice:', compChoice)

    time.sleep(0.25)

    if (userChoice == 'r'):
        if (compChoice == 'r'):
            print('Draw!')
        elif (compChoice == 'p'):
            print('You Lose!')
        else:
            print('You Win!')
    elif (userChoice == 'p'):
        if (compChoice == 'p'):
            print('Draw!')
        elif (compChoice == 's'):
            print('You Lose!')
        else:
            print('You Win!')
    else:
        if (compChoice == 's'):
            print('Draw!')
        elif (compChoice == 'r'):
            print('You Lose!')
        else:
            print('You Win!')
    
    userChoice = input("Player Choice: ")
    
time.sleep(0.25)
print('See You Next Time!')
exit()