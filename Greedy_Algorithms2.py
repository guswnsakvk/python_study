data = input()
arr = []
j = 0
for i in range(len(data)):
    arr.append(int(data[j]))
    j += 1

if arr[0] == 0 or arr[1] == 0:
    result = arr[0] + arr[1]
else:
    result = arr[0] * arr[1]

for i in range(2, len(data)):
    if arr[i] != 0:
        result *= arr[i]
    else:
        continue

print(result)