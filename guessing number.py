import random
number = random.randint(0,10)
user = 0

while user != number:
    user = int(input("enter the guess:"))

    ## return the string if needed

    if (user > number):
        print("guess is higher")
    elif (user < number):
        print("guess is lower")
    else:
        print("done")



