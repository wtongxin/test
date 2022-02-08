##小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# 方法一：
# s1=72
# s2=85
# name='小明'
# grade=(s2-s1)/s1*100
# print(f'{name}成绩提升的百分点为：{grade:.1f}%')
# 方法二：
# s1=72
# s2=85
# r=(s2-s1)/s1*100
# print('小明成绩提升的百分点为:','%.1f%%'%r)


##小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
##低于18.5：过轻
##18.5-25：正常
##25-28：过重
##28-32：肥胖
##高于32：严重肥胖
##用if-elif判断并打印结果：
# 方法一：
# weight = float(input('weight :'))
# height = float(input('height :'))
# BMI = weight/(height ** 2)
# if BMI < 18.5:
#     print('BMI指数：过轻')
# elif 25 > BMI >= 18.5:
#     print('BMI指数：正常')
# elif 28 > BMI >= 25:
#     print('BMI指数：过重')
# elif 32 > BMI >= 28:
#     print('BMI指数：肥胖')
# else:
#     print('BMI指数：严重肥胖')
# 方法二：
# height = 1.75
# weight = 80.5
# variable = '小明的BMI指数：'
# bmi = weight / (height **2)
# if bmi < 18.5:
#    print(f'{variable }过轻')    #f-string 一种格式化字符串的方法，被变量'variable'的值替换，替换为'小明的BMI指数：'
# elif bmi < 25:
#    print('{0}正常'.format(variable ))    #format() 一种格式化字符串的方法。用传入的参数依次替换字符串内的占位符（从{0}开始）。将variable的值（'小明的BMI指数：)'替换成{0}
# elif bmi < 28:
#    print('%s过重' % variable )    #%s 一种格式化字符串的方法。表示用字符串替换。将variable的值（'小明的BMI指数：)'替换成%s
# elif bmi < 32:
#    print(variable + '肥胖')
# else:
#    print(variable + '严重肥胖')


##计算100以内所有奇数之和，可以用while循环实现：
# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)

##利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# #方法一：
# for name in L:
#     print('Hello,', name+'!')
# 方法二：
# for name in L:
#     print('Hello,%s !'%name)
# 方法三：
# for name in L:
#     print(f'Hello,{name},!')
# 方法四：
# y = 0
# while y < 3:
#     u = L[y]
#     print(f'Hello,{u}!')
#     y = y + 1
#方法五：
# for y in range(3):
#  u = L[y]
#  print(f'Hello,{u}!')

##计算1-10的总和：
# sum=0
# for x in range(1,11):
#     sum=sum+x
#     print(x)
# print(sum)

##打印出1-100中5,10,15,20,…,85,90,95,100的数，并计算5,10,15,20,…,85,90,95,100的总和：
#方法一：
# sum = 0
# for x in range(1, 101):
#     if x % 5 == 0:
#         print(x)
#         sum = sum +x
# print(sum)
#方法二：
# sum = 0
# for x in range(0, 101, 5):
#     if x > 0:
#         print(x)
#         sum = sum + x
# print(sum)

##循环出runoob的每个字母(range 在 for 中的使用)：
#方法一：
# name = 'runoob'
# for x in name:
#     print(x)
#方法二：
# name = 'runoob'
# for x in range(len(name)):
#     print(name[x])




