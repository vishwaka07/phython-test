#Number guessing game
#make a variable, like winning_number and assign number to it
#Ask user to guess the no.
#if user guesses the correct no. then print YOU WIN!!
#if user didnt guess correctly
# - if user guessed no. lower then the actual no. then print too lower
# - if user guessed no. upper then the actual no. then print too high

win_number = 7
guess_number = input("guess the number in b/w 0 to 10: ")
guess_number = int(guess_number)
if guess_number == win_number:
    print("YOU WON !!!!")
else:
    if guess_number < win_number:
       print("TOO LOW")
    else:
       print("TOO HIGH")


