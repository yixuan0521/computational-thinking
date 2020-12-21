# 啟動模組
import turtle #導入海龜模組
shelly = turtle.Turtle() # 把模組中的螢幕游標叫出來
shelly.shape("turtle") # 將三角形改為烏龜
shelly.position() # 烏龜的位置
#海龜的外觀
## 海龜的顏色
shelly.color("blue", "blue") # 內紅邊綠
## 海龜畫線的顏色
shelly.pencolor("black") # 黑色
## 調整海龜尺寸
shelly.turtlesize(10,10,2) # (上下長度,左右寬度,外框粗細)變大
shelly.resizemode("auto") # auto表預設值,還原海龜大小
shelly.turtlesize(5,5,3) # 調整成自己喜歡的大小
# 海龜運動命令
## 畫一條線長100
shelly.forward(100)
## 向左轉90度
shelly.left(90)
## 提起筆離開畫布
shelly.penup()
## 放下筆貼近畫布
shelly.pendown()
## 隱藏使用的turtle
shelly.hideturtle()
#畫筆控制
## 要填滿繪製的圖案-開始
shelly.begin_fill()
## 用什麼顏色
shelly.fillcolor("gray")
## 繪製圖形
shelly.circle(200) #半徑250的圓
shelly.circle(200, 90, 30) #半徑50,範圍180度,轉動方向30度
## 要填滿繪製的圖案-停止
shelly.end_fill()
## 蓋章
shelly.stamp()
## 在螢幕寫字
shelly.write("Turtle Rock")