#coding utf-8
'''
斐波那契数列-迭代器
'''
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration # 手动设置异常，阻止迭代器继续迭代

    def __iter__(self):
        '''迭代器的__iter__返回自身即可'''
        return self

def Fib_iterate():
    while True:
        Fib = [0]
        m = input('你想要查找的起始项：')
        n = input('你想要查找的结束项：')
        if m.isdigit() and n.isdigit():
            m = int(m)  # 将输入化为整数型
            n = int(n)
            fib = Fibonacci(n)
            for num in fib:
                Fib.append(num)
            print(f'你想要查找的数列为：{list(enumerate(Fib[m:], m))}')
            break
        else:
            print('请输入有效的正整数')

if __name__ == '__main__':
    Fib_iterate()