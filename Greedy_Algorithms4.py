n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 1

for i in data:
    if result < i:
        break
    result += i

print(result)