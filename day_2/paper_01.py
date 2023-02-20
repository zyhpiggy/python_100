# 算法平均数蕴含了“重心”的意思，中位数用于概括一组数据的位置，是高度耐抗的，有个别的极大值或者极小值，不会引起中位数的变化。

# 在numbers.txt 中随机给出了100个人的某月收入（单位：元），请参照编程模板，求这些数据的算术平均数和中位数。

#在......中填写多行代码
def Arithmetic(numbers):#计算算法平均数
    sum = 0 
    for number in numbers:
        sum += eval(number)
    average_number = round(sum / len(numbers),2)
    return average_number

def Median(numbers):    #计算中位数
    new_numbers = list(map(int,numbers)) #使用map函数对列表每个元素运用int函数映射
    new_numbers.sort()  # 注意，经常弄错搞成将该值赋给一个新变量
    length = len(numbers)

    if length %2 == 0:
        mid_number = (new_numbers[length//2]+new_numbers[length//2+1])/2
    else:
        mid_number = new_numbers[(length+1)//2]
    return mid_number
fo = open("E:\\work\\九江学院\\python学习\\100days\\numbers.txt","r",encoding ="utf-8")
# numbers.txt究竟放在哪个目录下属于同级目录呢？
# 经测试发现要将当前文件夹打开，然后把Txt文件存在与py文件同一个文件夹之下就可以
ls = []
for line in fo.readlines():
    line = line.replace("\n","")
    ls.append(line)

print("算术平均数为{}。".format(Arithmetic(ls)))
print("中位数为{}。".format(Median(ls)))
