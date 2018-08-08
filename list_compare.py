def solve(a, b):
    try:
        albo = [0, 0]
        list1 = a
        list2 = b
        a3 = len(list1)
        b3 = len(list2)
        if a3 > 0 and b3 > 0:
            if b3 < a3:
                a3 = b3
            for x in range(a3):
                if list1[x] > list2[x]:
                    albo[0] += 1
                elif list1[x] < list2[x]:
                    albo[1] += 1
        elif a3 > 0:
            albo[0] = a3
        else:
            albo[1] = b3
        return albo
    except Exception as e:
        print(e)


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = solve(a, b)
print(result)
