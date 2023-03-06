## Day 4 循环结构
https://www.bilibili.com/video/BV1FT4y1R7sz?p=10&spm_id_from=pageDriver&vd_source=9a3365fff774e958354d6f2880eb6833

- 1、for in 循环  （明确的知道循环执行的次数或者要对一个容器进行迭代）
理解for i in range(10):  
　　　　　　print(i,"hello world")  
      　　　print(i,"goodbye world")  
和 for in range(10):  
     　　　print(i,"hello world")  
　　print(i,"goodbye world")的区别 
- 2、设置断点，进行单步调试，可以观察循环过程中每一个变量的变化
- 断点位于代码序号的左侧，点击一下会出现红色圆点，然后开启运行中的调试模式，开始进行单补调试
- 对于number_1 % i可以点击右键添加到监视变量中去
```Python
"""
输入两个正整数，求最大公约数

Version: 0.1
Author: jude
"""
number_1 = eval(input("请输入第一个正整数："))
number_2 = eval(input("请输入第二个正整数："))
min_number = min(number_1,number_2)
for i in range(1,min_number):
    if number_1 % i == 0 and number_2 % i == 0:
        gongyueshu = i 
print(gongyueshu)
```

- 3、while循环适合不明确知道循环执行的次数
