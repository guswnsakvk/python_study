#내 코드
def std_weight(height, gender):
    if(gender == "남자"):
        return height * height * 22
    elif(gender == "여자"):
        return height * height * 21


height, gender = input().split()
height = float(height) / 100
result = round(std_weight(height, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, result))

# 나도 코딩 코드

def std_weight(height, gender): # 키는 m단위 (실수), 성별 "남자" / "여자"
    if(gender == "남자"):
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))