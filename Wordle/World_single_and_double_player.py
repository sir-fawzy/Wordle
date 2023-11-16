import random
import re
import sys
from art import word, win, lose, out
print(word)

def main():
    print("Welcome to my Wordle game!\n")
    while True:
        bad_input = True
        while bad_input:
            mode = input("Do you want to play single or two-player mode?(s/t)")
            print()
            if mode.lower() == 's':
                print("You have selected the single player mode.\n")
                right_word = getRandomWord()
                bad_input = False
            elif mode.lower() == 't':
                print("You have selected the two player mode.\n")
                right_word = input("Player 1, please enter your word for player 2 to guess: ")
                print('_ '*len(right_word)+'\n')
                print(f"Player 2, it's your turn to play. Guess player 1's {len(right_word)} letter word.\n")
                bad_input = False
            else:
                print("You can only type 's' or 't'. Try again.\n")
                continue
            
            c_case = True    
            while c_case:
                case = input("Would you like your guess to be in upper, lower or random case?(upper/lower/random): ")
                print()
                if case.lower() == "upper":
                    print("You have selected upper case for your guesses.\n")
                    right_word = right_word.upper()
                    c_case = False
                elif case.lower() == "lower":
                    print("You have selected lower case for your guesses.\n")
                    right_word = right_word.lower()
                    c_case = False
                elif case.lower() == 'random':
                    print("You have selected random case for your guesses.\n")
                    selection = ['a', 'b']
                    r_word = ""
                    for word in right_word:
                        rand = random.choice(selection)
                        if rand == "a":
                           up = word.upper()
                           r_word += up
                        else:
                            down = word.lower()
                            r_word += down
                    right_word = r_word
                    c_case = False
                else:
                    print("You can only type 'upper', 'lower' or 'random'. Try again.\n")
                    continue
            
            attempts_count = 0
            correct = []
            wrong_input = True
            while wrong_input:
                difficulty_question= input("What level of difficulty do you want?(easy/medium/hard): ")
                print()
                difficulty_selection = re.fullmatch("(\w+)(?:\w+)?", difficulty_question)

                if difficulty_selection.group(1).lower() == "hard":
                    attempts = 2
                    wrong_input = False
                elif difficulty_selection.group(1).lower() == "medium":
                    attempts = 4
                    wrong_input = False
                elif difficulty_selection.group(1).lower() == "easy":
                    attempts = 6
                    wrong_input = False
                else:
                    print("Choose the correct difficulty.\n")
            print(f'You chose the {difficulty_question.lower()} difficulty, so you have {attempts} attempts.\n')

            while attempts-attempts_count != 0:
                user_guess = input(f"Enter your {len(right_word)} letter word: ")
                print()
                while True:
                    if len(user_guess) != len(right_word):
                        print("Incorrect length of words. Try again!\n")
                        user_guess = input(f"Enter your {len(right_word)} letter word: ")
                        continue
                    else:
                        break

                #pragma warning disable C0200 
                output = "" 
                space = " "
                for i in range(len(user_guess)):
                    if user_guess[i] == right_word[i]:
                        output += '\x1b[6;100;42m' + user_guess[i] + '\x1b[0m' + space
                        correct.append("yes")
                    elif user_guess[i] in right_word:
                        output += '\x1b[6;97;43m' + user_guess[i] + '\x1b[0m' + space
                    else:
                        output += '\x1b[6;97;41m' + user_guess[i] + '\x1b[0m' + space
                print(f'{output}')
                output = ""

                if len(correct) == len(right_word):
                    break
                else:
                    correct = []
                    attempts_count += 1

                if attempts-attempts_count == 1:
                    print(f'You have 1 attempt left.\n')
                elif attempts-attempts_count == 0:
                    pass
                else:
                    print(f'You have {attempts-attempts_count} attempts left.\n')

            if attempts-attempts_count == 0:
                print(lose)
                print("You have run out of attempts!\n")
                print(f'The correct word was {right_word}.\n')
            else:
                print(win)
                if attempts_count == 1:
                    print(f"Congratulations! You got the correct word with {attempts_count} failed attempt.\n")
                elif attempts_count == 0:
                    print(f"Congratulations! You got the correct word with no failed attempts.\n")
                else:
                    print(f"Congratulations! You got the correct word with {attempts_count} failed attempts.\n")
        while True:
            play = input("Do you want to play another round?(y/n) ")
            print()
            if play.lower() == "y" or play.lower() == "n":
                break
            else:
                print("You can only type 'y' or 'n'. Try again.\n")
                continue
        if play.lower() == "y":
            continue
        else:
            print(out)
            print("Goodbye, thank you for playing.")
            break


# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


main()