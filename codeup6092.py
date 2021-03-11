lst = [0 for i in range(24)]

n = int(input())
a = input().split()

for i in range(n):
    lst[int(a[i])] += 1

for i in range(1,24):
    print(lst[i], end=" ")