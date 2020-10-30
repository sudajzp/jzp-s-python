#coding utf-8
'''
斐波那契数列-生成器
'''
def Fib_gen(n):
    num_1 = 0
    num_2 = 1
    for i in range(n):
        num_1, num_2 = num_2, num_1 + num_2
        yield num_1

def Fib_generator():
    while True:
        Fib = [0]
        m = input('你想要查找的起始项：')
        n = input('你想要查找的结束项：')
        if m.isdigit() and n.isdigit():
            m = int(m)  # 将输入化为整数型
            n = int(n)
            fib = Fib_gen(n)
            for num in fib:
                Fib.append(num)
            print(f'你想要查找的数列为：{list(enumerate(Fib[m:], m))}')
            break
        else:
            print('请输入有效的正整数')


if __name__ == '__main__':
    Fib_generator()