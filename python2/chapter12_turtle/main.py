import random
# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할겁니다.
from turtle import Turtle, Screen

t = Turtle()            # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()       # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# for _ in range(10):           # 그냥 반복을 10번 하는 거고 변수를 사용하지 않았기 때문에 _를 썼습니다.(1이나 n이 아니라)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# t.left(90)
# t.forward(100)
# for _ in range(3):
#     t.right(90)
#     t.forward(100)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)

# t.left(45)
# t.forward(90)
# t.right(90)
# t.forward(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# dotted_line을 그리는 함수 하나 정의할겁니다.

def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()
#
# # 삼각형도 그려볼까요
# for _ in range(3):
#     dotted_line()#     t.left(120)
#
# # 이상의 함수를 사용하여 사각형을 그린다고 했을 때
# for _ in range(4):
#     dotted_line()
#     t.left(90)
#
# for _ in range(5):
#     dotted_line()
#     t.left(72)

# 1, draw_figures(num)을 정의하시오.
# 2. num 3 미만이면 "도형을 그릴 수 없습니다."가 출력되고 매서드를 종료하시오.
# 3. 3이상이면 해당 매서드가 실행될 수 있도록 하시고,
# 4. 반복문을 통해 draw_figures를 호출해 삼각형부터 십각형까지 그리는데,
# 5. 도형마다 색깔이 다를 수 있도록 작성하시오.


def draw_figures(num):
    if num < 3:
        print("도형을 그릴 수 없습니다.")
        return          # 함수에서 return 다음 아무것도 입력하지 않으면 종료
    for _ in range(num):
        dotted_line()
        t.left(360 / num)





# for _ in range(10):
#     draw_figures(3)
# 랜덤 객체 생성
random = random.Random()

colors = ["navy","dark gray","light slate gray","slate gray","royal blue","medium blue","dark blue"]
# 내부에 거북이 색깔들을 요소로 하는 리스트를 완성 랜덤 모듈을 사용해서요(행맨에서 했습니다.)

# t.color("medium sea green")


# draw_figures(3)
# draw_figures(4)
# draw_figures(1)

# for i in range(11):
#     draw_figures(i)



# for i in range(3, 11, 1):
#     draw_figures(i)
#     t.color(random.choice(colors))
'''
    .heading()매서드:
        거북이가 바라보는 방향을 나타내는 속성으로 도(degree) 단위로 나타남.
        
        해당 매서드는 콘솔창에 float 형태로 출력됩니다.
        0도 : 동
        90도 : 북
        180도 : 서
        270도 : 남
        
    .setheading() 매서드:
        특정 각도로 거북이를 회전시키는 매서드
    .circle() 매서드 :
        거북이가 원 그리는 매서드
'''
# t.forward(100)
# print(t.heading())
# t.right(90)
# print(t.heading())

# for _ in range(10):
t.circle(100)
t.color(random.choice(colors))
t.setheading(10)
t.circle(100)

# for _ in range(360 // 10):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading() + 10)

# 이상의 네 줄의 코드를 응용하여 draw_spriograph(size_of_gap)로 함수화 하시오.

def draw_spriograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.circle(100)
        t.color(random.choice(colors))
        t.setheading(t.heading() + size_of_gap)

t.speed(0)
draw_spriograph(2)



screen.exitonclick()