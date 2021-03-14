a, b = map(int, input().split())
data = list(map(int, input().split()))

result = 0

for i in range(a-1):
    for j in range(i+1, a):
        if data[i] != data[j]:
            result += 1

print(result)