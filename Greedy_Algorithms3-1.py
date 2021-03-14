data = input()
arr = []
j = 0
for i in range(len(data)):
    arr.append(int(data[j]))
    j += 1

count_0 = 0
count_1 = 0

if arr[0] == 1:
    count_0 += 1
else:
    count_1 += 1
# 11~14 코드가 없을 시에 0001100을 입력하면 count_0과 count_1의 값이 같아진다.
# 처음에 나오는 문자열에 따라 1을 증가시켜주어야만 올바른 뒤집기 횟수를 구할 수 있다.

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == 1:
            count_0 += 1
        else:
            count_1 += 1
    else:
        continue

print(min(count_0, count_1))