# Spyder Editor
# Created on Tue Sep 21 11:06:25 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 007 - 01 - Hangman Game

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)

# print(chosen_word)

lives = 6

print(hangman_art.logo)

display = []
for _ in chosen_word:
    display.append("_")

guessed_letters = []
    
while "_" in display:
    
    guess = input("Please guess a letter: ").lower()
    # print("\033[H\033[J")
    
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    
        correct_guess = False
        
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
                correct_guess = True
    
        print(f"{' '.join(display)}")
        
        if not "_" in display:
            print("You win.")
        
        if correct_guess == False:
            print(f"{guess} is not in the answer. You lose a life.")
            lives -= 1
            if lives == 0:
                print("You lose.")
                print(f"The correct answer is: {chosen_word}.")
                for index in range(len(chosen_word)):
                    display[index] = chosen_word[index]
            print(hangman_art.stages[lives])
    else:
        print(f"You have already guessed {guess}.")
    
    