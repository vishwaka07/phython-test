#Number Guessing using module
import random
winning_number = random.randint(1,100)
print(winning_number)
guess = 1
num = int(input("Enter the number between 1 to 100: "))
game_over = False

while not game_over:
    if num == winning_number:
        print("\n")
        print(f"You Won !!!, number of attempt {guess} ")
        game_over = True
    else:
        if num < winning_number:
            print("Too Low")
            guess = guess + 1
            num = int(input("Try again, Enter the number: "))
        else:
            num > winning_number
            print("Too High")
            guess = guess + 1
            num = int(input("Try again, Enter the number: "))

            

