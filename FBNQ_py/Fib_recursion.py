#coding utf-8
'''
斐波那契数列-递归法
'''
def Fib_rec(n):
    if n <= 1:
        return n
    else:
        return Fib_rec(n - 1) + Fib_rec(n - 2)

def Fib_recursion():
    while True:
        Fib = []
        m = input('你想要查找的起始项：')
        n = input('你想要查找的结束项：')
        if m.isdigit() and n.isdigit():
            m = int(m)  # 将输入化为整数型
            n = int(n)
            for i in range(m, n + 1):
                Fib.append(Fib_rec(i))
            print(f'你想要的查找的数列为：{list(enumerate(Fib,m))}')
            break
        else:
            print('请输入有效的正整数')


if __name__ == '__main__':
    Fib_recursion()