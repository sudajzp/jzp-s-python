#coding utf-8
'''
生成概率随机数，并求期望均值
'''

import numpy as np
from numpy.random import default_rng
from scipy import stats

rng = default_rng()

'''均匀分布'''
# uni = rng.uniform(2, 4, 100)
# print(f'U(2,4)分布的均值为：{stats.describe(uni).mean}')
# print(f'U(2,4)分布的方差为：{stats.describe(uni).variance}')

'''二项分布'''
# BNL = rng.binomial(10, 0.4, 100)
# print(f'b(10, 0.4)分布的均值为：{stats.describe(BNL).mean}')
# print(f'b(10, 0.4)分布的方差为：{stats.describe(BNL).variance}')

'''标准正态分布'''
# Std_norm = rng.standard_normal(100)
# print(f'标准正态分布的均值为：{stats.describe(Std_norm).mean}')
# print(f'标准正态分布的方差为：{stats.describe(Std_norm).variance}')

'''正态分布'''
# norm = rng.normal(9, 20, 100)
# print(f'N(9, 20)分布的均值为：{stats.describe(norm).mean}')
# print(f'N(9, 20)分布的方差为：{stats.describe(norm).variance}')

'''伽马分布'''
# gam = rng.gamma(10, 0.4, 100)
# print(f'Ga(10, 0.4)分布的均值为：{stats.describe(gam).mean}')
# print(f'Ga(10, 0.4)分布的方差为：{stats.describe(gam).variance}')

'''贝塔分布'''
# beta = rng.beta(10, 30, 100)
# print(f'Be(10, 0.4)分布的均值为：{stats.describe(beta).mean}')
# print(f'Be(10, 0.4)分布的方差为：{stats.describe(beta).variance}')

'''指数分布'''
# E = rng.exponential(0.4, 100)
# print(f'Exp(0.4)分布的均值为：{stats.describe(E).mean}')
# print(f'Exp(0.4)分布的方差为：{stats.describe(E).variance}')

'''卡方分布'''
# chi2 = rng.chisquare(9, 100)
# print(f'自由度为9的卡方分布的均值为：{stats.describe(chi2).mean}')
# print(f'自由度为9的卡方分布的方差为：{stats.describe(chi2).variance}')

'''F分布'''
# f = rng.f(10, 8, 100)
# print(f'F(10, 8)分布的均值为：{stats.describe(f).mean}')
# print(f'F(10, 8)分布的方差为：{stats.describe(f).variance}')

'''超几何分布'''
# hyper = rng.hypergeometric(30, 20, 10, 100)
# print(f'h(10, 30, 20)分布的均值为：{stats.describe(hyper).mean}')
# print(f'h(10, 30, 20)分布的方差为：{stats.describe(hyper).variance}')