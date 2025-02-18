MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    }
}

profit = 0
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}

logo = '''

          _____                   _______                   _____                    _____          
         /\    \                 /::\    \                 /\    \                  /\    \         
        /::\    \               /::::\    \               /::\    \                /::\    \        
       /::::\    \             /::::::\    \             /::::\    \              /::::\    \       
      /::::::\    \           /::::::::\    \           /::::::\    \            /::::::\    \      
     /:::/\:::\    \         /:::/~~\:::\    \         /:::/\:::\    \          /:::/\:::\    \     
    /:::/  \:::\    \       /:::/    \:::\    \       /:::/__\:::\    \        /:::/__\:::\    \    
   /:::/    \:::\    \     /:::/    / \:::\    \     /::::\   \:::\    \      /::::\   \:::\    \   
  /:::/    / \:::\    \   /:::/____/   \:::\____\   /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/    /   \:::\    \ |:::|    |     |:::|    | /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/____/     \:::\____\|:::|____|     |:::|    |/:::/  \:::\   \:::\____\/:::/__\:::\   \:::\____\
\:::\    \      \::/    / \:::\    \   /:::/    / \::/    \:::\   \::/    /\:::\   \:::\   \::/    /
 \:::\    \      \/____/   \:::\    \ /:::/    /   \/____/ \:::\   \/____/  \:::\   \:::\   \/____/ 
  \:::\    \                \:::\    /:::/    /             \:::\    \       \:::\   \:::\    \     
   \:::\    \                \:::\__/:::/    /               \:::\____\       \:::\   \:::\____\    
    \:::\    \                \::::::::/    /                 \::/    /        \:::\   \::/    /    
     \:::\    \                \::::::/    /                   \/____/          \:::\   \/____/     
      \:::\    \                \::::/    /                                      \:::\    \         
       \:::\____\                \::/____/                                        \:::\____\        
        \::/    /                 ~~                                               \::/    /        
         \/____/                                                                    \/____/         
                                                                                                    
'''
# print(MENU)
# print(MENU["라때"]["재료"]["우유"] + 1)
#
# 카푸치노의 가격을 콘솔에 출력하시오.
# 에스프레소의 물 양을 콘솔에 출력하시오.
# print(MENU["카푸치노"]["가격"])
# print(MENU["에스프레소"]["재료"]["물"])
# resources에서 에스프레소 두 잔을 뽑았을 때, 남는 물, 우유, 커피랑 연산하고,
# 그 결과를 콘솔에 출력하시오.
#
# resources["물"] -= MENU["에스프레소"]["재료"]["물"] * 2
# resources["커피"] -= MENU["에스프레소"]["재료"]["커피"] * 2
#
# 연산
# print(resources)
#
# # 이상을 진행했을 때 커피 두 잔이 자판기에서 나왔기 때문에 자판기에서는 돈이 들어가있겠죠
# # 자판기 profit 변수에 적절한 가격을 대입하시오.
#
# profit += MENU["에스프레소"]["가격"] * 2
#
# print(profit)

# choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
# off 라고 입력되면 종료될 것
# report 라고 입력되면 resources와 profit를 참조하여 manual과 같은
# 방식으로 콘솔에 출력할 것
# 잘못입력했을 경우 잘못 입력하셨습니다 라는 안내문이 출력될 것

# choice가 "라때"라는 str 데이터라면, "라떼"를 만드는데 필요한 재료를 조회하는 방법은
# 무엇일까요?
# print(MENU[choice]["재료"])


# 함수들 정의
def is_resources_enough(order_ingredients):
    """DocString: 함수/클래스/메서드가 어떤 작용을 하는지 '사람들에게' 설명해주는 기능
    주문 받은 음료를 'resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면
    True 반환, 아니면 Flase 반환
    :param: order_ingredients
    :return: True/ False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다.")
            return False
        return True # else 안쓴 이유: if문이 실행 안됐으면 어차피 True라서

def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수 call3()유형"""
    # 쿼터, 다임, 니켈, 페니 네 종류의 동전
    # 쿼터 = 0.25달러
    # 다임 = 0.1달러
    # 니켈 = 0.05달러
    # 페니 = 0.01달러
    # # guarters, dimes, nickels, pennies
    # guarters = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    # dimes = int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    # nickels = int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    # pennies = int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01
    #
    # return guarters + dimes + nickels + pennies
    # 축약 버전 -> 지역 변수가 너무 많아서
    total = 0.0
    total += int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    total += int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01

    return total

# 들어온 동전 금액과 가격을 비교하는 함수를 정의
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받아
     동전이 가격보다 높으면 True / 아니면 False 변환
      그리고 True면 profit에 음료 가격만큼 추가해줘야 함니다."""

    charge = money_received - drink_cost
    if charge >= 0:
        # profit에 돈 추가해야 합니다. drink_cost만큼. profit -> 전역변ㅇ수
        global profit
        profit += drink_cost
        print(f"잔돈 ${charge}를 반환합니다.")
        return True
    else:
        print(f"동전이 충분하지 않습니다. {money_received}원을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함.
    -> 차감은 무조건 이루어집니다. 음료 나오는 안내문구 작성"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"{choice}☕가 나왔습니다. 맛있게 드세요!😊")

is_on = True
print(logo)

while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    # 만약 choice가 off라면 반복문을 종료
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다. ✔")
    elif choice == "report":
        print(f"물: {resources["물"]}ml")
        print(f"우유: {resources["우유"]}ml")
        print(f"커피: {resources["커피"]}g")
        print(f"돈 : ${profit}")
    elif choice in ["에스프레소","라떼","카푸치노"]:# 에스프레소/라떼/카푸치노 중 하나를 입력했을 때 다음 단계로 넘어가는 부분
        print("정상작동합니다.")
        # 자판기에 매뉴명을 정확히 입력했을 때의 처리 과정
        # 1. 자원이 충분한지 확인해서 T / F
        # 2. T 라면 돈을 받아서 계산 -> 해당 금액의 가격보다 높은지 확인해서 T / F 확인
        # 3. T 라면 음료를 만들어주는데, resources dict에 있는 수량을 감소 / 음료 가격만큼 +
        drink = MENU[choice]
        if is_resources_enough(drink["재료"]):
            # 아싱의 조건식이 T라면 2. 단계로 넘어가야 함
            money_received = process_coins()        # 함수호출한 결과값을 변수에 대입
            if is_transaction_successful(money_received, drink["가격"]):
                # 재료 차감하고 음료 만들어서 사용자에게 제공
                # 재료 차감부분을 is_resources_enough()함수를 참조하여 작성하세요.
                # 여기에 작성하시고 추후에 함수화 시킬 예정
                # 기본적으로 dict의 value를 뽑아내서 차감해야합니다.
                # resources["물"] -= drink["재료"]["물"]
                # resources["우유"] -= drink["재료"]["우유"]
                # resources["커피"] -= drink["재료"]["커피"]
                make_coffee(choice, drink["재료"])
    else:
        print(f"잘못 입력하셨습니다. 다시 입력하세요 ❌")

