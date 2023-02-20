## Day 2 python语言元素
https://www.bilibili.com/video/BV1FT4y1R7sz?p=10&spm_id_from=pageDriver&vd_source=9a3365fff774e958354d6f2880eb6833


### 运算符
- 1、赋值运算符（=）
  - a = 4
  - b = 5
- 2、算术运算符(+、-、*、/、**、%、//) 
  - a = 4 + 3
- 3、复合运算符(+=、-=、*=、/=、//=，**=)
  - a += 10
  - a *= b + 2 
- 4、关系运算符/比较运算符(==、!=、>、<、<=、>=)     ——用来比大小，关系运算会产生布尔值（True 或 False）
  - True 在计算机是指非0
  - False 在计算机是指0
  - print(a>b)
- 5、逻辑运算符(and与、or或、not非)：多个关系运算符的结果进行组合，and 同时是真才为真，or 有一个真就为真，not 取反
  - 短路运算原则，当有多个表达式（值）时，左边的表达式值可以确定结果时，就不再继续运算右边的表达式的值。
  - and与：如果第一个表达式的值为假，则返回表达式1；or或：如果第一个表达式的值为真，则返回表达式1
  - print(a>b and a<5)
  - print( TRUE and FALSE)
  - print( TRUE and TURE)
  - print( FALSE OR FALSE)


### VS Code 技巧：
- 1、按住ctrl键，就能快速跳到源代码的定义，例如math.pi
- 
