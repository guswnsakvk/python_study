n = int(input())
sum = 0
num = 1
while True:
    sum += num
    if sum >= n:
        print(num)
        break
    else:
        num += 1