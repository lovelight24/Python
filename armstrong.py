import math
import os
def check_armstrong(Num):
	Result = 0;
	str_num = str(Num)
	for i in str_num:
		b = math.pow(int(i),3)
		print(b," ", i)
		Result += b
	if Result==Num:
		print("Numer is Armstrong.")
	else:
		print("Number is Not armstrong.")

if __name__ == "__main__":
	os.system("cls")
	Num = int(input("Please Enter a Number: "))
	check_armstrong(Num)
