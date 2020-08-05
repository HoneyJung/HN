import sys
def fuck(a,b,i,N,M):
    #print(N,M)
    bfs = []
    dfs = []

    bfs.append(b)
    visited = [0] * (N+1)
    while bfs:#####################################################################2번 루프
        temp = bfs.pop()
        for t in X[temp]:
            if(visited[t] == 1):
                continue
            if t == a:################################################## -1 판명
               # print("-1")
                res[i] = -1
                return
            bfs.append(t)
            visited[t] = 1
 
    dfs.append(a)
    visited = [0] * (N+1)
    while dfs:
        temp = dfs.pop()
        for t in X[temp]:
            if(visited[t] == 1):
                continue
            if t == b:################################################## 1판명
                #print("1")
                res[i] = 1
                return
            dfs.append(t)
            visited[t] = 1
    #print("0")
    res[i] = 0


N,M = map(int,sys.stdin.readline().split())  ############## N M
X = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    X[b].append(a)
NN = int(input())################################구하고자 하는 case 수
res = [0] * (NN) ############case에 대한 결과값.

#print(N,M,NN,X)
for i in range(NN):###################1번 루프 
    a,b = map(int, sys.stdin.readline().split())
    fuck(a,b,i,N,M)

for i in range(NN):
    print(res[i])

