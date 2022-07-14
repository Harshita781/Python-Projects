import random

from Guess_logo import logo

print(logo)
number = random.randint(0, 100)
level=input("Choose the level: Easy, Medium,Hard:\n")
if(level=='easy'):
    attempt=10
elif(level=='medium'):
    attempt=7
else:
    attempt=5
print(f"You got {attempt} attempts to guess the number")
point=0
for i in range(0,attempt):
    guess=int(input("Enter the number to guess: "))
    if(guess==number):
        print(f"You won!! and you have {attempt-i-1} attempts left")
        point=1
        break
    elif(guess>number):
        print("Too high")
        print(f"You have only {attempt-i-1} attempts left now")
    elif(guess<number):
        print("Too low")
        print(f"You have only {attempt-i-1} attempts left now")
if(point==0):
    print("You lose and you have no more attempts")