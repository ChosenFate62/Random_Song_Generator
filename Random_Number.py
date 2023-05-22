import random
randomNumber = random.randint(0,10)


while True:
    Response = int(input("Choose a number between 1 - 10: "))
    if Response == randomNumber:
        print("Congrats, you are correct. The number was {}".format(randomNumber))
        break
    else:
        print("Sorry you are incorrect, try again")