"""
 * @Author:Jude
 * @Description:字符串的索引/切片/操作
 * @Date:2023-04-26
"""
# 字面量语法
# a = 'hello world!'
# b = "hello world!"
# c = '''
# 床前明月光，
# 疑是地上霜。
# 举头望明月，
# 低头思故乡。
# '''

# 写路径的时候，可以写反斜杠，但是要用反斜杠来转义，
# windows系统和其他系统都认同正斜杠的路径
# 还有一种是直接用r，这种字符串叫做原始字符串

# r'c:\Users\Administrator\abc\hello.py'
# 作业一：一个列表中有很多重复元素，写一段代码去掉列表中的重复元素
# items = [12,15,12,12,12,65,15,78,12,47]
# unique_items = []
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)
# print(unique_items)

#作业二：有一个放整数的列表，找出列表中出现次数最多的元素
# items = [12,15,12,12,12,65,15,78,12,47]
# unique_items = []
# counts = {}
# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)
# for i in range(len(unique_items)):
#     count = 0 
#     for item in items:
#         if item == unique_items[i]:
#             print(f"item={item}")
#             print(f"unique_items的第{i}项为{unique_items[i]}")
#             count += 1 
#     print(unique_items[i])
#     counts[unique_items[i]] = count
# max_counts = max(zip(counts.values(),counts.keys()))
# print(max_counts[1])

# 做个标记，假设第一个元素是出现次数最多的
# items = [12,15,12,12,12,65,15,78,12,47]
# max_item,max_counter = items[0],items.count(items[0])
# for item in range(1,len(items)):
#     curr_counter = items.count(item)
#     if curr_counter > max_counter:
#         max_item,max_counter = item,curr_counter
# print(max_item,max_counter)

# 字符串的运算
# 字符串可以比大小，按照从第一个字母比，下面的h大于g，比的是字符串的编码大小
# a = 'hello world!'
# b = 'goodbye world!'
# print(a>b)
# print(ord('W'),ord('e'))

# # 字符串和元组一样是不可更改的，是不变数据类型，只能进行读操作，不能进行写操作
# a[0] = 'H'

# 一个练习：实现跑马灯文字效果
# 效果是这样的：


# 把北字拿掉放到最后一个字符
# content = '京欢迎你为你开天辟地           北'
# content = '欢迎你为你开天辟地           北京'
# content = '迎你为你开天辟地           北京欢'
# 依次循环
# import time
# count = 0  
# content = '北京欢迎你为你开天辟地           '
# while count<=30:
#     print('\r'+content,end='')
#     time.sleep(0.3)
#     content = content[1:]+content[0]
#     count += 1 
    
# 另一种：清屏
# 首先调用OS模块，清除屏幕输出：windows->cls/ macos->clear

# import time
# import os 
# count = 0  
# content = '北京欢迎你为你开天辟地           '
# while count<=30:
#     os.system("cls")
#     print(content)
#     time.sleep(0.3)
#     content = content[1:]+content[0]
#     count += 1 

# a = 'hello world123'
# # upper是字母全大写
# print(a.upper())
# # lower是字母全小写
# print(a.lower())
# # capitalize是首字母大写
# print(a.capitalize())
# # title是每个单词首字母大写
# print(a.title())

# # 判断字符串是否都由数字构成
# print(a.isdigit())
# b = '123'
# print(b.isdigit())

# # 判断字符串是否都由字母构成
# c = 'hello'
# print(c.isalpha())

# # 判断字符串是否由字母和数字构成
# a = 'helloworld123'
# print(a.isalnum())

# # 判断字符串是否由某个字符串开头
# m = '你好呀'
# print(m.startswith('我'))
# print(m.endswith("呀"))

# # 在字符串中查找有没有某个子串的操作
# # ~index/rindex
# # find/rfind
a = 'Oh,apple,i love apple.'

# # 得到索引3是apple的开头,index是从左到右,而rindex是从右往左
# print(a.index("apple"))
# print(a.rindex("apple"))

# # 可以指定从哪里开始找，默认是0
# # 找到了返回字串对应的索引（下标），找不到直接报错（程序崩溃）
# print(a.index('apple',10))
# # 子串不存在时报错
# print(a.index('banana'))

# # find更稳健一些，找不到也不会报错
# print(a.find("apple"))
# print(a.rfind("apple"))
# print(a.find("banana"))


# 字符串的格式化输出
# a = 'hello world'
# # 中间对齐
# print(a.center(80,'-'))
# # 左对齐
# print(a.ljust(80,'-'))
# # 右对齐
# print(a.rjust(80,'-'))

# zerofill函数，在字符串左边补0
# b = '123'
# print(b.zfill(6))

# 中间有空格，不会修剪
# email =' zyhmomo123@gmail.com   '
# print(email.strip())
# print(email.rstrip())
# print(email.lstrip())

# # 替换方法
# content =' 马化腾是个傻逼 '
# # 将指定的字符串替换为新的内容
# # 该方法没有修改原来的字符串，而是产生了新的字符串
# print(content.replace("马化腾","*").replace("傻逼",'*'))


# 字符串的拆分与合并方法
# content = "You go your way, I will go mine."
# content2 = content.replace(',','').replace('.','')

# # 拆分结束后是一个一个列表
# words = content2.split()
# for word in words:
#     print(word)
    
# content3 = content.split(',')
# print(content3)

# # 还有一个参数叫做maxsplit
# content4 = content.split(' ',maxsplit=3)
# print(content4)

# 还有一个从右向左拆分的，最多允许拆分三次 
# content5 = content.rsplit(' ',maxsplit = 3)
# print(content5)

# # 合并方法
# contents = ['床前明月光',
#             '疑是地上霜',
#             '举头望明月',
#             '低头思故乡']
# new_contents = '#'.join(contents)
# print(new_contents)

# # 字符串的编码和解码
# # str ----- 经过字符集编码 ----- bytes
# # gbk是gb2312的扩展集，是两个ascii码拼一起
# a = '我爱你中国'
# b = a.encode('gbk')
# # 一个中文对应两个字节，gbk的编码
# # 在UTF-8中，一个中文由3个字节构成
# # 如果编码和解码的方式不一致，可能会乱码也可能会报异常
# print(b)
# c = b'\xce\xd2\xb0\xae\xc4\xe3\xd6\xd0\xb9\xfa'
# print(c.decode('gbk'))

# # UTF-8是Unicode（万国码）的一种实现方案
# # a = '我爱你中国'
# # b = a.encode('gbk')

# # print(b)

# # 一个emoji字符则占4个字符
# # utf-8是一种变长编码，表示数字和英文字母的时候，只需要一个字符
# m = '🌙🧣'
# n = m.encode()
# print(n,len(n))

# 总结：选择字符集编码时，最佳的选择是UTF-8编码
# 编码和解码的字符集要保持一致，否则就会出现乱码
# 不能用ISO-8859-1编码保存中文，否则会出现编码黑洞，中文全部变成问号
# UTF-8是一种边长编码，最少一个字节，最多4个字节，表示中文用3个字节

# 了解什么是"百分号编码"以及它的应用场景
# 了解什么是"base64编码"以及它的应用场景

# 作业，凯撒密码 - 通过对应字符的替换，实现对明文进行加密的一种方式
# 对称加密：加密和解密使用了相同的密钥 ----> AES
# 非对称加密：加密和解密使用不同的密钥 ----> RSA:适合互联网应用
# abcdefghijklmnopqrstuvwxyz
# defghijklmnopqrstuvwxyzabc

# passwords = input()
# new_password = ''
# for password in passwords:
#     if password == ' ':
#         new_password += ' '
#     else:
#         new_password += chr(ord(password)+3)
# print(new_password)


# # 方法二，使用对照表
# passwords = input()
# table = str.maketrans(
#     'abcdefghijklmnopqrstuvwxyz',
#     'defghijklmnopqrstuvwxyzabc'
# )
# # 通过字符串的translate方法实现字符串转译
# print(passwords.translate(table))

# 集合，不允许有重复元素，也不需要有0，1，2，3的顺序
# python上的集合和数学概念的集合极其相似
# 把一定范围的、确定的、可以区别的事物当作一个整体来看待,集合中
# 的各个事物通常称为集合的元素。集合应该满足以下特性：
# 1、无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的
# 2、互异性：一个集合中，任何两个元素都认为是不相同的，每个元素只能出现一次
# 3、确定性：给定一个集合中

# set1 = {1,1,2,3,1,1,2}
# print(type(set1))
# set2 = set()
# print(type(set2))
# print(set1)

# 在集合中绝对不能使用下标，因为集合的元素是无序的
# 集合的元素可以遍历
# 集合的成员运算在效率上是远远高于列表的成员运算
# for elem in set1:
#     print(elem)

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))

# 对称差(去掉交集的补集)
print(set1^set2)


set1 = {'apple','banana','pitaya'}
# list是不可哈希（散列）的类型，会报错
# 集合底层使用了高效率的存储方式，这种方式称之为哈希存储
# 或者叫做散列存储
# set3 = {[1,2,3],[4,5,6]}
# print(set3)


# 什么叫哈希存储？
# 顺序存储，像列表、元组、字符串，一个元素挨着另一个元素
# 优点：可以实现随机存取，可以指哪儿打哪儿，给一个下标就可以拿到元素
# 缺点：判断元素在不在容器中，查找元素效率都很低下

# 集合是来一个元素，先进行hash()计算，得到一个哈希值
# 这样就可以得到这个元素的位置，而不是挨个存放
# 哈希存储的关键是设计一个好的哈希函数，让不同的对象尽可能地产生不同的哈希码
# 所以集合在元素查找时效率远高于列表，而且不依赖问题规模的大小，是一种常量级时间复杂度的存储方案
# 4、如果一个对象不能计算哈希码，就不能放在集合中，列表就是这样的对象
# （集合、列表、字典）也是一个可变容器，可以删除可以增加
# 但是可以放元组
set1 = {'apple','banana','pitaya'}
set1.add('grade')
set1.add("durian")

# 删除元素是随缘，而不是最后一个
print(set1)
print(set1.pop())
set1.discard("pitaya")
print(set1)

# 清空元素
set1.clear()
print(set1)

# 去重的一种简单方法
list1 = [1,2,3,1,6,8,7,6,7,9]
set1 = set(list1)
list2 = list(set1)
print(list2)
