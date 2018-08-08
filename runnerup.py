def search_runnerup(list):
    a = -100
    b = -100
    c = -100
    for x in list:
        if x>a :
            if b>c:
                c = b
            if a>b:
                b = a
            a = x
        elif x<a and x>b and x>c:
            if b>c:
                c = b
            b = x
        elif x<b and x>=c:
            c = x;
    return b;

if __name__ == '__main__':
	n = int(input())
	if n>=2 or n<=10:
		arr = list(map(int, input().rstrip().split()))
		runup = search_runnerup(arr)
		print(runup)