import random
a = [1, 2, 3, 4, 5]; b = [1, 2, 3, 4];
for x in a:
    for y in b:
        randno = random.randint(1, 99)
        print(randno, end=" ")
    print("\n")