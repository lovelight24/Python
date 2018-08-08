decimal_val = 0
base = 1
num = int(input("Please Enter a Binary Number: "))
binary_num = num
while num>0:
	rem = num%10
	decimal_val = decimal_val+rem*base
	num = num//10
	base = base*2
print("Binary Number is: %d" %(binary_num))
print("Decimal Number is: %d" %(decimal_val))