"""
 * @Author:Jude
 * @Description:逻辑运算符的应用
 * @Date:2023-02-20
"""
# 练习1：判断一个用户输入的数字是否为大于50的偶数
# 如果符合条件退出程序，如果不符合条件继续输入数字判断

number = eval(input("请输入一个数字："))
flag_01 = number>50
flag_02 = number%2 == 0 
while True:
    if flag_01 and flag_02:
        print("该数为大于50的偶数")
        break
    else:
        print("该数不满足大于50的偶数条件")
        number = eval(input("请输入一个数字："))
        flag_01 = number>50
        flag_02 = number%2 == 0 

# 练习2：输入年份判断是不是闰年
year = eval(input("请输入年份:"))
flag = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(flag)

# 练习3：输入一个三角形边长，判断能否构成三角形
a = eval(input("请输入第一条边的边长："))
b = eval(input("请输入第二条边的边长："))
c = eval(input("请输入第三条边的边长: "))
if (a+b>c and a+c>b and b+c>a):
    print("这三条边可以构成三角形")
else:
    print("这三条边不能构成三角形")
        
