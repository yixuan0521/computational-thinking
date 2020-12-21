# 方法(一):for 迴圈
import turtle
shelly = turtle.Turtle()

for i in range(4): # 畫正方形 - 1 + 2 做四次 [0,1,2,3]
    shelly.forward(250) # 1.畫直線
    shelly.left(90) # 2.轉向
    print (i) # 計數,一共四次
# 方法(二):for 迴圈 + 色彩(紅色)
import turtle
shelly = turtle.Turtle()
shelly.color("red") # 顏色 - 線用紅色

for i in range(4): # 形狀 - 正方形
    shelly.forward(250)
    shelly.left(90)