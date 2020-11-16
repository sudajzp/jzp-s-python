#coding utf-8

'''
概率分布
'''
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']        # 绘图支持中文
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False       # 绘图支持负号



class Sample:
    def __init__(self, start, stop, step):
        self.X = np.arange(start, stop, step)

    def plot(self, P):
        plt.plot(self.X, P, marker = 'o', linestyle = None)
        plt.xlabel('随机变量：X')
        plt.ylabel('概率\密度')
        plt.show()

    def hist(self, P):
        plt.hist()

    def bernoulli(self, p):
        P = stats.bernoulli.pmf(self.X, p)          # 生成self.X的概率列表：离散型用pmf,连续性用pdf
        return P

    def binom(self, n, p):
        P = stats.binom.pmf(self.X, n, p)
        return P

    def poisson(self, mu):
        P = stats.poisson.pmf(self.X, mu)
        return P

    def norm(self, mu, sigma):
        P = stats.norm.pdf(self.X, mu, sigma)
        return P

    def beta(self, m, n):
        P = stats.beta.pdf(self.X, m, n)
        return P, list

    def uniform(self, L, M):
        P = stats.uniform.pdf(self.X, L, M)
        return P

    def expon(self, m):
        P = stats.expon.pdf(self.X, m)
        return P

    def chi2(self, n):
        P = stats.chi2.pdf(self.X, n)
        return P

    def f(self, m, n):
        P = stats.f.pdf(self.X, m, n)
        return P, list

    def gamma(self, m, n):
        P = stats.gamma.pdf(self.X, m, n)
        return P

    def hypergeom(self, N, M, n):
        P = stats.hypergeom.pmf(self.X, N, M, n)
        return P



if __name__ == "__main__":
    x = Sample(0, 10, 1)
    # x = Sample(-5, 6, 0.01)
    # x = Sample(0, 1, 0.01)
    # x = Sample(0, 20, 0.1)
    # P = x.norm(0, 1)
    # P = x.bernoulli(0.4)
    # P = x.poisson(3)
    P = x.binom(20, 0.2)
    # P = x.gamma(10, 1/2)
    # P = x.hypergeom(30, 20, 10)
    x.plot(P)

    # print(x.norm(0, 1))


