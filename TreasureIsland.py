print("Welcome to Treasure Island. Your Mission is to find the treasure! ")
user = input("Do you want to go Left or Right ")
if user == "Right":
    print("Game Over!")
elif user == "Left":
    condition_two = input("Do you want to Swim or Wait ")
    if condition_two == "Swim":
        print("Game Over")
    elif condition_two == "Wait":
        condition_three = input("What door do you want to go into Red, or Blue ")
        if condition_three == "Red":
            print("Game Over!")
        elif condition_three == "Blue":
            print("You Win !")