#coding utf-8
'''
斐波那契数列-矩阵法
'''
import numpy as np

def Fib_matrix():
    while True:
        T = np.array([[1, 1],[1, 0]]) # 变换，计算矩阵
        F = np.array([1, 0]) # 初始矩阵
        Fib = []
        m = input('你想要查找的起始项：')
        n = input('你想要查找的结束项：')
        if m.isdigit() and n.isdigit():
            m = int(m)  # 将输入化为整数型
            n = int(n)
            for i in range(n + 1):
                if i >= m:
                    Fib.append(F[1])
                F = np.dot(T, F)
            print(f'你想要的查找的数列为：{list(enumerate(Fib,m))}')
            break
        else:
            print('请输入有效的正整数！')

if __name__ == '__main__':
    Fib_matrix()