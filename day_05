"""
 * @Author:Jude
 * @Description:列表的使用
 * @Date:2023-03-16
"""
# import random
# import time 

# start_time = time.time()
# f1 = f2 = f3 = f4 = f5 = f6 = 0
# for  _ in range(60001):
#     face = random.randrange(1,7)
#     if face == 1:
#         f1 += 1
#     elif face == 2:
#         f2 += 2
#     elif face == 3:
#         f3 += 3
#     elif face == 4:
#         f4 += 4
#     elif face == 5:
#         f5 += 5
#     else:
#         f6 += 6
# end_time = time.time()
# print(f"出现1点的次数为{f1}")
# print(f"出现1点的次数为{f2}")
# print(f"出现1点的次数为{f3}")
# print(f"出现1点的次数为{f4}")
# print(f"出现1点的次数为{f5}")
# print(f"出现1点的次数为{f6}")
# run_time = end_time - start_time
# print(run_time)

# 对列表进行读操作的for循环：
# x只是nums列表中元素的代言人，不会对列表元素产生实质性影响
# nums = [35,98,12,27,66]
# for x in nums:
#     print(x)
#     x = 100 
# print(nums)
# 这里的x用num命名会更好

# 如果要进行读写操作，要使用枚举函数enumerate(nums)
# for i,x in enumerate(nums):
#     print(i,x)

# 对列表进行读写操作的for循环:
# range函数内的数字最好不要写死，这样能应对程序的改动，比如列表增加了元素
# for i in range(len(nums)):
#     print(nums[i])
#     nums[i] = 100
# print(nums)

# 向列表里面追加或者插入元素
# nums.append(100)
# nums.insert(0,1)

# 删除元素（默认是删除最后一个元素）
# nums.pop()

# 使用列表来投骰子，将一个骰子掷60000次，统计每一面出现的次数
# import random 
# touzi = [0,0,0,0,0,0]
# # 列表的重复运算
# touzi = [0] * 6
# for _ in range(60000):
#     face = random.randrange(1,7)
#     touzi[face - 1] += 1
# for i in range(len(touzi)):
#     print("第{}面摇出了{}次".format(i+1,touzi[i]))

#上课案例：输入10个整数，计算平均值、方差和标准差，找出最大值和最小值
# numbers = []
# sum = 0
# for _ in range(10):
#     num = eval(input("请输入整数："))
#     numbers.append(num)

# for num in numbers:
#     sum += num 
# average_num = sum/10

# # 直接用一个函数求列表元素的和也可以
# # average_num = sum(numbers)/len(numbers)
# var_sum = 0
# max_num = numbers[0]
# min_num = numbers[0]

# # 直接用一个函数求列表元素的最大值和最小值也可以
# # max_num = max(numbers)
# # min_num = min(numbers)
# for num in numbers:
#     var_sum = var_sum + pow((average_num - num),2)
#     if max_num < num:
#         max_num = num 
#     if min_num > num:
#         min_num = num 
# variance = var_sum/(len(numbers)-1)
# standard_var = pow(variance,0.5)
# print(f'十个数字的平均值是{average_num}，\
# 方差是{variance:.2f}，标准差是{standard_var:.2f}，\
# 最大值是{max_num}，最小值是{min_num}')
    
# 输入三个整数，按照从大到小的顺序输出
# nums = []
# for _ in range(3):
#     nums.append(eval(input("请输入一个整数:")))
# nums.sort()
# print(nums[::-1])

# 不使用sort函数和列表
# a = eval(input("a = "))
# b = eval(input("b = "))
# c = eval(input("c = "))

# if a < b:
#     a,b = b,a 
# if a < c:
#     a,c = c,a 
# if b < c :
#     b,c = c,b
# print(a,b,c)

# 向列表中添加10个随机整数，找出其中第二大的元素
# 下面的写法是糟糕的写法
# import random 
# integers = []
# for _ in range(10):
#     integers.append(random.randint(0,1000))
# print(integers)
# max_integer = max(integers)
# print(max_integer)
# for integer in integers:
#     if integer==max_integer:
#         integers.remove(integer)
# second_max_integer = max(integers)
# print(integers)
# print(second_max_integer)

# 通过循环的方式去寻找最大值
# import random 
# integers = []
# for _ in range(10):
#     integers.append(random.randint(0,1000))
# print(integers)

# if integers[0] < integers[1]:
#         integers[0],integers[1] = integers[1],integers[0]

# for i in range(2,len(integers)):
#     if integers[0] < integers[i]:
#         integers[0],integers[i] = integers[i],integers[0]
#     if integers[1] < integers[i]:
#         integers[1],integers[i] = integers[i],integers[1]
# print(integers)
# print(integers[1])
            
# 除了交换两个数字，还有没有别的思路？
# import random
# numbers = []
# # 列表生成式语法/推导式等价于下面的for循环追加：
# # 写法更便捷且执行效率更高，因为函数调用更慢
# # numbers = [random.randint(0,1000) for _ in range(10)]
# for _ in range(10):
#     numbers.append(random.randint(0,1000))
# a,b = numbers[0],numbers[1]
# print(numbers)
# if a < b:
#     a,b = numbers[1],numbers[0]
# for i in range(2,len(numbers)):
#     if numbers[i] > a:
#         a,b = numbers[i],a 
#     elif numbers[i] == a:
#         pass
#     elif numbers[i] > b:
#         b = numbers[i]
# print(b) 

# # 使用list也可以生成列表，这种方式是构造器函数
# list_1 = list(range(1,10))

# # 综上所述，创建列表可以有三种方式
# # 第一种，使用字面量语法
# # 第二种，使用构造器函数来生成列表
# # 第三种，使用列表生成式来生成列表
# list_1 = ['apple','orange','pear','banana']

# list_1 = list('apple') #结果list_1为：['a','p','p','l','e']

# list_1=[i for i in range(101)]

# # 列表的运算
# # 重复运算*
# list = [1,10,100]*3 # 返回结果 [1,10,100,1,10,100,1,10,100]

# # 合并运算
# list_1 = [1,3,5,7]
# list_2 = [2,4,6]
# temp = list_1 + list_2
# print(temp)

# # 比较大小
# list_3 = [1,3,5,8]
# print(list_3 > list_1)

# # 删除元素
# list_1.pop(0) # 删除列表的第一个元素
# print(list_1.pop(0)) # 被删除的那个元素会被打印出来
# del list_1[0] # 删除列表的第一个元素

# items = ['apple','orange','pear','banana']
# # items.remove("apple") # 删除列表中的某个具体值
# # # 清空列表元素
# # items.clear()

# # 逆序输出,对原列表无影响
# print(items[::-1])
# print(items)

# # items列表反转，原列表改变
# items.reverse()
# print(items)

# # items列表升序,降序用reverse
# items.sort(reverse = True)

# 如果对一个列表元素进行排序，不使用sort方法应该怎么办？
# nums = [35,12,99,58,67,42,49,31,73]
# new_nums = []
# for i in range(0,len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if nums[i] > nums[j]:
#             nums[i],nums[j] = nums[j],nums[i]

# print(nums)

# 第二种思路,这种方法实际上是
# 简单选择排序：每次从剩下的元素中选择最小
# nums = [35,12,99,58,67,42,49,31,73]
# sorted_nums = []
# while len(nums) > 0:
#     sorted_nums.append(min(nums))
#     nums.remove(min(nums))
# print(sorted_nums)    

# 冒泡排序：简单排序算法，效率比较低
# 元素两两做比较，如果前面的元素大于后面的元素，就交换两个元素的位置
# 大的沉下去，小的冒起来
# nums = [35,12,99,58,67,42,49,31,73]
# for i in range(1,len(nums)):
#     for i in range(len(nums)-i):
#         if nums[i] > nums[i+1]:
#             nums[i],nums[i+1] = nums[i+1],nums[i]
# print(nums)

# # 优化冒泡算法，比如[9,1,2,3,4,5,6,7,8]
# # 事实上只要做一次冒泡排序比较就可以
# nums = [35,12,99,58,67,42,49,31,73]
# for i in range(1,len(nums)):
#     swapped = False 
#     for i in range(len(nums)-i):
#         if nums[i] > nums[i+1]:
#             nums[i],nums[i+1] = nums[i+1],nums[i]
#             swapped = True 
#     if not swapped:
#         break 
# print(nums)

# 冒泡排序升级版：搅拌排序/鸡尾酒排序
# 应对的是[2,3,4,5,6,7,8,9,1]这种极端情况
# nums = [2,3,4,5,6,7,8,9,1]
# swapped = False
# for i in range(1,len(nums)):
#     for j in range(0,len(nums)-i):
#         # if nums[j] > nums[j+1]:
#         #     nums[j],nums[j+1] = nums[j+1],nums[j]
#         #     swapped = True

#         x = len(nums)-j-1

#         if nums[x] < nums[x-1]:
#             nums[x],nums[x-1] = nums[x-1],nums[x]
#             swapped = True
#     if not swapped:
#         break
# print(nums) 

# 列表的应用，随机抽取和乱序
# import random 
# names = ['小红','小明','小英','小白','小李']
# # sample函数可以对列表元素进行无放回抽样
# print(random.sample(names,3))
# # choices函数可以对列表元素进行有放回抽样
# print(random.choices(names,k=3))


# 例题：幸运的女人
# 有15个男人和15个女人坐船出海，船坏了，需要把其中15个人
# 扔到海里，其他人才能活下来；所有人围成一圈，由某个人从1
# 开始依次报数，报到9的人被扔到海里，下一个重新从1开始报数
# 直到将15个人扔到海里，最后，15个女人都幸存了下来，15个
# 男人被扔到了海里。问原先哪些位置是男人，哪位位置是女人
# people = [True] * 30
# print(people)
# counter,index,number = 0,0,0
# while counter <= 15:
#     if people[index]:
#         number += 1 
#         if number == 9:
#             people[index] = False 
#             counter = counter + 1
#     index = index + 1 
#     if index == 30:
#         index = 0
# print(people)

# people = [i for i in range(30)]
# for i in range(15):
#     people = people[9:]+people[:8]
# new_people=[i for i in range(30)]
# for i in new_people:
#     if i in people:
#         new_people[i] = '女'
#     else:
#         new_people[i] = '男'
# print(new_people)



# 用一个列表保存54张扑克牌，先洗牌
# 再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第一个玩家(地主)
# 最后把每个玩家手上的牌显示出来
# import random
# pokers = []
# faces = ['♥','♦','♣','♠']
# counts=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# for face in faces:
#     for count in counts:
#         pokers.append(face+count)
# pokers.append('大王')
# pokers.append('小王')
# random.shuffle(pokers)
# # user_a = []
# # user_b = []
# # user_c = []
# # 定义一个嵌套列表
# players = [[] for _ in range(3)]
# # for i in range(1,len(pokers)-3+1,3):
# #     user_a.append(pokers[i])
# #     user_b.append(pokers[i+1])
# #     user_c.append(pokers[i+2])
# for _ in range(17):
#     for player in players:
#         player.append(pokers.pop())
# players[0] = players[0]+pokers
# for player in players:
#     player.sort(key = lambda x:x[1:])
#     print(player)
# for i in range(1,4):
#     user_a.append(pokers[-i])
# user_a.sort(key = lambda x:x[1:])
# user_b.sort(key = lambda x:x[1:])
# user_c.sort(key = lambda x:x[1:])

# 保存5个学生，3门课程的成绩
import random
names = ['小明','小红','小李','小灰','小白']
courses = ['语文','英语','数学']
scores = [[random.randint(70,100) for _ in range(3)]for _ in range(5)]
# scores =[
#     [88,90,95],
#     [85,92,80],
#     [79,96,87],
#     [78,83,93],
#     [84,91,89]
# ]
# print(scores)
# for i,name in enumerate(names):
#     for j,course in enumerate(courses):
#        print("{}的{}成绩是{}分".format(name,course,scores[i][j]))

# 统计每个学生的平均成绩
# avg=[]
# for student in scores:
#     sum = 0 
#     for i in range(len(student)):
#         sum += student[i]
#     avg_result = round(sum/len(student),1)
#     avg.append(avg_result)
# for i in range(len(names)):
#     print("{}的平均成绩为{}".format(names[i],avg[i]))

# 统计每个学生的最高分和最低分
# max_numbers = []
# min_numbers = []
# print(scores)
# for i,score in enumerate(scores):  
#     max_number = score[0]
#     min_number = score[0]
#     for j in range(len(score)):
#         if max_number < score[j]:
#             max_number = score[j]
#         if min_number > score[j]:
#             min_number = score[j]
        
#     max_numbers.append(max_number)
#     min_numbers.append(min_number)
# print(max_numbers)
# print(min_numbers)                

# 统计每门课程的最高分和最低分
# print(scores)
# print(courses)
# max_score = []
# min_score = []
# for i in range(len(courses)):
#     max_grade = scores[0][i]
#     min_grade = scores[0][i]
#     print(max_grade,min_grade)
#     for j in range(len(scores)):
#         if max_grade > scores[j][i]:
#             max_grade = scores[j][i]
#         if min_grade < scores[j][i]:
#             min_grade = scores[j][i]
#     max_score.append(max_grade)
#     min_score.append(min_grade)
# print(max_score)
# print(min_score)

# 一种更简便的方法，把原列表转变为语文一个列表，数学一个列表，英语一个列表，三个列表组成
for j,course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print("{}的最高分是{}".format(course,max(temp)))
    print("{}的最低分是{}".format(course,min(temp)))
