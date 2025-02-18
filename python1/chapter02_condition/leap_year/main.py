'''
주어진 해가 윤년인지 아닌지 계산하는 프로그램을 작성합니다.
일반적으로 1년은 365일이고, 윤년은 366일로 2월에 하루가 더 있습니다.

다음은 특정연도가 윤년인지 확인하는 방법입니다.
    1. 4로 나누어 떨어지는 해는 윤년입니다.
    2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
    3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.

ex)

    2000 / 4 = 500 이라서 윤년
    2000 / 100 = 20 이라서 윤년 x
    2000 / 400 = 5 이라서,

    최종적으로 2000년은 윤년에 해당합니다.

    2100 / 400 = 525 이라서 윤년
    2100 / 100 = 21 이라서 윤년 x
    2100 / 400 = 5.25 이라서 윤년 x

    최종적으로 2100년은 윤년이 아닙니다.

실행 예

윤년인지 확인하고 싶은 연도를 확인하세요 >>> 2200년
2200년은 윤년이 아닙니다.

윤년인지 확인하고 싶은 연도를 확인하세요 >>> 2000년
2000년은 윤년입니다.
'''
year = int(input("윤년인지 확인하고 싶은 연도를 확인하세요 >>> "))

# 중첩 if문을 사용하지 않았을 경우 -> 조건을 큰 것으로 부터 작은 것으로 배치하여 걸러 낼 수 있게끔 작성할 필요가 있음
# if year % 400 == 0:
#     print("윤년입니다.")
# elif year % 100 == 0:
#     print("윤년이 아닙니다.")
# elif year % 4 == 0:
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")

# 중첩 if문을 사용했을 경우 -> 4로 나누어 떨어지지만 그 내부에서(중첩if문) 윤년인 경우와 아닌 경우를 고려해야겠음
# if year % 4 == 0:
#     if year % 400 == 0:
#         print("윤년이 아닙니다.")
#     elif year % 100 == 0:
#         print("윤년이 아닙니다.")
#     else:
#         print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")


