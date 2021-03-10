n = int(input())

for i in range(1, n+1):
    if i < 10:
        if i == 3 or i == 6 or i == 9:
            print("X", end=" ")
        else:
            print(i, end=" ")
    else:
        if i / 10 == 3:
            if i == 3 or i == 6 or i == 9:
                print("XX", end=" ")
            else:
                print("X", end=" ")
        else:
            if i%10 == 3 or i%10 == 6 or i%10 == 9:
                print("X", end=" ")
            else:
                print(i, end=" ")