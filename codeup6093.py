n = int(input())
a = input().split()
arr = []

for i in range(n):
    arr.append(int(a[i]))

arr.reverse()

for i in range(n):
    print(arr[i], end=" ")