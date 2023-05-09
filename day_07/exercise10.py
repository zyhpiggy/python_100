"""
 * @Author:Jude
 * @Description:函数的概念和应用场景
 * @Date:2023-05-07
"""
# 函数是相对独立且会被重复使用的功能（代码）
# 将来想使用这些功能的时候，不需要再复制粘贴，而是直接通过调用函数来做到
# 练习一：CRAPS赌博游戏--->色子游戏
# import random 

# def roll_dice(n):
"""##快捷键：ctrl + win + t
    摇色子功能
    param num: 色子的数量（对自变量进行说明）
    return : 摇出的点数（对因变量进行说明）
"""
#     point = 0
#     for _ in range(n):
#         face = random.randint(1,6)
#         point += face
#     return point 


# def result_money(user,money,zhuma):
#     print("{}胜".format(user))
#     if user == '玩家': 
#         money += zhuma   
#     else:
#         money -= zhuma 
#     print("玩家还剩{}元".format(money))
#     return money 

# def win():
#     print("玩家胜")
#     global money 
#     money += zhuma 
#     print("玩家还剩{}元".format(money))
#     return money

# def lose():
#     print("庄家胜")
#     global money 
#     money -= zhuma 
#     print("玩家还剩{}元".format(money))
#     return money 
    

# money = 1000 
# zhuma = 0
# while money > 0 :
#     zhuma = eval(input("请下注："))
#     while zhuma > money or zhuma <= 0 :
#         try:
#             zhuma = eval(input("请下注："))
#         except NameError:
#             pass 
#     first_point = roll_dice(2)
#     print("玩家摇出了{}点".format(first_point))
#     if first_point in (7,11):
#         # print("玩家胜")
#         # money += zhuma 
#         # print("玩家还剩{}元".format(money))
#         # result_money("玩家",money,zhuma)
#         win()
#     elif first_point in (2,3,12):
#         # print("庄家胜")
#         # money -= zhuma 
#         # print("玩家还剩{}元".format(money))
#         # result_money("庄家",money,zhuma)
#         lose()
#     else:
#         while True:
#             curr_point = roll_dice(2)
#             print("玩家摇出了{}点".format(curr_point))
#             if curr_point == first_point:
#                 result_money("玩家",money,zhuma)
#                 break
#             elif curr_point == 7:
#                 result_money("庄家",money,zhuma)
#                 break 
# print("玩家破产，游戏结束")

# 找到重复代码，进行函数封装
# def roll_dice():
#     face1 = random.randint(1,6)
#     face2 = random.randint(1,6)
#     point = face1 + face2 
#     return point 

# 进一步思考如果要把代码写得更通用，更灵活怎么办呢
# 比如roll_dice这个功能，想摇3个色子呢？那就可以加入自变量

# 关于局部变量和全局变量
# python程序中搜索一个变量是安装LEGB顺序进行搜索的
# L是local（局部作用域）,
# 如果局部没有就找embbed（嵌套作用域）
# 没有就找global，再没有就Built-in (内置作用域)
# global---->声明使用全局变量或者将一个局部变量放到全局作用域
# nonlocal---->声明使用嵌套作用域的变量（不使用局部变量）
# x = 100  # 全局变量
# def foo():
#    # x = 200   # 局部变量
#     print(x)
    
# foo()
# print(x)

# 局部里面还可以嵌套定义函数        
# x = 100
# def foo():
#     # x = 200 
    
#     def bar():
#         # x = 300
#         print(x)
#     bar()
#     print(x)
# foo()
# print(x)
# 先调用foo()
# 然后调用bar() print出300
# 然后print(x)  print出200

# 练习2：双色球随机选号
# 红色球01-33，选择不重复的6个球，按从小到大排列
# 蓝色球01-16，选择一个球，跟在红色球后面

# import random 
# def generate(redball_max=34,redball_num=6,blueball_max=17,blueball_num=1):
#     '''
#     description: 生成一组号码
#     return: 保存一组彩票号码的列表
#     如果把这个函数修改得更加通用,既可以玩大乐透也可以玩双色球应该怎么做呢？
#     generate传入四个参数：redball_max,redball_num,
#     '''    
#     red_balls = [i for i in range(1,redball_max)]
#     blue_balls = [i for i in range(1,blueball_max)]
#     selected_balls = random.sample(red_balls,redball_num)
#     selected_balls.sort()
#     selected_balls.append(random.sample(blue_balls,blueball_num))
#     return selected_balls

# def display(selected_balls):
#     '''
#     description: 显示一组彩票号码
#     param: 彩票号码的球的列表
#     '''    
#     for ball in selected_balls:
#         print("{}".format(ball),end=' ')

# n = int(input("机选几注："))
# for _ in range(n):  
#     selected_balls = generate()
#     display(selected_balls)
#     print()

# # 使用函数重构改写双色球随机选号的问题
# def generate(ball_max,ball_num):
#     balls = [i for i in range(1,ball_max)]
#     selected_balls = random.sample(balls,ball_num)
#     selected_balls.sort()
#     return selected_balls 

# def make_big_lottery():
#     """生成大乐透的号码"""
#     return generate(35,5) + generate(12,2)

# def make_two_colors():
#     """生成双色球的号码"""
#     return generate(33,6) + generate(16,1)


# 函数的作业讲评 
# 写一个实现生成指定长度的随机验证码（有数字和英文构成）的函数

# import random 
# import string 

# def generate_code(lenth):
#     '''
#     description: 生成特定长度的随机验证码
#     param: 特定长度
#     return: 随机验证码的列表
#     '''    
#     # number_list = [i for i in range(10)]
#     # big_list = [chr(i) for i in range(65,91)]
#     # small_list = [chr(i) for i in range(97,123)]
#     whole_list =  string.digits + string.ascii_letters
#     return random.choices(whole_list,k=lenth)
# def display(list):
#     for element in list:
#         print(element,end='')

# lenth = int(input())
# display(generate_code(lenth))

# 作业2：写一个函数判断一个正整数是不是质数
# def is_prime(number):
#     '''
#     description: 判断一个正整数是否为质数
#     param num:正整数
#     return 真或假
#     '''    

#     for i in range(2,int(number**0.5)+1):
#         # is_prime = True
#         if number % i == 0:
#             # is_prime = False 
#             # break 
#             return False   # 函数已经执行完毕，不要再循环了
#     return number != 1 
# for i in range(100):
#     if is_prime(i):
#         print(i,end=' ')

# 作业3：用函数实现求两个数的最大公约数和最小公倍数
# 设计函数最为重要的原则：单一职责原则（一个函数只做好一件事）—高度内聚
# 写程序的终极原则：高内聚(high cohesion)，低耦合(low coupling)
# 所以最好设计两个函数
# def gongyue_gongbei(a,b):
#     origin_a = a
#     origin_b = b
#     if a<b:
#         a,b = b,a 
#     while a%b != 0 :
#         a,b = b,a%b 
#     gongyue = b 
#     gongbei = origin_a * origin_b//gongyue
#     return gongyue,gongbei 
# print(gongyue_gongbei(15,18))

# def gcd(x:int,y:int)->int:
#     '''
#     description: 求最大公约数
#     '''    
#     while x % y != 0 :
#         x , y = y , x % y 
#     return y 

# def lcm(x,y):
#     gongyue = gcd(x,y)
#     return x * y // gongyue

# # 作业4：设计获得样本数据描述性统计信息的函数
# # 一类是看集中趋势：众数、均值、中位数
# # 还有一类是看离散趋势：极差、方差和标准差

# def mean(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i 
#     return sum//len(numbers)
# def common(numbers):
#     pass
# def jicha(numbers):
#     '''
#     description: 计算极差
#     '''    
#     result = max(numbers) - min(numbers)
#     return result 

# def variance(numbers):
#     '''
#     description: 求方差
#     '''  
#     x_bar = mean(numbers)
#     total = 0 
#     for number in numbers:
#         total += (number - x_bar)**2  
#     return total//(len(numbers)-1) 


# def standard_deviation(numbers):
#     '''
#     description: 求标准差
#     '''  
#     return variance(numbers) ** 0.5
    
# def median(numbers):
#     # 函数的设计要做到无副作用，下面的写法会影响原参数
#     # numbers.sort()
#     '''找出中位数'''
#     new_numbers = sorted(new_numbers)
#     if len(new_numbers)%2 ==0:
#         return (new_numbers[len(new_numbers)//2-1]+new_numbers[len(new_numbers)//2])/2
#     else:
#         return new_numbers[(len(new_numbers)-1)//2]

# # 找众数
# def common(numbers):
#     counter = {}
#     for number in numbers:
#         counter[number] = counter.get(number,0) + 1
#     maxcount = 0
#     maxnumber = 0 
#     for key,value in counter.items():
#         if value>maxcount:
#             maxcount = value 
#             maxnumber = key 
#     return maxnumber 
# print(common([12,3,4,12,45,23,12,15]))
