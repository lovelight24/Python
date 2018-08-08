from random import randint
from os import system


def userInput():
    try:
        system("cls")
        userput = input("Please Enter any Four Digit Number: ")
        if len(userput) >= 4:
            IntNum = int(userput)
        else:
            main()
        return userput
    except Exception as e:
        print(e)


def Check_cow_bull(Num):
    randnum = randint(0000, 9999)
    NumList = list(Num)
    print("Number is %s, Random Number is %d" % (Num, randnum))
    i = 0
    cow = 0
    bull = 0
    for x in str(randnum):
        if x == NumList[i]:
            cow += 1
        else:
            bull += 1
        i += 1
    print("You Have %d Cow and %d Bull" % (cow, bull))


def main():
    Guess = userInput()
    Check_cow_bull(Guess)

if __name__ == "__main__":
    main()
