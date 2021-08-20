import sys
import random
import datetime

mail_strings = sys.argv[1]
number_string = sys.argv[2]

mailTest_CStxts = open(mail_strings,'r')
mailTest_txts_List = mailTest_CStxts.readlines()    #没想出来啊
mailTest_CStxts.close()   #没想起来

timeG = datetime.datetime.now().strftime(format('%Y-%m-%d %H:%M:%S'))

print('开始抽奖啦------'+f'显示时间是：{timeG}'+'\n'*2)

n = 0
print(f'参与奖品编号为:{number_string}'+'的抽奖参与者邮箱列表为：\n')
print('-'*20)

for mailLine_string in mailTest_txts_List:
    n += 1
    print(f'参与者{n}'+':***'+f'{mailLine_string[3:-1]}')
print('-'*20+'\n'*3)

print('抽奖开始！')
print('-'*20)

for i in range(0,3):
    if i == 0:
        zhongjz = random.choice(mailTest_txts_List)
        print(f'中奖者为：***'+f'{zhongjz[3:-1]}')
        i += 1
    elif i == 1:
        houXuan1 = random.choice(mailTest_txts_List)
        i += 1
        print(f'候选中奖者1为：***'+f'{houXuan1[3:-1]}')
    else:
        houXuan2 = random.choice(mailTest_txts_List)
        i += 1
        print(f'候选中奖者2为：***'+f'{houXuan2[3:-1]}')
print('-'*20)
print('抽奖结束！')
