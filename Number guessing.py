#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number,result,attempts):
    if guessed_number < result:
        print("Your guess is too low")
        return attempts - 1
    elif guessed_number > result:
        print("your guess is too high")
        return attempts - 1
    else:
        print(f"Your guess is right...The answer was {result}")
def game():
    print("Think a number between 1 to 40: ")
    result = random.randint(1,40)
    print(result)
    level = input("Choose level of difficulty:'easy' or 'hard':")
    attempts = set_difficulty(level)
    guessed_number = 0
    
    while guessed_number!=result:
        print(f"you have {attempts} remaining to guess the number:")
        guessed_number = int(input("Guess the number:"))
        attempts = check_answer(guessed_number,result,attempts)
        if attempts == 0:
            print("you are out of guesses...You lose!")
            return
        elif guessed_number!=result:
            print("Guess again")
game()
        


# In[ ]:




