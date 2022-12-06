# pip install inputimeout

from inputimeout import inputimeout, TimeoutOccurred
import random

def get_difficulty():
    try:
        dif = int(input("""    *********************************************************************************
    In this mini game you will have to input the one character that is shown. 
    Make sure to hit hit enter fast after entering the character that differs.
    *********************************************************************************
    Choose difficulty:
    1. Hard
    2. Intermediate
    3. Beginner
    4. Easy
    
    > """))
        if (dif < 5 and dif > 0):
            return dif
        else:
            print("Invalid input, choosing Beginner.")
            return 3
    except:
        print("Invalid input, choosing Beginner.")
        return 3
        

def get_rand_char(char_list):
    return(random.choice(char_list))

def print_characters(random_char, level):
    length = 42
    left = random.randrange(start = 0, stop = length)
    right = length - left
    sep_char = "#"
    # print as many lines as levels
    level_loop = level
    while(level_loop > 0):
        print(f"{sep_char}"*left,random_char,f"{sep_char}"*right)
        level_loop -= 1

def game_loop(difficulty, rounds, wins, level):
    rounds += 1
    char_list = [".", ",", "*", "\"", "ç"]
    random_char = get_rand_char(char_list)
    print_characters(random_char, level)
    try:
        i = inputimeout(prompt=': ', timeout=difficulty)
        if(i == random_char):
            print("Win!")
            wins += 1
        else:
            print("Wrong!")
    except TimeoutOccurred:
        print('timeout')
    print(f"Wins: {wins}/{rounds}")
    game_loop(difficulty, rounds, wins, level)
rounds = 0
wins = 0
level = 1
difficulty = get_difficulty()
print(difficulty)
game_loop(difficulty, rounds, wins, level)
