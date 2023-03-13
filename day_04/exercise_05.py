"""
 * @Author:Jude
 * @Description:循环结构练习-2
 * @Date:2023-03-11
"""
# 练习一：找出100—999之间的水仙花数
# 水仙花数：（各个数字的立方和刚好等于这个数本身）
# 比如：153=1的立方+5的立方+3的立方
for i in range(100,1000):
    first = i//100
    second = i % 100 // 10
    third = i % 10
    if i == first**3 + second**3 + third**3:
        print(i)

# 练习二：把某个数字的每个位上的数字进行取倒
# 例如：1234-->4321
# 例如：557432-->234755

input_number = eval(input("请输入一个数："))
total = 0 
quotient = input_number
while quotient > 0 :
    remainder = quotient % 10 ## 1234%10 =4
    quotient = quotient // 10 ## 1234//10=123
    total = total * 10 + remainder  ## 0*10+4=4
print(total)

# 方法二
input_number = input("请输入一个数字：")
reverse_string = input_number[::-1]
print(reverse_string)

# # 练习3 输入两个非负整数m和n(m>=n)，计算C(m,n)的值，组合数
m = int(input("请输入一个非负整数m："))
n = int(input("请输入一个非负整数n："))

def factorial(x):
    total = 1
    for i in range(1,x+1):
        total =  total * i       
    return total
result = factorial(m)//factorial(m-n)//factorial(n)
print(result)

# 方法二 导入数学模块
import math
m = int(input("请输入一个非负整数m："))
n = int(input("请输入一个非负整数n："))
result = math.factorial(m)//math.factorial(m-n)//math.factorial(n)
print(result)

# 练习4：输入一个正整数，判断它是不是质数（只能被1和自身整除的数）
integer = eval(input("请输入一个正整数："))
if integer == 1:
    print("这个正整数不是质数")
elif integer == 2:
    print("这个正整数是质数")
else:
    for i in range(2,integer):
        if integer % i != 0:
            if i == integer-1:
                print("这个正整数是质数")    
        else:
            print("这个正整数不是质数")
            break
    
# 练习4：输入一个正整数，判断它是不是质数（只能被1和自身整除的数）
# 思路：先假设这个数就是质数，用一个布尔值进行标识，如果布尔值为真就是质数，布尔值为假就不是质数
number = int(input("请输入一个正整数："))
is_prime = True 
for i in range(2,number):
    if number % i == 0 :
        is_prime = False 
        break 
if is_prime and number!=1:
    print("这个正整数是质数")
else:
    print("这个正整数不是质数")

# 练习5：请输出1—100范围内的质数
# 嵌套的循环
for i in range(1,101):
    is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime = False 
            break
    if is_prime == True and i != 1:
        print(i,end=' ')


# 练习6：请按照以下规律输出数字
# 1
# 22
# 333
# 4444
line = eval(input("请输入塔的行数："))
for i in range(1,line+1):
    print(str(i)*i)

# 练习7：请按照以下规律输出数字
# 1111
# 2222
# 3333
# 4444
line = eval(input("请输入塔的行数："))
for i in range(1,line+1):
    print(str(i)*line)
# 练习7：请按照以下规律输出数字
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
line = eval(input("请输入塔的行数："))
for i in range(1,line+1):
    for j in range(1,line+1):
        print(i,end=' ')
    print()

# 练习6：请按照以下规律输出数字
# 1
# 2 2
# 3 3 3
# 4 4 4 4
line = eval(input("请输入塔的行数："))
for i in range(1,line+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# 练习6：打印出九九乘法口诀表
# 1*1=1
# 2*1=2 2*2=4
# 3*1=3 3*2=6 3*3=9
# 4*1=4 4*2=8 4*3=12 4*4=16
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end='\t') #使用\t可以使得两位数和一位数上下对齐
    print()

# 练习7：输入三角形三条边的长度，如果能构成三角形就计算周长和面积
# 如果不能构成三角形，提示用户重新输入，直到正确
flag = True
while flag:
    a = eval(input("a="))
    b = eval(input("b="))
    c = eval(input("c="))
    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        p = perimeter / 2 
        area = (p * (p-a) * (p-b) * (p-c)) ** 0.5
        print(f"三角形的周长是{perimeter:.2f}")
        print(f"三角形的面积是{area:.2f}")
        break
    else:
        print("三条边无法构成三角形，请重新输入！")

# 练习8：找出1——10000之间的完美数（除自身之外所有因子的和等于这个数）
# 28 = 1 + 2 + 4 + 7 + 14 
# 但是下面的写法效率非常低，可以用time模块来计算一下程序运行的时间
# 优化写法是，一个数的因子如果开根的前一部分
import time 
start_time = time.time()
for i in range(1,10001):
    total = 0
    for j in range(1,int(i**0.5)+1):
        if i % j == 0:
            total = total + j 
            if i != i//j:                
                total = total + i//j      #例如49=7*7，那么就相当于加了两次7
    if total == i:
        print(i)
end_time = time.time()
total_time = end_time - start_time 
print("执行时间为{:.3f}秒".format(total_time))

# 练习9：下面我们通过一个猜数字的小游戏来看看如何使用while循环。
# 猜数字游戏的规则是：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，
# 计算机给出对应的提示信息（大一点、小一点或猜对了），
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
import random 
number = random.randint(1,100)
total = 0
while True:
    user_number = input("请猜一个1—100以内的正整数：")
    if number == eval(user_number):
        total += 1 
        print("猜对了")
        print(f"一共猜了{total}次")
        break 
    elif number > eval(user_number):
        total += 1
        print("比正确答案小")
    else:
        total += 1
        print("比正确答案大")
if total > 7:
   print('你的智商余额明显不足')
# 输入两个正整数，计算它们的最大公约数和最小公倍数。
# 最大公约数用欧几里得算法
user_number_1 = eval(input("请输入第一个正整数:"))
user_number_2 = eval(input("请输入第二个正整数:"))
number_1 = user_number_1
number_2 = user_number_2
while number_1 % number_2 != 0:
    number_1,number_2 = number_2,number_1 % number_2
max_gongyue = number_2 
min_gongbei = (user_number_1//max_gongyue)*(user_number_2//max_gongyue)*max_gongyue
print(f"最大公约数是{max_gongyue}")
print(f"最小公倍数是{min_gongbei}")

# 如果不用欧几里得算法
number_1 = eval(input("请输入第一个正整数:"))
number_2 = eval(input("请输入第二个正整数:"))
number = min(number_1,number_2)
for i in range(number,1,-1):
    if number_1 % i == 0 and number_2 % i == 0:
        max_gongyue = i 
        break 
min_gongbei = (number_1//max_gongyue)*(number_2//max_gongyue)*max_gongyue
print(f"最大公约数是{max_gongyue}")
print(f"最小公倍数是{min_gongbei}")

# 打印如下所示的三角形图案。
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end='')
    print("*"*i)
#     *
#    ***
#   *****
#  *******
# *********
line = eval(input("请输入三角形图案的行数："))
for i in range(1,line+1):
    for j in range(1,line+1-i):
        print(" ",end='')
    print("*"*(2*i-1))

# 练习10：输入一个n，输出n个菲波拉契数
# 1 1 2 3 5 8 13 21 34 55...
n = int(input("请输入一个n："))
x1 = 1
x2 = 1
i = 3
if n == 1 :
    print(x1)
elif n == 2:
    print(x1,end=' ')
    print(x2,end=' ')
else:
    print(x1,end=' ')
    print(x2,end=' ')
    while i <= n:        
        x1,x2 = x2,x1+x2
        print(x2,end=' ') 
        i += 1

# 练习11：百钱百鸡问题
# 公鸡5块钱一只，母鸡3块钱一只，小鸡一块钱买三只，有100块钱要买100只鸡
# 问买公鸡多少只，母鸡多少只，小鸡多少只？
# 穷举法：穷尽所有的可能性，然后设置条件，直到找到问题的解 ---->暴力破解法
cock = 0
hen = 0 
chicken = 0
sum_price = cock * 5 + hen * 3 + chicken * 1/3
total_number = cock + hen + chicken
for cock in range(0,21):
    for hen in range(0,34):
        for chicken in range(0,100,3):
            sum_price = cock * 5 + hen * 3 + chicken * 1/3
            total_number = cock + hen + chicken
            if sum_price == 100 and total_number == 100:
                print(cock,hen,chicken)

# 减少循环的次数，如果已知了x和y,z就已经确定了，就不需要再进行循环
cock = 0
hen = 0 
chicken = 0
sum_price = cock * 5 + hen * 3 + chicken * 1/3
total_number = cock + hen + chicken
for cock in range(0,21):
    for hen in range(0,34):
        chicken = 100 - cock - hen 
        sum_price = cock * 5 + hen * 3 + chicken * 1/3
        total_number = cock + hen + chicken
        if chicken % 3 == 0 and sum_price == 100:
            print(cock,hen,chicken)
# 练习12：分鱼问题
# 五个人（ABCDE）晚上去捕鱼，捕了不计其数的鱼，然后累了去睡觉
# 第二天，A第一个醒过来，把鱼分成了5份，扔掉了多余的1条，然后拿走自己的1份；
# B第二个醒过来，以为鱼没有分过，把剩下的鱼分成了5份，扔掉了多余的1条，拿走自己的1份；
# C,D,E依次醒过来，都按照同样的方法来分鱼，问他们最少捕了多少条鱼？
fish = 1 

while True:
    is_enough = True
    first = fish - 1
    second = first / 5 * 4 - 1
    third = second / 5 * 4 - 1
    fourth = third / 5 * 4 - 1
    fifth = fourth / 5 * 4 - 1

    if fifth < 0 or first % 5 != 0 or second % 5 != 0 or third % 5 != 0 \
        or fourth % 5 != 0 or fifth % 5 != 0:
        is_enough = False

    if is_enough:
        print(fish)
        break 
    else:
        fish += 1

fish = 1 

while True:
    is_enough = True
    
    total = fish 
    for _ in range(5):
        if total-1 > 0 and (total - 1) % 5 == 0:
            total = (total-1) // 5 * 4
        else:
            is_enough = False
            break 

    if is_enough:
        print(fish)
        break 
    else:
        fish += 1
