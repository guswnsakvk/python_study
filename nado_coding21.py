import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

import theater_module as mv # theater_module를 mv로 부를 수 있다.
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module에 모든 내용 가져오기
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # theater_module에 특정 내용만 가져오기
price(5)
price_morning(6)

from theater_module import price_soldier as price # theater_module에 특정 내용만 가져오는데 별명 만들기
price(5)

# # theater_module
# # 일반 가격
def price(people):
    print("{0}명의 가격은 {1}원 입니다.".format(people, people * 10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명의 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))

# 군인 할인 가격
def price_soldier(people):
    print("{0}명의 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000))