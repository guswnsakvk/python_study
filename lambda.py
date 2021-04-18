#lambda 함수
# 익명 함수란 이름이 없는 구현체만 존재하는 간단한 함수를 의미
# 코드 상에서 한번만 사용되는 기능이 이씅ㄹ 때, 굳이 함수로 만들지 않고 1회성으로 만들어서 쓸 때 사용

square = lambda x: x**2
print(square(5))

# lambda를 활용하여 문자열 길이순으로 정열
strings = ['bob', 'charles', 'alexander3', 'teddy']
strings.sort(key= lambda x: len(x))

print(strings)

# filter, map, reduce
# lambda가 유용하게 사용되는 3가지 대표적 함수
# 함수형 프로그래밍의 기본 요소이기도 함
# filter: 특정 조건을 만족하는 요소만 남기고 필터링
# map: 각 우너소를 주어신 수식에 따라 변형하여 새로운 리스트를 반환
# reduce: 차례대로 앞 2개의 원소를 가지고 연산. 연산으 ㅣ결과가 또 다음 연산의 입력으로 진행됨.
#         따라서 마지막까지 진행되면 최종 출력은 한개의 값만 남게 됨

# filter 예시
nums = [1,2,3,6,8,9]
lst = list(filter(lambda x: x % 2==0, nums))
print(lst)

# map 예시
lst1 = list(map(lambda x:x**2, nums ))
print(lst1)

# reduce 예시
import functools

a = [1,3,5,8]
result = functools.reduce(lambda x,y:x+y, a)
print(result)