right_word = "retina"
user = input("6 letter word? ")
while True:
    
    if len(user) > 6 or len(user) < 6:
        print("Incorrect length of words\nTry again!")
        user = input("6 letter word? ")
        continue
    else:
        break
for i in range(len(user)):
    for j in range(len(right_word)):
        if i == j and user[i] == right_word[j]:
            print(f"{user[i]} - green")
        elif user[i] == right_word[j]:
            print(f"{user[i]} - Yellow")
    if user[i] not in right_word:
        print(f"{user[i]} - red")   
