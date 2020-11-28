import random
guesses = 1
lower = int(input("enter the lower bound"))
upper = int(input("enter the upper bound"))
num = random.randint(lower, upper + 1)
#print(num)
guess = int(input("enter the guess number"))
while True:
    guesses += 1  # to count the number of guesses made
    if num > guess:
        print("you guessed too low")
        lower = guess + 1
        guess = int(input("guess the number between {} and {}".format(lower,upper)))
    elif num < guess:
        print("you guessed too high")
        upper = guess - 1
        guess = int(input("guess the number between {} and {}".format(lower, upper)))
    elif num == guess:
        print("yay! you guessed the number {} in {} guesses.".format(guess,guesses))
        break

