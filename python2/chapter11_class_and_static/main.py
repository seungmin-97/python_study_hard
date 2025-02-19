'''
1. 클래스 변수

    인스턴스 변수: 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수: 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
    목적 - 인스턴스마다 서로 다른 값을 지정
    접근 방식 - 인스턴스 접근(o)
            - 클래스 접근(x)

    클래스 변수 :
    목적 - 인스턴스가 공유하는 값을 지정
    접근 방식 - 인스턴스 접근(o)
            - 클래스 접근(o)
'''

# # 클래스 변수 예제
# class Korean:
#     country = "한국"
#     # 인스턴스 변수의 경우 생성자 내부에 있었습니다. 클래스 변수와 경우에는 이상처럼
#     # 클래스 내부에 그냥 선언하고 초기화하면 됩니다.
#
#     def __init__(self, name, age, address):
#         self.name = name                # 인스턴스 변수 1
#         self.age = age                  # 인스턴스 변수 2
#         self.address = address          # 인스턴스 변수 3
#
# # 객체 생성
# man = Korean(name="박승민", age=18, address="부산광역시 영도구")       # keyword argument
# print(man.name)         # 객체의 속성 확인 방법
# print(man.age)          # 객체의 속성 확인 방법
# print(man.address)      # 객체의 속성 확인 방법 -> 셋 다 인스턴스 변수 확인
#
# # 클래스 변수 확인 방법
# print(man.country)          # 객체명.클래스변수명을 통한 접근 : 가능
# print(Korean.country)       # 클래스명.클래스변수명을 통한 접근 : 가능

# 객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하긴 하지만 클래스 내부의 코드를
# 들여다보기 전까지는 country라는 변수가 클래스 변수인지 인스턴스 변수인지 확인이
# 불가능하다는 문제가 있습니다.

# 이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명으로 참조하기 보다는
# 클래스명.클래스변수명을 통해서 참조하는 것이 바람직합니다.

'''
클래스 매서드 : 클래스 변수를 사용하는 매서드
'''
class Korean2:
    country = "대한민국"            # 클래스 변수 선언 및 초기화

    # 클래스 매서드 정의 법
    @classmethod                                # 예를 명시하면 밑의 코드가 클래스 매서드로 작성됨
    def trip(cls, travelling_site):             # 그 결과 첫 번째 매개변수로 self가 아니라 cls가 자동완성
        if cls.country == travelling_site:
            print("국내 여행입니다.")
        else:
            print("해외 여행입니다.")


# 클래스 매서드의 호출
Korean2.trip("대한민국")
Korean2.trip("미국")