"""
 * @Author:Jude
 * @Description:输出格式化练习
 * @Date:2023-02-14
"""
# 练习1 温度转化 C=(F - 32) / 1.8
F = eval(input("请输入华氏摄氏度:"))
C = (F - 32) / 1.8
#第一种格式化
print("转换后的摄氏度为%0.2f"%(C))
#第二种格式化
print(f"转换后的摄氏度为{C:.2f}")
#第三种格式化
print("转换后的摄氏度为{0:.2f}".format(C))

# 练习2 圆的周长和面积计算
import math
radius = eval(input("请输入圆的半径:"))
perimeter = 2 * math.pi * radius 
area = math.pi * radius ** 2 
print(f"圆的周长为{perimeter:.2f}")
print("圆的面积为{0:.2f}".format(area))


