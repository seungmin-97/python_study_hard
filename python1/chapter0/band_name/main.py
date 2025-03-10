'''
밴트 네임 생성기 프로그램일 작성하겠습니다.

1. 지금 입은 하의 색깔을 물어보는 input 함수를 작성하고 pants_color라는 변수에 저장합니다.

2. 마지막으로 먹은 음식을 물어보는 input 함수를 작성하고 last_food라는 변수에 저장합니다.

3. f-string을 활용하여 콘솔창에 다음과 같이 출력될 수 있도록 작성합니다.

실행 예
지금 입은 하의 색깔은 무엇입니까? >>> 그레이
마지막으로 먹은 음식은 무엇입니까? >>> 부리또
당신의 밴드 이름은 그레이 부리또입니다.
'''
logo = '''

 ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀█▄▄   ▄▀▀▄ ▀▄  ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄ 
▐ ▄▀   █ ▐ ▄▀ ▀▄ █  █ █ █ █ ▄▀   █ █  █ █ █ ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐ 
  █▄▄▄▀    █▄▄▄█ ▐  █  ▀█ ▐ █    █ ▐  █  ▀█   █▄▄▄█ ▐  █    █   █▄▄▄▄▄  
  █   █   ▄▀   █   █   █    █    █   █   █   ▄▀   █   █    █    █    ▌  
 ▄▀▄▄▄▀  █   ▄▀  ▄▀   █    ▄▀▄▄▄▄▀ ▄▀   █   █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄   
█    ▐   ▐   ▐   █    ▐   █     ▐  █    ▐   ▐   ▐   █    █     █    ▐   
▐                ▐        ▐        ▐                ▐    ▐     ▐        

'''

print(logo)
pants_color = input("자금 입은 하의 색깔은 무엇입니까? >>> ")
last_food = input("마지막으로 먹은 음식은 무엇입니까? >>> ")
band_name = pants_color +" "+ last_food                    # band_name 변수를 선언해서 다시 대입
# print(f"당신의 밴드 이름은 {band_name}입니다")
print(f"당신의 밴드 이름은 {pants_color} {last_food}입니다")