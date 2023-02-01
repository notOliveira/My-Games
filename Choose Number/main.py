# This game consists of the user choosing 5 numbers to compose their list of numbers between 1 and 20. The machine will randomly choose 5 numbers between 1 and 20 as well, if the user chooses at least one number equal to the machine, the player wins the game

import random
import time

# Game's defs

def menu():
    print('\n1 - Play the game\n2 - Quit\n')
    menuOption = input()
    if menuOption == '1':
        game()
    elif menuOption == '2':
        quitGame()
    else:
        invalidOption()
        menu()

def invalidOption():
    print('\n#############################################')
    print('\nInvalid option! Please choose a valid option!\n')
    print('#############################################')
def invalidNumber():
    print('\n#############################################')
    print('\nInvalid number! Please choose a valid number!\n')
    print('#############################################')
    
def quitGame():
    print('\nThank you for playing!\nQuiting in 3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)

def endgame():
    print('\n1 - Play again\n2 - Quit\n')
    response = input()
    if response == '1':
        game()
    if response == '2':
        quitGame()
    else:
        invalidOption()
        endgame()

def choose_n1():
    try:
        n1 = int(input('\nEnter with the first number: '))
    except ValueError or int(n1) < 1 or int(n1) > 20:
        invalidNumber()
        choose_n1()
    finally:
        if int(n1) < 1 or int(n1) > 20:
            invalidNumber()
            choose_n1()
        else:
            return int(n1)      
    
def choose_n2():
    try:
        n2 = int(input('\nEnter with the second number: '))
    except ValueError:
        invalidNumber()
        choose_n2()
    else:        
        if int(n2) < 1 or int(n2) > 20:
            invalidNumber()
            choose_n2()
        else:
            return int(n2)
    
def choose_n3():
    try:
        n3 = int(input('\nEnter with the third number: '))
    except ValueError:
        invalidNumber()
        choose_n3()
    else:
        if int(n3) < 1 or int(n3) > 20:
            invalidNumber()
            choose_n3()
        else:
            return int(n3)
    
def choose_n4():
    try:
        n4 = int(input('\nEnter with the fourth number: '))
    except ValueError:
        invalidNumber()
        choose_n4()
    else:   
        if int(n4) < 1 or int(n4) > 20:
            invalidNumber()
            choose_n4()
        else:
            return int(n4)
    
def choose_n5():
    try:
        n5 = int(input('\nEnter with the fifth number: '))
    except ValueError:
        invalidNumber()
        choose_n5()
    else:   
        if int(n5) < 1 or int(n5) > 20:
            invalidNumber()
            choose_n5()
        else:
            return int(n5)

def game():
    print("\nNow you're playing the game! I'll choose five numbers between 1 and 20 and you must choose five ones.\n\nIf you choose at least 1 number I thought, you win! Please enter with 5 numbers below:\n\n")
    
    # Generating a random list using random module
    randomArray = random.sample(range(1,20),5)
    randomArray.sort()
    
    n1 = choose_n1()
    n2 = choose_n2()
    n3 = choose_n3()
    n4 = choose_n4()
    n5 = choose_n5()
    
    playerArray = [n1,n2,n3,n4,n5]
    
    points = 0
    
    # Checking the points
    for i in randomArray:
        if i == n1:
            points += 1
        if i == n2:
            points += 1
        if i == n3:
            points += 1
        if i == n4:
            points += 1
        if i == n5:
            points += 1
        
    print('\nYour numbers are:\n{p1} - {p2} - {p3} - {p4} - {p5}'.format(p1 = playerArray[0], p2 = playerArray[1], p3 = playerArray[2], p4 = playerArray[3], p5 = playerArray[4]))
    print('\nMy 5 numbers are:\n{n1} - {n2} - {n3} - {n4} - {n5}'.format(n1 = randomArray[0], n2 = randomArray[1], n3 = randomArray[2], n4 = randomArray[3], n5 = randomArray[4]))
    
    # Win validation
    if points >= 1 and points <=4:
        print('\nYou win!\nScore: {score} points\nWhat do you want to do?'.format(score = points))
        endgame()
    elif points == 5:
        print('\nYou are the GREATEST!\nYou scored {score} points!\nWhat do you want to do?'.format(score = points))
        endgame()
    else:
        print('\nYou lose!\nWhat do you want to do?')
        endgame()

# Start game after file is executed
if __name__ == '__main__':
    print("Hello! You're playing my game right now!\nYou must choose between this two options:\n")
    menu()