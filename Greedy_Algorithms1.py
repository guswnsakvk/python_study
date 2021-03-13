n = int(input())

lst = input().split()
lst.sort()

result = 0
count = 0

for i in lst:
    count += 1
    if count >= int(i):
        result += 1
        count = 0

print(result)