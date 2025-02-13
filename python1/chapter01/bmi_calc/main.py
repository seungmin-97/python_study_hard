'''
bmi_calc를 만들기 위한 사전 준비
'''
# age = input("당신의 나이는 몇 살입니까? >>> ")
# print(type(age))
# # print(f"당신은 내년에 {age+1}살이 됩니다.") # 오류 발생
'''
input() 함수의 결과값은 언제나 str입니다. -> 즉, 수학 연산을 하기 위해서는 별도의 과정이 필요합니다.

이때 필요한 함수가 '형변환 함수'입니다.(Conversion)
'''
# age1 = input("당신의 나이는 몇 살입니까? >>> ")
# print(type(age1))       # 결과값 : str
# age1_int = int(age1)    # str인 age1를 int로 자료형을 변환시켜서 age1_int라는 새로운 변수에 대입
#
# print(type(age1_int))
# print(f"당신은 내년에 {age1_int+1}살이 됩니다.")   # 여기서는 오류 발생 x

'''
자주 쓰이는 형변환 함수
1. int() -> str 또는 float을 int로 변경       -> 소수의 경우 버림
2. float() -> str 또는 int를 float으로 변경    -> 정수의 경우 .0 붙여줌
3. round() -> 반올림 해주는 함수
'''
# temp = int(3.8)
# print(temp)
# temp2 = float(4)
# print(temp2)
#
# temp3 = round(3.8)
# print(temp3)
#
# temp4 = round(5.312321312, 2)   # 괄호 첫번째 수를 소수점 2째자리까지 표기
# print(temp4)
'''
BMI 계산기를 작성합니다.

1. 키(cm)를 입력 받아(input()를 쓰라는 의미) 변수 height에 저장합니다.
2. 몸무게(kg)을 입력 받아 변수 weight에 저장합니다.
3. 몸무게 / (키(m)의 제곱)을 계산하면 bmi 지수가 나옵니다.
4. bmi 지수를 int로 출력하세요. -> int() 함수 사용하라는 의미
5. bmi 지수를 소수점 셋째자리에서 반올림 하여 둘째 자리까지 출력하세요. -> round()함수 사용

실행 예

로고 출력하세요(구글에서 text to ascii art 검색)
당신의 키는 몇 cm입니까? >>> 173.2
당신의 몸무게는 몇 kg입니까? >>> 70
당신의 bmi 지수는 23입니다.
당신의 bmi 지수는 23.xx입니다.
'''
# 로고 출력
logo = '''

 ▄▀▀█▄▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▀▄   
▐ ▄▀   █ █  █ ▀  █ █   █  █  
  █▄▄▄▀  ▐  █    █ ▐   █  ▐  
  █   █    █    █      █     
 ▄▀▄▄▄▀  ▄▀   ▄▀    ▄▀▀▀▀▀▄  
█    ▐   █    █    █       █ 
▐        ▐    ▐    ▐       ▐ 

'''
print(logo)
# 키 / 몸무게를 입력받고 변수에 저장
# 최대한 중간과정을 많이 표기한 가독성을 중시한 코드
# height = input("당신의 키는 몇 cm입니까? >>> ")
# height = float(height)
# height = height / 100  # cm->m로 단위 변환 / 이미 float으로 바뀌었기 때문에 height로 입력해도 됨
# weight = input("당신의 몸무게는 몇 kg입니까? >>> ")
# weight = float(weight)
# bmi = weight / (height**2) # 몸무게 / 키(m)의 제곱 -> 결과값이 float으로 나옴
# bmi_int = int(bmi)          # 계산 후 결과값을 정수로 표현
# bmi_round = round(bmi, 2)   # 계산 후 결과값을 소수점 셋째자리에서 반올림 한 결과
# print(f"당신의 bmi지수는 {bmi_int}입니다.")
# print(f"당신의 bmi지수는 {bmi_round}입니다.")

# 가장 짧지만 가독성이 별로인 코드
height = float(input("당신의 키는 몇 cm입니까? >>> ")) / 100 # 키 입력받고 바로 m로 변환
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
print(f"당신의 bmi지수는 {round(weight/(height**2), 2)}입니다.")


# 지시사항 3번과 같이 연산을 해야함 -> 연산전에 height를 cm -> m표기로 바꿀 필요가 있음
# print(type(height)) # str으로 나오기 때문에 수학 연산이 불가능 합니다.
# height / weight가 srr이기 때문에 수학 연산이 가능한 자료형으로 형변환을 할 필요가 있음.
# 형 변환 후에 height의 경우에는 cm를 m으로 바꾸기 위한 연산이 필요함 -> height / 100

# 이상의 과정이 끝나고 나서야 (몸무게) / (키(m)의 제곱) 연산이 가능

# 지시사항 4, 5에 해당하는 출력문 작성

# chapter01에 우클릭 -> new -> python package -> tip_calc 패키지 생성
# tip_calc 우클릭 -> new -> python file -> main