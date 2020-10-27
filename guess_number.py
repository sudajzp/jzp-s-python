#猜数字游戏
import random

#guess函数
def guess(num):
    count = 0
    while True:
        count += 1
        number = input('请输入你心中的数字：')
        if number == 'quit':
            print('结束游戏，你输了！')
            break
        elif not number.isdigit() or int(number) not in range(1,100):
            print('请输入1-99之间的整数！')
            continue
        elif int(number) == num:
            print('恭喜你，你猜了{0}次终于猜对了数字{1}!'.format(count,num))
            break
        elif int(number) > num:
            print('你猜大了')
        elif int(number) < num:
            print('你猜小了')

#生成一个1-100之间的随机数
num = random.randint(1,99)
print('猜数字游戏')
print('请猜一个1到99之间的随机数字，输入‘quit’退出游戏')
guess(num)