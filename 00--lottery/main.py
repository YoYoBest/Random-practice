#!/usr/bin/python3
#coding:utf-8

import sys
import random
import datetime  #datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。


draw_user_file_path = sys.argv[1]  #获取外部输入1（test.txt） 输入：python main.py test.txt 5
prize_num = sys.argv[2]  #获取外部输入2（5） 输入：python main.py test.txt 5

r = open(draw_user_file_path,'r')  #open() 函数用于打开一个文件
user_list = r.readlines()  #readlines() 读取所有行并返回列表 返回：['7895531@outlook.com\n', 'ysoulcn@gmail.com\n', 'aacheng@gmail.com\n', 'aacheng@gmail.com\n', 'l@safly.com\n', '38277529@qq.com\n', 'caixiaowei0001@126.com\n']
r.close()

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M') #datetime.datetime.now():2021-08-12 20:55:02.537375 strftime('%Y%m%d%H%M'):202108122055

newtime = timestamp[0:4]+'/'+timestamp[4:6]+'/'+timestamp[6:8]+'\000'+timestamp[8:10]+':'+timestamp[10:12] #输出：2021/08/12 2059 切片包左不包右  \000:  终止符，\000后的字符串全部忽略


print('抽奖开始啦'+"------显示时间是:"+ newtime +"\n"*2)
print('参与奖品编号为:' + str(prize_num)+ '的抽奖参与者邮箱列表为:')
print("-" * 20)

n = 1
for i in user_list:
    print('参与者{}:'.format(n) + "***" + i[3:].strip('\n') )  #print ( '{}' . format ( 'zhangk' )),输出：zhangk   {}中是切片位置
    n += 1

	
print('-' *20 + '\n' *2)

print('抽奖开始!')
print("-" * 20)
i = 0
while i<3:
    lucky_user = random.choice(user_list)  # choice() 方法返回一个列表，元组或字符串的随机项。

    user_list.remove(lucky_user)  #去掉随机项

    if i== 0:
        print('中奖者为:' + "***" + lucky_user[3:-1]) #[3:-1]：取第四个到最后一个
    elif i ==1:
        print('候选中奖者为1:' + "***" + lucky_user[3:-1])
    else:
        print('候选中奖者2:' + "***" + lucky_user[3:-1])
    i +=1

print("-" *20)
print("抽奖结束!" + "\n" *2)


# import sys
# import random

# # 接受传入参数
# draw_user_file_path = sys.argv[1]
# prize_num = sys.argv[2]

# # 读取参与者邮箱列表文件
# r = open(draw_user_file_path, 'r')
# user_list = r.readlines()
# r.close()

# # 打印参与者列表
# print('参与奖品编号为：' + str(prize_num) + ' 的抽奖参与者邮箱列表：')
# print('-' * 20)
# for i in user_list:
#     print('参与者：' + '****' + i[3:].strip('\n'))
# print('-' * 20 + '\n' * 2)

# # 抽奖开始
# print('抽奖开始！')
# print('-' * 20)
# i = 0
# while i < 3:
#     lucky_user = random.choice(user_list)
#     user_list_input = user_list.remove(lucky_user)

#     if i == 0:
#         print('中奖者为：' + '****' + lucky_user[3:-1])
#     elif i == 1:
#         print('候选中奖者1为：' + '****' + lucky_user[3:-1])
#     else:
#         print('候选中奖者2为：' + '****' + lucky_user[3:-1])
#     i += 1
# print('-' * 20)
# print('抽奖结束！' + '\n' * 2)
