# coding:utf-8      中文编码声明。标识py文件的存储格式，通过记事本打开，另存为时可以看到
# name=input("请输入你的名字：")
# print("hello,",name)

# num1=int(input('请输入第一个数字'))
# num2=int(input('请输入第二个数字'))
# num3=int(input('请输入第三个数字'))
# print(num1,'+',num2,'+',num3,'=',num1+num2+num3)

# print(2*2**4)
# print(4*2**3)

##将数据输出到文件中
##注意点：1、所指定的盘符要存在；2、使用file=xx的形式，否则数据无法写入文件中
# fp=open('D:/text.txt', 'a+')      #输出到D盘中的text中。'a+'是以追加方式写+读的形式打开文件，如果文件不存在就创建，存在的话就在文件内容的后面继续追加
# print('hello,world', '\nhhhhhh', file=fp)
# fp.close()

##\转义字符   \n表示换行   \r表示回车   \t表示水平制表符(四个字符为一个制表位)   \b表示退格
# print('I\'m \"OK\"')
# print('I\'m learning\npython.')
# print('\\\n\\', '\n\'gaga\'\n\"ppp\"')
# print('hello\tworld')    #world将hello进行了覆盖
# print('hello\bworld')    #b是退一个格，将o退没了

##r''  原字符，表示''内部的字符串默认不转义。不希望字符串中的转义字符起作用，就是用原字符，就是在字符串之前加上r，或R
# print('\\\t\\')
# print(r'\\\t\\')

##'''...'''表示多行内容
# print('''line1
# line2
# line3''')    #'''...'''表示多行内容

##多行字符串'''...'''还可以在前面加上r使用
# print(r'''hello,\n
# world''')

##布尔值用在条件判断中
# age=int(input('请输入年龄：'))
# if age>=18:
#     print('adult')
# else:
#     print('teenager')

##判断如果性别为男，输出boy；如果性别为女，输出girl；否则输出请输入正确内容！
# gender=input('性别：')
# if gender=='男':
#     print('boy')
# elif gender=='女':
#     print('girl')
# else:
#     print('请输入正确内容！')

# 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
# a = 123 # a是整数
# print(a)
# a = 'ABC' # a变为字符串
# print(a)    #

##把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(a,b)

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# name = 'xin'
# print('标识：', (id(name)))  # 获取对象的数据类型
# print('类型：', type(name))  # 获取对象所存储的内存地址
# print('值：', name)

# name = 'xin'
# age = 20
# print('我叫' + name + '今年' + str(age) + '岁')     #当将str类型与int类型进行连接时，报错。解决方案：类型转换。将int类型通过str()函数转换为str类型

##str()函数将其它类型转成str类型
# a = 10
# b = 45.55
# c = False
# print(type(a), type(b), type(c))
# print(str(a), type(str(a)), str(b), type(str(b)), str(c), type(str(c)))

##int()函数将其它类型转成int类型
# a = '666'
# b = 99.99
# c = '12.34'
# d = True
# e = 'hello'
# print(type(a), type(b), type(c), type(d), type(e))
# print(int(a), type(int(a)))    #将str转成int类型，字符串为 数字串
# print(int(b), type(int(b)))    #将float转成int类型，截取整数部分，舍掉小数部分
# #print(int(c), type(int(c)))    #将str转成int类型，报错，因为字符串为小数串
# print(int(d), type(int(d)))    #布尔值True可以转化为整数1
# #print(int(e), type(int(e)))    #将str转成int类型时，字符串必须为数字串（整数），非数字串不允许转换

##float()函数将其它数据类型转成float类型
# a = '24.66'
# b = '45'
# c = True
# d = 'hello'
# e = 32
# print(type(a), type(b), type(c), type(d), type(e))
# print(float(a), type(float(a)))
# print(float(b), type(float(b)))
# print(float(c), type(float(c)))
# # print(float(d), type(float(d)))    #字符串中的数据如果是非数字串，则不允许转换
# print(float(e), type(float(e)))


##ord()函数获取字符的整数表示
# print(ord('A'))
# print(ord('中'))
##chr()函数把编码转换为对应的字符
# print(chr(66))
# print(chr(25991))

##计算str包含多少个字符，可以用len()函数
# print(len('strength'))

##%运算符是用来格式化字符串的。
##在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
# print( 'Hello, %s' % 'world')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print('What\'s the time?','It\'s %d o\'clock.' % 5)
# print('Oh,it\'s time to have %s' % 'lunch')
# print('Hello,i am %s,i am %d years old.' % ('Mike',18))
# print('Hello,i am %s' % 'Mike')
# print('I am %d years old.' % 18)
# print('Hi,i am %s.I\'m %d years old.This is my %s' %('xixi',25,'friend'))

##如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
# print( 'Age: %s. Gender: %s' % (25, True))

##字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
# print('growth rate:%d %%' % 7)

##format()  另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
# print('午饭吃了{0}，{1}，花费{2}元，相比上个月多花费{3}%'.format('汉堡','寿司',50,8))
# print('Hi,i am {0}.I\'m {1} years old.This is my {2}'.format('xixi',25,'friend'))

##f-string   一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
# r=2.5
# s=3.14*r**2
# print(f'The area of a circle with radius {r} is {s:.2f}')
# aa=2
# bb=4*aa**3
# print(f'The apples are {aa},the pears are {bb}')

# s1=85
# s2=72
# a='小明'
# b=((s1-s2)/s2)*100
# print(f'{a}成绩提升{b:.1f}%')

##Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
# classmates = ['Michael', 'Bob', 'Tracy','Lucky','Sam']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[1])
# print(classmates[2])
# print(classmates[-1])
# print(classmates[-2])
# print(classmates[-3])

##往list中追加元素到末尾
# classmates.append('Adam')
# print(classmates)

##把元素插入到指定位置
# classmates.insert(1,'Jack')
# print(classmates)
# classmates.insert(3,'Lisa')
# print(classmates)

##删除list末尾的元素
# classmates.pop()
# print(classmates)

##删除指定位置的元素
# classmates.pop(3)
# print(classmates)

##把某个元素替换成别的元素，可直接赋值给对应的索引位置
# classmates[1]='Sarah'
# print(classmates)
# classmates[4]='Rose'
# print(classmates)

##list里面的元素的数据类型也可以不同
# L=['apple',222,True]
# print(L)
##list元素也可以是另一个list
# s= ['python', 'java', ['asp', 'php'], 'scheme']
# print(len(s))
# L=['apple',222,True]
# s= ['python', 'java', L, 'scheme']
# print(s)
# print(L[1])      #拿到L中的'222'
# print(s[2][1])   #拿到L中的'222'

##一个list中一个元素也没有，就是一个空的list，它的长度为0
# L=[]
# print(len(L))

##tuple元组
# classmates=('Michael', 'Bob', 'Tracy')
# print(classmates)


##tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)

##用索引取出下面list的指定元素：
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# 打印Apple
# print(L[0][0])
# 打印Python
# print(L[1][1])
# 打印Lisa
# print(L[2][2])

##if else语句
# age=int(input())
# if age>16:
#     print('Your age is:',age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('child')

##elif语句
# age = 3
# if age >= 18:
#     print('adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

##多个elif语句
# grade = int(input())
# if grade >= 90:
#     print('你的成绩是：', '优秀')
# elif grade > 75:
#     print('你的成绩是：', '良好')
# elif grade > 60:
#     print('你的成绩是：', '及格')
# else:
#     print('你的成绩是：', '不及格')

# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

##for x in循环 依次把list或tuple中的每个元素迭代出来。把每个元素代入变量x，然后执行缩进块的语句
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# 计算1-10的整数之和，可以用一个sum变量做累加：
# sum = 0
# for x in[1,2,3,4,5,6,7,8,9,10] :
#     sum = sum + x
# print(sum)

# word = 'haha'
# for z in('A', 'b', 'C', 'd', 'z'):
#     word = word+z
# print(word)

##计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
# list(range(100))

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

##while循环  只要条件满足，就不断循环，条件不满足时退出循环
# sum = 0
# n = 98
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# num = 100
# for x in range(num):
#     print(x)
# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')

##break  循环打印1～100的数字,提前结束循环
# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

##continue   跳过当前的这次循环，直接开始下一次循环
#打印出1～10中的奇数，可以用continue语句跳过某些循环：
# n=0
# while n<10:
#     n=n+1
#     if n % 2 == 0 :
#         continue
#     print(n)

##dict 字典
##访问字典里的值。把相应的键放入熟悉的方括弧
# tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print("tinydict['Name']: ", tinydict['Name'])
# print("tinydict['Age']: ", tinydict['Age'])

# i = {'name': 'dd', 'age': 24, 'gender': '女', 'interest': ('play games', 'swimming', 'run')}
# print('姓名:', i['name'])
# print('年龄:', i['age'])
# print('性别:', i['gender'])
# print('爱好:', i['interest'])

##修改字典 向字典添加新内容的方法是增加新的键/值对
# i = {'name': 'dd', 'age': 24, 'gender': '女'}
# i['address'] = 'NanJing'
# i['Tel'] = 88866622
# print('姓名:', i['name'])
# print('年龄:', i['age'])
# print('性别:', i['gender'])
# print('地址:', i['address'])
# print('电话:', i['Tel'])
#
# i = {'name': 'dd', 'age': 24, 'gender': '女'}
# i['address'] = 'NanJing'
# i['Tel'] = 88866622
# i['age']=18
# i['name']='bilibili'
# print('姓名:', i['name'])
# print('年龄:', i['age'])
# print('性别:', i['gender'])
# print('地址:', i['address'])
# print('电话:', i['Tel'])

##删除字典元素
# i = {'name': 'dd', 'age': 24, 'gender': '女'}
# del i['name']    #删除键是"name"的条目
# i.clear()        #清空字典所有条目
# del i            #删除字典
# print(i)

##dict字典和list列表的区别
#dict字典
# i = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# i['Ncny'] = 100
# print('Ncny：', i['Ncny'])

#list列表
# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# print(names[0],scores[1])

##通过in判断key是否存在(dict字典)
# i = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print('Bob' in i)      #存在,打印True
# print('Bbb' in i)      #不存在,打印False

##用pop(key)方法删除一个key(键),对应的value(值)也会从dict中删除
# i = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# i.pop('Bob')
# print(i)

##set  创建一个set,需要提供一个list作为输入集合
# i = set([1, 2, 3, 4])
# print(i)

##重复元素在set中自动被过滤
# i = set([1, 2, 3, 2, 6, 1, 4, 3, 5])
# print(i)

##通过add(key)方法添加元素到set中,可重复添加,但不会有效果(set()函数)
# i = set([1, 2, 3])
# i.add(4)
# print(i)

##通过remove(key)方法删除元素(set()函数)
# i = set([1, 2, 3, 4])
# i.remove(3)
# print(i)

##set可以看成数学意义上的无序和无重复元素的集合,因此,两个set可以做数学意义上的交集、并集等操作
# x=set('Michael')
# y=set('Tracy')
# print(x, y)
# print(x&y)      #交集
# print(x|y)      #并集
# print(x-y)      #差集。即集合元素包含在集合a中,但不包含在集合b中

# x = set([1, 2, 3, 4])
# y = set([2, 3, 4, 5])
# print(x, y)
# print(x&y)      #交集
# print(x|y)      #并集
# print(x-y)      #差集。即集合元素包含在集合a中,但不包含在集合b中

# m=[5,9]
# n=m+[6]
# print(n)

# i = {'Michael': 95, 'Bob': (75,88), 'Tracy': ('hh', 'hf')}
# print(i)
# i = {'Michael': 95, 'Bob': 75, 'Tracy': 'hh,fhgfg'}
# print(i)


