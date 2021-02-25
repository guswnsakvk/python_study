# 내 코드
address = input()
new_password = address.replace("http://", "") # http://를 삭제
num = new_password.find('.') # '.'이 있는 위치 찾기
new_password = new_password[:num] # '.'의 이후에 있는 문자열 삭제
a = len(new_password) # 문자열 개수 구하기
b = new_password.count("e") # e의 개수 구하기
print(new_password[:3] + str(a) + str(b) + "!")

# 나도 코딩 코드
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}".format(url, password))
