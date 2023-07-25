
import turtle
import time
import random
#=============== 
wn = turtle.Screen() #tạo cửa sổ
wn.bgcolor('#49F634') #tạO MÀU cho backgroud
wn.setup (width=600, height=600) #kích thứơc màu cửa sổ
wn.tracer(0) 



# 3 scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("#FF55BB")
sc.penup()
sc.hideturtle()
sc.goto(0,0)
sc.write("score: 0  Hige score:o", align ="center", font=("ds-digital", 24, "normal" ))
score = 0
high_score = 0
 #=============== 
#2 Mainloop
while True:
    wn.update()
    move()
    time.sleep(0.1)
wn.mainloop
# 4 snake head
head = turtle. Turtle()
head.speed(0)
head.shape("circle")
head.penup()
head.goto(0,0)
head.dicrection ="stop"
#di chuyển code

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


