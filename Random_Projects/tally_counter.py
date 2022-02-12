confident = 0
mediocre = 0
unconfident = 0

userInput = 0

while userInput != 9:
    userInput = input("How confident were you about the last question. \n(3 for confident, 2 for mediocre, 1 for unconfident): ")
    if int(userInput) == 3:
        confident += 1
    elif int(userInput) == 2:
        mediocre += 1
    elif int(userInput) == 1:
        unconfident += 1
    elif int(userInput) == 9:
        break
    else:
        print("Invalid input try again.")

    print('Current Tally:\nConfident: {}\nMediocre: {}\nUnconfident: {}'.format(confident, mediocre, unconfident))
    print('You are currently at {} out of 37.\n'.format((confident+ mediocre/2)))