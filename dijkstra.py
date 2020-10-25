#dijkstra算法
dim=input("请输入顶点个数：")
dim=int(dim)
G=[[0]*dim for i in range(dim)]
print("请输入权矩阵：\n")
for j in range(dim):
    for k in range(dim):
        G[j][k]=int(input())
visit=[0]*dim#设置一个访问判断向量
distance=[999]*dim#距离向量
parent=[0]*dim#父节点向量
visit[0]=1#从顶点1开始访问
startnode=0#顶点1为起始顶点
distance[0]=0
count=0
for count in range(dim-1):#每个顶点作为起始顶点遍历一次
    for i in range(dim):
        if visit[i]==0:
            if distance[i]>G[startnode][i]:#更新距离矩阵
                distance[i]=G[startnode][i]
                parent[i]=startnode+1#更新父顶点
    m=999
    for i in range(dim):#求最短距离和最短距离的顶点
        if visit[i]==0 and m>distance[i]:
            m=distance[i]
            startnode=i
    visit[startnode]=1
if m==999:
    print("没有最小树")
else:
    print("生成树的距离矩阵：",distance)#输出权矩阵(index+1)
    print("生成树的形状：",parent)#输出上一个节点（index+1）

