name = input("Please, type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are in a dirt road, it has come to the end and you can go left or right. Type 'left' or 'right': ").lower()

if answer == "left":
    answer = input("You came to the river, you can walk around it or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swam across the river and have been eaten by an alligator. \nYou lose, try again. ")
        quit()
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
       print("Not a valid option. You lose.")
    
elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to him? (Yes/No) ").lower()
        if answer == "yes":
            print("You talk to the stranger and he gave you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and he is offended and you lose. ")
        else:
           print("Not a valid option. You lose.")
    else:
       print("Not a valid option. You lose.")

else: 
    print("Not a valid option. You lose.")
    
print("Thank you for trying", name)