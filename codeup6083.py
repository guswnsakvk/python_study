a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = 0

for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            print("{0} {1} {2}".format(i,j,k))
            sum+=1

print(sum)