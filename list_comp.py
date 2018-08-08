x = int(input("Please Enter X: "))
y = int(input("Please Enter Y: "))
z = int(input("Please Enter Z: "))
N = int(input("Please Enter N: "))

hecilogic = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)!=N:
                list = [i,j,k]
                hecilogic.append(list)
print(hecilogic)