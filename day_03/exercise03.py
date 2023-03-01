"""
 * @Author:Jude
 * @Description:分支结构
 * @Date:2023-02-26
"""

# 练习一：系统进行用户名和密码校验
import getpass  # 不用pip，内置模块
username = input("请输入用户名：")
password = input("请输入密码：")
password = getpass.getpass("请输入密码:")
if username == 'admin' and password == 'admin123':
    print("登录成功")
else:
    print("登录失败")

## 练习二：分段函数的输入
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
x = eval(input("请输入x:"))
if x > 1:
    y = 3 * x - 5
elif x>=-1:
    y = x + 2
else:
    y = 5*x+3
print('y的值为:{0}'.format(y))

# 分支结构的其他写法对比，写法一全部写if，假设x=3
# 即使已经满足了第一个if，还要继续执行后面的语句，造成执行资源的浪费
x = eval(input("请输入x:"))
if x>1:
    y = 3 * x - 5
if -1 <= x <= 1:
    y = x + 2
if x<-1:
    y = 5 * x + 3
print(f'y的值为{y}')

# 分支结构的其他写法对比，写法二第二个else里面写嵌套
# 不符合python写法要尽量扁平的特点，嵌套越多，可读性越差x = eval(input("请输入x:"))
if x>1:
    y = 3 * x - 5
else:
    if x<-1:
        y = 5 * x + 3
    else:   
        y = x + 2
print(f'y的值为{y}')

# 练习3：个人所得税的计算器
income = eval(input("请输入每个月工资收入："))
insurance = eval(input("五险一金扣除额为："))

E = income - insurance
I = E - 3500

if 0 < I < 1500:
    R = 0.03
    D = 0
elif I <= 4500:
    R = 0.1
    D = 105
elif I <= 9000:
    R = 0.2
    D = 555
elif I <= 35000:
    R = 0.25
    D = 1005
elif I <= 55000:
    R = 0.3
    D = 2755
elif I <= 80000:
    R = 0.35
    D = 5505
else:
    R = 0.45
    D = 13505

if I > 0:
    T = I * R - D
else:
    T = 0

print("个人所得税为：{:.2f}".format(T))
print("税后收入为：{:.2f}".format(E-T))

练习1：英制单位英寸与公制单位厘米互换
已知1英寸=2.54厘米
input_number = input("请输入要转换的单位:")
if input_number[-2:] == 'in':
    output_number = eval(input_number[0:-2])*2.54
    print(f"{input_number} = {output_number:.2f}cm")
else:
    output_number = round(eval(input_number[0:-2])/2.54,2)
    print(f'{input_number} = {output_number}in')

练习2：百分制成绩转换为等级制成绩
score = input("请输入百分制成绩：")
if int(score)>=90:
    print("A")
elif int(score)>=80:
    print("B")
elif int(score)>=70:
    print("C")
elif int(score)>=60:
    print("D")
else:
    print("E")

# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。
a,b,c = eval(input("请输入三角形的三条边边长（用逗号隔开）："))
if a+b>c and a+c>b and b+c>a:
    p = (a+b+c)/2
    print(type(p))
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print("这三条边可以构成三角形")
    print("面积为：{:.2f}".format(area))
    print("周长为：{}".format(a+b+c))
else:
    print("这三条边无法构成三角形")
