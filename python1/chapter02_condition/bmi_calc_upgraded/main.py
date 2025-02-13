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
height = float(input("당신의 키는 몇 cm입니까? >>> ")) / 100 # 키 입력받고 바로 m로 변환
weight = float(input("당신의 몸무게는 몇 kg입니까? >>> "))
bmi = round(weight/(height**2), 2)      # 반복적으로 나오게 되는 연산의 경우에는 간단한 변수명에 대입하는 것이
if bmi < 18:                            # 가독성 높은 코드를 작성하는 방식에 해당함.
    print(f"당신의 bmi지수는 {bmi}이고, 저체중입니다.")
elif bmi < 23.5:
    print(f"당신의 bmi지수는 {bmi}이고, 정상 체중입니다.")
elif bmi < 25:
    print(f"당신의 bmi지수는 {bmi}이고, 과체중입니다.")
else:
    print(f"당신의 bmi지수는 {bmi}이고, 비만입니다.")
# print(f"당신의 bmi지수는 {int(weight/(height**2))}입니다.")
# print(f"당신의 bmi지수는 {round(weight/(height**2), 2)}입니다.")

'''
업그레이드 관련 지시 사항

1. chrome에서 사이트를 확인하신 후 bmi가 특정 구간일 때마다
    당신의 bmi지수는 xx.xx이고, 저체중/정상/과체중/비만입니다. 가 출력될 수 있도록
    조건문을 작성하여 반영하시오.
'''

