import random
import time

print("\tWelcome to Rock Paper Scissors Game !!")

while True:
    try : 
            Player1 = int(input("\t Choose a Number ! \n\t 1)Rock \n\t 2)Paper \n\t 3)Scissor \n\t\t > "))
            if Player1 > 3 or Player1 < 1:
                print("Write a Number Between [1-3] Please !")
            else:
                break

    except ValueError : 
        print("\nThats Not A Number !")


if Player1 == 1:
    print("You Choosed a Rock !!")
elif Player1 == 2:
    print("You Choosed a Paper !!")
elif Player1 == 3:
    print("You Choosed a Scissor !!")

cpu = random.randint(1,3)

if cpu == 1:
    print("CPU Choosed a Rock !!\n")
elif cpu == 2:
    print("CPU Choosed a Paper !!\n")
elif cpu == 3:
    print("CPU Choosed a Scissor !!\n")

time.sleep(1)

#THE BATTLE !!

if Player1 == cpu:
    print("ITS A DRAW !!")
elif Player1 == 1:
    if cpu == 2:
        print("You Lost !")
    elif cpu == 3:
        print("You Won !")
elif Player1 == 2:
    if cpu == 1:
        print("You Won !")
    elif cpu == 3:
        print("You Lost !")
elif Player1 == 3:
    if cpu == 2:
        print("You Won !")
    elif cpu == 1:
        print("You Lost !")