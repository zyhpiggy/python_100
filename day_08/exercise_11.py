
"""
 * @Author:Jude
 * @Description:函数的模块管理
 * @Date:2023-05-09
"""
# 获取A班和B班的考试成绩的描述性统计信息
# 比较A班和B班哪个班的学习效果更理想
# import random 
# import exercise_10

# class_a_score = [random.randint(50,100) for _ in range(50)]
# class_b_score = [random.randint(50,100) for _ in range(50)]

# print(f"A班的平均成绩为：{exercise_10.mean(class_a_score)}")

# # 如果要导入的模块和当前文件的路径不一致
# # 做工程化项目开发时，如果项目中的代码文件非常多，我们可以使用包来管理模块
# # 再通过模块来管理函数，包其实就是一个文件夹，而模块就是一个文件
# # 通过这种方式可以解决大型项目中经常遇到的命名冲突问题
# from utilts.stats import * 

# # 解决命名冲突
# # 方法一：导入函数的时候对函数进行别名
# # 方法二：使用完全限定名---->包名.模块名.函数名

# # 定义函数时，写在*前面的参数称为位置参数，调用函数传递参数时，只需要对号入座
# # 写在*后面的参数称为命名关键字参数，调用函数传递参数时，必须写成
# # “参数名=参数值”的形式，例子是choices必须要写k=，而sample不用
# # 关键字参数一定写在位置参数之后
# # 设计函数时，不确定有多少个参数传进来，使用*号表示进行打包操作
# def add(*a):
#     print(a,type(a))
# add(1,2,3,4) 

# # 位置参数*args,**可以接收任一个关键字参数，将所有关键字参数打包成一个字典
# def add(*args,**kwargs):
#     print(kwargs,type(kwargs))
#     total = 0
#     for arg in args:
#         if type(arg) in (int,float):
#             total += arg
#     for value in kwargs.values():
#         if type(value) in (int,float):
#             total += value 
#     return total 
# print(add(1,2,c=3,b=2,a=1,d='hello'))

# def add(*args,**kwargs):
#     print(kwargs,type(kwargs))
#     total = 0
#     for arg in args:
#         if type(arg) in (int,float):
#             total *= arg
#     for value in kwargs.values():
#         if type(value) in (int,float):
#             total *= value 
#     return total 

# # 上面的两段代码不够灵活，重复代码过多，只能做一种运算
# # 如果要提高灵活性，就可以传入参数，
# # 一等函数：
# # 函数可以做输入，也可以做返回值，也可以赋值给变量
# # 这个被称为一等函数
# # fn----->一个实现二元运算的函数
# import operator
# def calc(init_value,fn,*args, **kwargs):
#     total = init_value
#     for arg in args:
#         if type(arg) in (int,float):
#             total = fn(total,arg)
#     for value in kwargs.values():
#         if type(value) in (int,float):
#             total = fn(total,value)
#     return total 
# def add(x,y):
#     return x+y 

# def sub(x,y):
#     return x-y 

# def mul(x,y):
#     return x*y 

# def devision(x,y):
#     return x//y 

# print(calc(0,add,12,13,56,23))
# print(calc(9,operator.add,12,13,45,23))
# print(calc(0,lambda x,y:x+y,12,13,14,56))
# fn = lambda x,y:x+y 
# print(calc(0,fn,12,13,56,23))

# 编写实现对列表元素进行冒泡排序的函数
# 设计函数时一定要注意函数的无副作用性(调用函数不影响传入的参数)
# def bubble_sort(numbers,ascending = True):
#     numbers = numbers[:]
#     for i in range(1,len(numbers)):
#         swapped = False
#         for j in range(0,len(numbers)-i):
#             if numbers[j]>numbers[j+1]:
#                 numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
#                 swapped = True 
#         if not swapped:
#             break 
#     if not ascending:
#         numbers = numbers[::-1]
#     return numbers 
                
## 算法二：二分查找
# def bin_search(items,key):
    
#     # description: 二分查找
#     # items:待查找的列表（元素有序）
#     # key:要找的元素
#     # return:找到了返回元素的索引，找不到返回-1
#     # """
#     start,end = 0 ,len(items)-1
#     while start <= end:
#         mid = (start + end)//2
#         if items[mid] == key :
#             return mid
#         elif items[mid] < key :
#             start = mid + 1
#         else:
#             end = mid - 1 
#     return -1


# if __name__ == '__main__':
#     items = [1,5,8,21,46,78,90]
#     print(bin_search(items,78))

# 保存现场->调用函数->恢复现场
# 每个函数都有属于自己的栈结构，保存现场就是将整个栈结构保存起来

def foo():
    print('foo')

def bar():
    foo()
    print('bar')

def main():
    a,b = 5,10
    bar()
    print(a,b)
    print('game over!')

if __name__ == '__main__':
    main()    
    

# 关于递归,foo函数调用main,而main又调用foo函数
# 这样无休止的调用，那么迟早会将栈空间消耗殆尽，导致程序崩溃
# 官方的cpython调用默认情况下，调用栈的大小是1000
def foo():
    print("hello")
    main()
    
def main():
    foo()
