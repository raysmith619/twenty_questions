# twenty_questions.py 19Apr2021  crs  Git
#                     12Aug2020 crs
"""
first iteration of tq
+ Prompt user for number
+ Set up target, check for match
Use integer values
+ Check / Report too high, low,..
+ Randomize the target
+ Add preamble with range
+ Add multiple game support
+ Protect against typos - ask again
+ Support letter guesses
"""

import random
target_hi = 20      # High end of target
target_hi = 30      # High end of target
###target_hi = 5    # TFD
target_low = 1      # LOW END OF TARGET
game_type = "NUMBER"    # Default game type
game_by_letter = {
    'n' : "NUMBER",
    'l' : "LETTER",
    'w' : "WORD",
    }
letter_list = "abcdefghijklmnopqrstuvwxyz"

print("Welcome to our guessing game!")
print("Please choose the type of guessing you want")
while True:
    inp = input("N for numbers, L for letters, or W for words: ")
    if inp == "":
        inp = 'n'
    choice = inp.lower()[0]
    if choice in game_by_letter:
        game_type = game_by_letter[choice]
        if game_type == "WORD":
            print(f"Don't have game {game_type} working yet")
            continue
        
        break
    print(f"I couldn't understand {inp}. Please try again.")
if game_type == "LETTER":
    if target_low < 1 or target_low > len(letter_list):
        target_low = 1
    if target_hi < 1 or target_hi > len(letter_list):
        target_hi = len(letter_list)
    t_low = chr(ord(letter_list[0])+target_low-1)
    t_hi = chr(ord(letter_list[0])+target_hi-1)
    t_type = "letter"
elif game_type == "NUMBER":
    t_low = target_low
    t_hi = target_hi
    t_type = "number"
else:
    print(f"Sorry we don't yet play game type {game_type}")
    exit()
            
preamble = f"""
I'm thinking of a {t_type} between {t_low} and {t_hi}
Can you guess it?  Remember to press the ENTER key
to enter your guess.  Good Luck!
"""
print(preamble)
while True:
    target = random.randint(target_low, target_hi)
    while True:
        inp = input(f"Enter Guess (between {t_low} and {t_hi}):")
        print("Guess:", inp)
        if game_type == "NUMBER":
            try:
                guess = int(inp)    # Convert to integer
            except:
                print(f"I don't recognize '{inp}' as a number"
                      " please try again.")
                continue
            guess_pos = guess
        elif game_type == "LETTER":
            guess = inp.lower()
            if len(guess) < 1:
                print("You must enter one letter")
                continue
            if len(guess) > 1:
                print("Please enter only one letter at a time")
                continue
            if guess not in letter_list.lower():
                print(f"Sorry, Your input: {inp} was not one of {letter_list}")
                continue
            guess_pos = ord(guess) - ord(letter_list[0]) + 1
        if guess_pos < target:
            print("Sorry your input of", guess, "is too low.")
            continue
        if guess_pos > target:
            print("Sorry your input of", guess, "is too high.")
            continue
        
        if guess_pos == target:
            print(f"Congratulations {guess} is my {t_type}!")
            break       # End this game

    print("Play a new game?")
    inp = input("Enter N to quit: ")
    if inp == "N" or inp == "n":
        break
print("See you next time.")
