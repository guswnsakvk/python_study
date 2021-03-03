try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # int형으로 받아야 하는데 다른 형태로 입력받으면 valuserror 발생
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 나누는 수는 0이 될 수 없으니 나누는 수가 0일 경우 에러 발생
    print(err)
except Exception as err: # ValueError 또는 ZeroDivisionError가 아닌 경우 모든 에러를 처리하는 것
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) # 어떤 에러가 발생했는지 알려줌