import random
randomNumber = random.randint(0,100)
def higher_Or_Lower(Response):
    if Response > randomNumber:
        print("Your number is higher than the random number")
    else:
        print("Your number is lower than the random number")

while True:
    Response = int(input("Choose a number between 1 - 100: "))
    if Response == randomNumber:
        print("Congrats, you are correct. The number was {}".format(randomNumber))
        break
    else:
        print("Sorry you are incorrect, try again")
        higher_Or_Lower(Response)
