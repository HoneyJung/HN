import sys
N,M = map(int,sys.stdin.readline().split())
X = []
res = [0 for _ in range(N+1)]

for i in range(N+1):
    X.append([])
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    X[b].append(a)
bfs = []
 ################# 시작
#print(X)

for i in range(N+1):
    visited = [0]*(N+1)
    if not X[i]: ###비어있으면
        res[i] = 0
        continue
    else:
        visited[i] = 1
        for k in X[i]:
            bfs.append(k)
            #print(k)
            visited[k] = 1 
        while bfs: ###########dfs시작
            temp = bfs.pop()
            res[i] = res[i] + 1
            for j in X[temp]:
                
                if(visited[j] == 1):
                    continue
                else:
                    #print("j",j)
                    bfs.append(j)
                    visited[j] = 1
#print(res)
t = max(res)
for i in range(len(res)):
    if(t == res[i]):
        print(i,end=' ')

