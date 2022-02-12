import random
import sys
def playgame():
    global restart
    guesses = 6
    num = random.randint(1,20)
    answer = 0
    while num!= answer and guesses > 0:
        answer = int(input("Guess the number "))
        guesses -= 1
        if answer < num:
            print("Higher, number of guesses left: " +str(guesses))
        elif answer < num:
            print("Lower, number of guesses left: " +str(guesses))
        elif answer == num:
            print("Conrrect, the number was: " +str(num))
            restart = input("Another game? Answer yes or no ").lower()
    if answer != num:
        print("That was your last guess, sorry, the number was: " +str(num))
        restart = input("Another game? Answer yes or no ").lower()
playgame()
restart = "yes"
if restart == "yes":
    playgame()
else:
    sys.exit("Good nignt!!")

