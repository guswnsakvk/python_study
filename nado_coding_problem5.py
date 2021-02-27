from random import *
내 코드
count = int(0)
for customer in range(50):
    Time = randint(5,50)
    if Time >= 5 and Time <= 15:
        count += 1
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer+1,Time))
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer+1,Time))

print("\n총 탑승 승객 : {0}명".format(count))

# 나도 코딩 코드
cnt = 0
for i in range(1, 51): # 1 ~ 50 이라는 수(승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("\n총 탑승 승객 : {0}명".format(cnt))