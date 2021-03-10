n = int(input())
sum = 0
sum_num = 1

while True:
    if sum >= n:
        print(sum)
        break
    else:
        sum += sum_num
        sum_num += 1