a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)
count = 1

while True:
    if n == 1:
        print(a)
        break
    else:
        a *= r
        count += 1
        if(count == n):
            print(a)
            break