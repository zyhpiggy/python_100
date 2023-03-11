"""
 * @Author:Jude
 * @Description:循环结构练习
 * @Date:2023-03-06
"""
# 示例一 重复打印hello world 100遍
# for i in range(100):
#     print(i,"hello world")
#     print(i,"goodbye")

# 希望从1开始
# for i in range(1,101):
#     print(i,'hello world')
#     print(i,"goodbye")

# # 理解缩进,但是第二个print中建议不要再用i，i一般只在循环内使用
# for i in range(1,101):
#     print(i,'hello world')
# print(i,"goodbye")

# # 1—100之内的求和
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# # 1—100之内的偶数和，嵌套层次上更扁平，这里循环做了50次，下面的循环做了100次，判断做了50次
# # 效率上更好
# sum = 0
# for i in range(2,101,2):
#     sum += i
# print(sum)

# # 1—100之内的偶数和 ，使用if语句做判断，写了if可以不写else
# # 如果没想好要写什么，可以先写pass（一个空语句），运行时就不会报错
# sum = 0
# for i in range(1,101):
#     if i%2 == 0:
#         sum += i
#     else:
#         pass
# print(sum)
# # 1—100之内的偶数和
# total = sum(range(2,101,2))
# print(total)
# # 100以内，3或者是5的倍数进行求和
# sum = 0 
# for i in range(0,101):
#     if i%3 == 0 or i%5 == 0:
#         sum += i 
# print(sum)

# 练习 ： 输入两个正整数，找出它们的最大公约数
# number_1 = eval(input("请输入第一个正整数："))
# number_2 = eval(input("请输入第二个正整数："))
# min_number = min(number_1,number_2)
# for i in range(1,min_number):
#     if number_1 % i == 0 and number_2 % i == 0:
#         gongyueshu = i 
# print(gongyueshu)

# 方法二：倒数来求最大公约数
# number_1 = eval(input("请输入第一个正整数："))
# number_2 = eval(input("请输入第二个正整数："))
# for i in range(number_1,0,-1):
#     if number_1 % i == 0 and number_2 % i == 0:
#         print(i)    
#         break      # 求到最大的公约数就停止循环

# 练习：输入一个非负整数N，计算N的阶乘
# number = eval(input("请输入一个非负整数："))
# total = 1
# for i in range(number,1,-1):
#     total *= i
# print(total)

# # while循环,示例一，根本停不下来的循环
# while True:
#     print("hello world")

# # 使用条件判断和break组合来结束循环，这种写法前后矛盾
# i = 0 
# while True:
#     print("hello wrold")
#     i += 0 
#     if i > 10:
#         break
# # 不如下面的写法
# i = 0
# while i<=10:
#     print("hello wrold")
#     i += 0 
# print("game over!")

# 欧几里得算法求两个正整数的最大公约数
# 15,27 ->12,15->3,12->3为最大公约数
number_1 = eval(input("请输入第一个正整数："))
number_2 = eval(input("请输入第二个正整数："))
while number_2 % number_1 != 0:
    number_1,number_2 = number_2 % number_1,number_1
print(number_1)
