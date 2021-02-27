from random import *

# 내 코드
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print("-- 당첨자 발표 --")
print("치킨 당첨자 :", lst[0])
lst.remove(lst[0])
print("커피 당첨자 :",sample(lst,3))
print("-- 출하합니다 --")

# 나도 코딩 코드
users = range(1, 21) # 1부터 20까지 숫자를 생성, type은 range
users = list(users) # list로 타입변경
shuffle(users)

winners = sample(users, 4) # 4명중 한명은 치킨 나머지는 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 출하합니다 --")