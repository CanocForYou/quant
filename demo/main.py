# 导入turtle模块，用于绘制图形
import turtle
# 导入random模块，用于生成随机数
import random

# 定义一个函数，用于绘制一朵烟花


def draw_firework():
    # 创建一个Turtle对象，用于绘制图形
    t = turtle.Turtle()
    # 隐藏海龟的形状
    t.hideturtle()
    # 提起画笔，不留下痕迹
    t.penup()
    # 将海龟移动到屏幕底部的随机位置
    t.goto(random.randint(-300, 300), -300)
    # 设置画笔的颜色为随机颜色
    t.pencolor(random.choice(
        ["red", "orange", "yellow", "green", "blue", "purple"]))
    # 设置画笔的宽度为2像素
    t.width(2)
    # 放下画笔，开始绘制
    t.pendown()
    # 让海龟向上移动一段距离（模拟烟花上升）
    t.setheading(90)
    t.forward(random.randint(100, 200))

    # 定义一个变量，表示烟花爆炸后的碎片数量（随机在10到20之间）
    n = random.randint(10, 20)

    # 循环n次，绘制n个碎片（模拟烟花爆炸）
    for i in range(n):
        # 记录当前海龟的位置和方向（用于恢复状态）
        position = t.position()
        heading = t.heading()

        # 让海龟向随机方向移动一段距离（模拟碎片飞散）
        angle = random.randint(0, 360)
        distance = random.randint(30, 60)
        t.setheading(angle)
        t.forward(distance)

        # 恢复海龟的位置和方向（准备绘制下一个碎片）
        t.penup()
        t.goto(position)
        t.setheading(heading)
        t.pendown()

# 定义一个主函数，用于执行程序逻辑


def main():

    # 创建一个Screen对象，用于管理窗口和事件循环
    screen = turtle.Screen()
    # 设置窗口标题为"Fireworks"
    screen.title("Fireworks")
    # 设置窗口背景颜色为黑色（模拟夜空）
    screen.bgcolor("black")

    # 定义一个变量，表示要绘制的烟花数量（随机在5到10之间）
    m = random.randint(5, 10)

    # 循环m次，绘制m朵烟花
    for j in range(m):
        # 调用draw_firework函数，绘制一朵烟花
        draw_firework()

    # 启动事件循环，等待用户关闭窗口或按下ESC键退出程序
    screen.exitonclick()


if __name__ == "__main__":
    main()
