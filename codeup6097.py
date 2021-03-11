h, w = input().split()
w = int(w)
h = int(h)

arr = [[0 for j in range(w)] for i in range(h)]

n = int(input())

for i in range(n):
    a, d, x, y = input().split()
    a = int(a)
    d = int(d)
    x = int(x)
    y = int(y)
    if d == 0:
        for j in range(a):
            arr[x-1][y-1+j] = 1
    else:
        for j in range(a):
            arr[x-1+j][y-1] = 1

for i in range(0, h):
    for j in range(0, w):
        print(arr[i][j], end=" ")
    print()