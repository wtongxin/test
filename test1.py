# present=input('你想要什么礼物呢？')
# print(present,type(present))

# a = input('一个加数：')
# a = int(a)
# b = input('另一个加数：')
# b = int(b)
# print(type(a), type(b))
# print('结果：', a + b)

# a = int(input('一个加数：'))
# b = int(input('另一个加数：'))
# print(type(a), type(b))
# print('结果：', a + b)


##赋值运算符
##链式赋值
# a = b = c = 20
# print(a, b, c)
# ##参数赋值
# a = 20
# a += 30  # 相当于a=a+30
# print(a)
# a -= 10  # 相当于a=a-10
# print(a)
# a *= 2  # 相当于a=a*2
# print(a, type(a))
# a /= 3
# print(a, type(a))
# a //= 2
# print(a, type(a))
# a %= 3
# print(a, type(a))
# ##系列解包赋值
# a, b, c = 20, 30, 40
# print(a, b, c)
# # 交换两个变量的值
# a, b, c = 10, 20, 30
# print('交换之前：', a, b, c)
# a, b, c = c, b, a  # 交换
# print('交换之后：', a, b, c)


##比较运算符
# a = 10
# b = 20
# print('a>b吗？', a > b)
# print('a<b吗？', a < b)
# print('a>=b吗？', a >= b)
# print('a<=b吗？', a <= b)
# print('a==b吗？', a == b)
# print('a!=b吗？', a != b)

#=为赋值运算符    ==为比较运算符
#一个变量由三部分组成：标识、类型、值。  ==比较的是值    is比较的是对象的标识
# a=10
# b=10
# print(a==b)      #True  说明a与b的value相等
# print(a is b)    #True  说明a与b的id标识相等
# print(a is not b)    #False   a的id与b的id是不相等的
#
# list1 = [11, 22, 33, 44]
# list2 = [11, 22, 33, 44]
# print(id(list1))
# print(id(list2))
# print(list1 == list2)    #vlaue   --->True
# print(list1 is list2)    #id      --->False
# print(list1 is not list2)    #True    list1的id与list2的id是不相等的


##位运算符
# print(4&8)    #按位与&，同为1时结果为1
# print(4|8)    #按位或|，同为0时结果为0
# print(4<<1)    #向左移动1位（移动1个位置），相当于乘2
# print(4<<2)    #向左移动2位（移动2个位置
# print(4>>1)    #向右移动1位，相当于除以2
# print(4>>2)    #向右移动2位，相当于除以4


# print('----------程序开始----------')
# print('1.把冰箱门打开')
# print('2.把大象放进冰箱里')
# print('3.把冰箱门关上')
# print('----------程序结束----------')

print(bool(False))        #False
print(bool(0))            #False
print(bool(0.0))          #False
print(bool(None))         #False
print(bool(''))           #False
print(bool(""))           #False
print(bool([]))           #空列表 False
print(bool(list[]))       #空列表 False
print(bool(()))           #空元祖 False
print(bool(tuple()))      #空元组 False
print(bool({}))           #空字典 False
print(bool(dict{}))       #空字典 False
print(bool(set()))        #空集合 False
print('----------以上对象的布尔值为False----------')
