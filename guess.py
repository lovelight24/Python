import random
import os



def game():
  userinput  = input('Enter No between 0 to 9 :')
  randNumber = random.randint(1,9)
  try:
    val = int(userinput)
    if val == randNumber:
     print("Congratulation You Guess Right Number");
    else:
        print("rand Number is {} and your Number is {}".format(randNumber,userinput))
        if val > randNumber:
          print("Value is Grater Than To Your Number ")
        else:
          print("Value is Less Than To Your Number")
    game()
  except ValueError:
      if userinput == 'exit' or userinput == 'out':
       print("good Bye!")


game()