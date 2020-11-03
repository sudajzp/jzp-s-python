#coding UTF-8
'''
Ford-Filkerson算法
'''
class Dot():
    def __init__(self, l, deta, type):
        self.type = type
        self.l = l
        self.deta = deta

    def __str__(self):
        return str(self.l) + str(self.deta) + str(self.type)


def FF(dot, f, c, n):
    while True:
        '''
        更新
        '''
        dot[0].type = 1
        visit = [0] * n
        for i in range(n):
            if not visit[i] and dot[i].type:
                for j in range(n):
                    if not dot[j].type and c[i][j] - f[i][j] > 0:
                        dot[j].l = i + 1
                        dot[j].deta = min(dot[i].deta, c[i][j] - f[i][j])
                        dot[j].type = 1
                    elif not dot[j].type and f[j][i] > 0:
                        dot[j].l = - (i + 1)
                        dot[j].deta = min(dot[i].deta, f[j][i])
                        dot[j].type = 1
                visit[i] = 1
            # print(1)
        if not dot[n - 1].type:    # 如果收点没有被访问，没有增广链，结束循环
            break

        '''
        选择增广链
        '''

        v = n    # 位置参数：dot[i].l 存储index = i的顶点的父节点的位置参数
        path = []    # 增广路径,存储index
        F = INF
        while v != 1:
            if F > dot[v - 1].deta:
                F = dot[v - 1].deta
            path.append(v - 1)
            v = abs(dot[v - 1].l)
            # print(2)

        '''
        增广
        '''

        for i in path:
            if dot[i].l > 0:
                f[dot[i].l - 1][i] += F
            elif dot[i].l < 0:
                f[i][dot[i].l - 1] += F
            # print(3)

        '''
        取消所有标点
        '''
        for i in range(n):
            dot[i].l = 0
            dot[i].type = 0
            dot[i].deta = INF
            # print(4)
    return f

if __name__ == '__main__':
    INF = 999
    n = int(input('请输入顶点个数：'))
    c = [[0] * n for i in range(n)]
    f = [[0] * n for i in range(n)]
    dot = [0] * n
    for i in range(n):
        for j in range(i,n):
            c[i][j] = int(input(f'请输入从顶点{i + 1}到顶点{j + 1}的容量(没有弧相连，容量设置为0)：'))
            #c[i][j] = int(input())
        dot[i] = Dot(0, INF, 0)
    f = FF(dot, f, c, n)
    for i in range(n):
        for j in range(n):
            if f[i][j] != 0:
                print(f'从顶点{i + 1}到顶点{j + 1}的流量为{f[i][j]}')