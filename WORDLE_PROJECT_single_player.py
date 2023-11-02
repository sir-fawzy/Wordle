def main():
    while True:
        
        import re
        right_word = "stack"
        attempts_count = 1
        correct = []
        difficulty_question= input("What level of difficulty do you want? ")
        difficulty_selection = re.fullmatch("(\w+)(?:\w+)?", difficulty_question)

        if difficulty_selection.group(1).lower() == "hard":
            attempts = 2
        elif difficulty_selection.group(1).lower() == "medium":
            attempts = 4
        else:
            attempts = 6
        
        while attempts_count <= attempts:
            user_guess = input(f"You have {attempts+1-attempts_count} attempts left.\nEnter a 5 letter word? ")
            user_guess = user_guess.lower()
            while True:
                if len(user_guess) > 5 or len(user_guess) < 5:
                    print("Incorrect length of words\nTry again!")
                    user_guess = input(f"You have {attempts-attempts_count} attempts left.\nEnter a 5 letter word?")
                    continue
                else:
                    break

            #pragma warning disable C0200  
            for i in range(len(user_guess)):
                if user_guess[i] == right_word[i]:
                    print(f"{user_guess[i]} - green")
                    correct.append("yes")
                elif user_guess[i] in right_word:
                    print(f"{user_guess[i]} - Yellow")
                else:
                    print(f"{user_guess[i]} - red")
            
            if len(correct) == len(right_word):
                break
 
            else:
                correct = []
                attempts_count += 1
        if attempts_count > attempts:
            print("You have run out of attempts!")
        
        else:
            if attempts_count == 1:
                print(f"You got the correct word with {attempts_count} trial")
            else:
                print(f"You got the correct word with {attempts_count} trials")
        play = input("Do you want to play another round?(y/n) ")
        if play.lower() == "y":
            continue
        else:
            break

main()




"""for i in range(len(user)):
            for j in range(len(right_word)):
                if i == j and user[i] == right_word[j]:
                    print(f"{user[i]} - green")
                elif user[i] == right_word[j]:
                    print(f"{user[i]} - Yellow")
            if user[i] not in right_word:
                print(f"{user[i]} - red")   """