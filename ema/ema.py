# 指数移动平均算法

import matplotlib.pyplot as plt
import random

# 从头开始进行指数移动平均
def exponential_moving_average(input: list, N: int):
    emaList = list()
    dayList = list()

    if len(input) < N:
        return list()
    
    # 设置起始默认值
    s0 = cal_ma(input[:N])
    emaList.append(s0)
    dayList.append(N)

    next = N
    lastEma = s0
    alpha = cal_alpha(N)
    while next < len(input):
        ema = cal_ema(lastEma, input[next], alpha)
        emaList.append(ema)
        dayList.append(next)
        next+=1
        lastEma = ema

    return dayList, emaList


def moving_average(input: list, N: int):
    maList = list()
    dayList = list()

    if len(input) < N:
        return list()
    
    s0 = cal_ma(input[:N])
    maList.append(s0)
    dayList.append(N)

    head = 0
    next = N
    lastMa = s0

    while next < len(input):
        ma = lastMa-input[head]/N+input[next]/N
        maList.append(ma)
        dayList.append(next)
        head+=1
        next+=1
        lastMa = ma
    
    return dayList, maList


def cal_alpha(N: int) -> float:
    return 2/(N+1)


# 计算指数移动平均值
def cal_ema(lastEma: float, thisItem: int, alpha: float) -> float:
    return alpha*thisItem + (1-alpha)*lastEma


# 计算简单移动平均
def cal_ma(input: list) -> float:
    sum = 0
    for item in input:
        sum+=item
    return sum/len(input)


def gen_test_input() -> list:
    testInput = list()
    for i in range(1, 100):
        testInput.append(random.randint(0, 10))
    return testInput


if __name__ == '__main__':
    testInput = gen_test_input()
    x, y = exponential_moving_average(testInput, 7)
    plt.plot(x, y, color='#000000')
    x, y = moving_average(testInput, 7)
    plt.plot(x, y)
    plt.show()
