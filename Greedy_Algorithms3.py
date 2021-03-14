data = input()
arr = []
j = 0
for i in range(len(data)):
    arr.append(int(data[j]))
    j += 1

count_0 = 0
count_1 = 0

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == 1:
            count_0 += 1
        else:
            count_1 += 1
    else:
        continue

print(min(count_0, count_1))