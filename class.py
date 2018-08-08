a=[1,2,5,6,7,8,9,3,333,56,787,23,333]
b=[1,2,5,6,7,8,9,23,33,233,33,233]
x=1
while x==1:
    num1=int(input("plz enter no from 1,2,3: "))
    if num1==1:
        print(a)
        x=0
    elif num1==2:
        print(b)
        x=0
    elif num1==3:
        print(a)
        print(b)
        x=0
    else:
        print("Please select value from only 1,2,3")
        x=1