from random import choice

MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라때": {
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
# # print(MENU)
# # print(MENU["라때"]["재료"]["우유"] + 1)
#
# # 카푸치노의 가격을 콘솔에 출력하시오.
# # 에스프레소의 물 양을 콘솔에 출력하시오.
# # print(MENU["카푸치노"]["가격"])
# # print(MENU["에스프레소"]["재료"]["물"])
# # resources에서 에스프레소 두 잔을 뽑았을 때, 남는 물, 우유, 커피랑 연산하고,
# # 그 결과를 콘솔에 출력하시오.
#
# # resources["물"] -= MENU["에스프레소"]["재료"]["물"] * 2
# # resources["커피"] -= MENU["에스프레소"]["재료"]["커피"] * 2
#
# # 연산
# # print(resources)
#
# # 이상을 진행했을 때 커피 두 잔이 자판기에서 나왔기 때문에 자판기에서는 돈이 들어가있겠죠
# # 자판기 profit 변수에 적절한 가격을 대입하시오.
#
# profit += MENU["에스프레소"]["가격"] * 2
#
# print(profit)

choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노")
# off 라고 입력되면 종료될 것
# report 라고 입력되면 resources와 profit를 참조하여 manual과 같은
# 방식으로 콘솔에 출력할 것
# 잘못입력했을 경우 잘못 입력하셨습니다 라는 안내문이 출력될 것