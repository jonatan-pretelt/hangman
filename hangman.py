from hangman_art import logo, stages, won_display
from word_bank import word_list
import random
import os

print(logo)
secret_word = random.choice(word_list)
# print(secret_word)

display = []

for i in range(len(secret_word)):
    display.append('_')

print(display)

def start_new_game():
    print(logo)
    display = []
    secret_word = random.choice(word_list)
    print(secret_word)
    for i in range(len(secret_word)):
        display.append('_')
    return display, secret_word


game_on = True
lives = 6
guesses = []
def hangman(game_on, lives, secret_word, display, guesses):
    while game_on:
        user_guess = input("\nGuess a letter: ").lower()

        for letter_index in range(len(secret_word)):
            if user_guess == secret_word[letter_index]:
                display[letter_index] = user_guess
        os.system('cls')
        
        if user_guess not in secret_word and user_guess not in guesses:
            lives -= 1
        if lives == 0:
            os.system('cls')
            print(f'You Lose! \n The word was {secret_word}')
            continue_playing = input('Play again? (Yes/no) ')
            if continue_playing.lower() == 'yes':
                os.system('cls')
                # start_new_game()
                # print(logo)
                display = []
                lives = 6
                guesses = []
                secret_word = random.choice(word_list)
                # print(secret_word)
                for i in range(len(secret_word)):
                    display.append('_')
                game_on = True
            else:
                game_on = False
                os.system('cls')
                print('Thanks for playing. Bye!')
                return None
            
        print(logo)
        print(stages[lives])
        if user_guess in guesses:
            print(f"You already guessed {user_guess}\n")
        guesses.append(user_guess)
        print(display)
        if "_" not in display:
            os.system('cls')
            print(won_display)
            continue_playing = input('Play again? (Yes/no) ')
            if continue_playing.lower() == 'yes':
                os.system('cls')
                # start_new_game()
                print(logo)
                display = []
                lives = 6
                guesses = []
                secret_word = random.choice(word_list)
                # print(secret_word)
                print(stages[lives])
                for i in range(len(secret_word)):
                    display.append('_')
                game_on = True
                
            else:
                game_on = False
                os.system('cls')
                print('Thanks for playing. Bye!')
                return None

        
        print("\nPress Ctrl-C to stop playing...")


hangman(game_on, lives, secret_word, display, guesses)