#floyd算法
#定义floyd函数
def Floyd(G,R):
    #将第k个顶点作为跳板
    k = 1
    while True:
        for i in range(n):
            for j in range(n):
                if G[i][j] > G[i][k-1] + G[k-1][j]:
                    G[i][j] = G[i][k-1] + G[k-1][j]
                    R[i][j] = R[i][k-1]
                else:
                    G[i][j] = G[i][j]
                    R[i][j] = R[i][j]
        if k == n:
            return G, R
        else:
            k += 1

#main
#权矩阵在第k步更新时，与此时已更新的权值无关，所以只需要二维列表即可完成更新迭代。
n = int(input('请输入顶点个数：'))
G = [[0] * n for i in range(n)]
R = [[0] * n for i in range(n)]
print('请输入权矩阵:')
for i in range(n):
    for j in range(n):
        G[i][j] = int(input())
        R[i][j] = j + 1
Floyd(G,R)
print(G,R)