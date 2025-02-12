'''
while 반복문
    while 다음에 나오는 조건문이 참이라면 이하의 실행문이 반복 실행됨(조건문이 Flase가 될때까지.)

형식 :
whlie 조건문:
    실행문
'''
# 무한 루프의 개념
# num1 = 1
# while num1 > 0:
#     print(num1)

'''
그래서 whlie 반복문을 작성할 때 고려할 점 :
    특정한 상황에서 조건식이 False가 될 수 있도록 사전에 미리 지정해줘야 함.
    -> 아닐 경우 무한 루프에 빠지게 될 수 있음
'''
# 특정 조건에서 반복문이 종료될 수 있도록 하는 예시
# num2 = 1
# while num2 < 11:
#     print(num2)
#     num2 += 1           # 특정 조건에서 조건문이 False가 될 수 있도록 하는 부분
#
# print(f"최종 num2 = {num2}")
'''
if문과의 비교
    if문의 경우 조건식이 참일 때 실행문이 한 번 실행되지만,
    whlie문의 경우 조건식이 참일 때 실행문이 '반복' 실행되기 때문에
    특정 조건이 맞을 경우와 아닐 경우에 대한 고민이 필요한 편
    
기본 예제
10부터 1까지의 모든 정수를 출력하는 whlie문을 작성하시오.

실행 예
10
9
8
7
...
1
'''
# my write:
# num3 = 11
# while num3 < 1:
#     print(num3)
#     num3 += 11

# num3 = 10
# while num3 > 0:
#     print(num3)
#     num3 -= 1

# num3 = 11
# while num3 > 1:
#     num3 -= 1
#     print(num3)

'''
중첩 whlie문(Nested whlie-loop) : while문 내부에 whlie문이 나타나는 것

ex)
총 5일 동안 매일 3시간씩 수업을 진행합니다. 매일 '1일차 1교시입니다.'와 같은 메시지를 출력합니다.
1일차부터 5이차까지 반복되는 일수와 1교시부터 3교시까지 반복되는 시간이라는 2개의 반복 처리 대상을 기준으로
중첩 while문을 작성합니다.

실행 예

1일차 1교시입니다.
1일차 2교시입니다.
1일차 3교시입니다.
2일차 1교시입니다.
2일차 2교시입니다.
2일차 3교시입니다.
...
5일차 3교시입니다.
'''
# day = 1
# while day < 6:              # 5일차까지만 출력되야 하니까.
#     hour = 1
#     while hour < 4:         # 3일차까지만 출력되야 하니까.
#         print(f"{day}일차 {hour}교시입니다.")
#         hour += 1
#     day += 1                # 이 부분에서 실수가 자주 일어납니다.
'''
기본 예제

구구단 2단부터 9단까지 출력하는 프로그램을 작성하시오.(whlie문으로 사용할 것)
변수명은 dan / number
실행 예
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
9 x 8 = 72
9 x 9 = 81
'''
# dan = 2
# while dan:                # 값이 있으면 True로 취급함
#     number = 1
#     while number:
# while 1:

# dan = 2
# while dan < 10:
#     number = 1
#     while number < 10:
#         print(f"{dan} x {number} = {dan*number}")
#         number += 1
#     dan += 1

'''
응용 예제

1부터 100 사이의 모든 정수를 한 줄에 10개씩 출력하는 프로그램을 작성하세요.

실행 예시
1   2   3   3   4   5   6   7   8   9   10
11  12  13  13  14  15  16  17  18  19  20
21  22  23  23  24  25  26  27  28  29  30
31  32  33  33  34  35  36  37  38  39  40
41  42  43  43  44  45  46  47  48  49  50
51  52  53  53  54  55  56  57  58  59  60
61  62  63  63  64  65  66  67  68  69  70
71  72  73  73  74  75  76  77  78  79  80
81  82  83  83  84  85  86  87  88  89  90
91  92  93  93  94  95  96  97  98  99  100
'''
# print("얘가 기본적으로 자동 개행이 일어납니다", end=" ")
# print("얘가 기본적으로 자동 개행이 일어납니다")
# print("얘가 기본적으로 자동 개행이 일어납니다")
# 1부터 10까지는 공백으로 마무리짓도록 print()함수를 작성
# 10으로 나누어 떨어질 때마다 자동 개행이 일어나야 하므로(if조건문)
# 비어있는 print() 함수를 사용하면 작성 가능
# n = 1
# while n < 101:
#     print(f"{n} {n+1}  {n+2}  {n+3}  {n+3}  {n+4}  {n+5}  {n+6}  {n+7}  {n+8}  {n+9}")
#     n += 10

# 이상의 코드의 경우에는 반복을 10번 돌리는 경우였습니다.
# 모든 편견을 가지고 코드를 억지로 작성하게 되면 즉, 반복을 100번 돌리게 됐을 경우에 사용 가능한 방식
n2 = 1
while n2 < 101:
    print(n2,end=" ")
    if n2 % 10 == 0:
        print()
    n2 += 1
