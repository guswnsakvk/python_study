n = int(input())
a = input().split()
arr = []

for i in range(n):
    arr.append(int(a[i]))

arr.sort()

print(arr[0])