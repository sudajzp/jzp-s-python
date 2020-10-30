#coding utf-8
'''
斐波那契数列-循环法
'''
def Fib_circle():
    while True:
        num_1 = 0
        num_2 = 1
        fib_array = [0] # 用于存储计算出的FB数列值
        m = input('你想要查找的起始项：')
        n = input('你想要查找的结束项：')
        if m.isdigit() and n.isdigit():
            m = int(m) # 将输入化为整数型
            n = int(n)
            for i in range(n):
                num_1, num_2 = num_2, num_1 + num_2
                fib_array.append(num_1)
            print(f'你要查找的数列为{list(enumerate(fib_array[m:], m))}')
            break
        else:
            print('请输入有效的正整数')

if __name__ == '__main__':
    Fib_circle()
