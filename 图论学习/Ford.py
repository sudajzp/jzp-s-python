#权矩阵，存储矩阵，父节点向量
n = int(input('请输入节点个数:'))
weight = [[0] * n for i in range(n)]#列表生成式生成2维列表并初始化
save = [[0] * n for i in range(n)]
parent = [0] * n#父节点
k = 1
print('请输入权矩阵：')
for i in range(n):
    for j in range(n):
        weight[i][j] = int(input())

#初始化父节点，存储矩阵
parent[0] = -1
for i in range(1,n):
    parent[i] = 0
for i in range(n):
    save[0][i] = weight[0][i]#初始化k=1


#循环
while True:
    #对每个顶点遍历最短路径
    for i in range(n):
        for j in range(n):
            #对顶点i，遍历所有顶点，有较小值则更新save列表
            if save[k-1][i] > save[k-1][j] + weight[j][i] or save[k][i] > save[k-1][j] + weight[j][i]:
                save[k][i] = save[k-1][j] + weight[j][i]
                parent[i] = j
            #如果顶点i的save值没有更新即为空值时，以上一步save值更新，不用更新父节点
            elif not save[k][i]:
                save[k][i] = save[k-1][i]
    k += 1
    #当k = n时循环结束
    if k == n:
        break

print(save[n-1],parent)