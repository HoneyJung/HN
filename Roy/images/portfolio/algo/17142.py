import sys
import itertools
import collections
import copy
n,m = map(int,sys.stdin.readline().split())
Map = [[int(x) for x in sys.stdin.readline().split()]for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
#print(Map)
L = []
for i in range(n):
    for j in range(n):
        if Map[i][j] == 2:
            Map[i][j] = -1 # 바이러스
            L.append((i,j))
        if Map[i][j] == 1:
            Map[i][j] = -2 # 벽
        if Map[i][j] == 0:
            Map[i][j] = -3 # 빈곳

com = list(itertools.combinations(L,m))

mtime = 1000000
t = 1000000
for v in com: # BFS

    t = 0
    dq = collections.deque([])
    M = copy.deepcopy(Map)
    for i in range(m):
        dq.append((v[i][0],v[i][1],t))
        M[v[i][0]][v[i][1]] = 0
    #오른쪾에 넣고
    #왼쪽에서 뺀당
    #print(v)
    #print(M)
    while dq:
        x,y,t = dq.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx >=  n or xx < 0 or yy >= n or yy < 0 or M[xx][yy] >= 0 or M[xx][yy] == -2 or M[xx][yy] == -4: #넘어가거나 벽이거나 이미 간 곳이거나
                continue
            else:
                if M[xx][yy] != -1:    
                    M[xx][yy] = t+1
                else:
                    M[xx][yy] = -4
                dq.append((xx,yy,t+1))
    temp = 0
    flag = 0
    for i in range(n): # 다 채웠나 화긴
        for j in range(n):
            if M[i][j] == -3:
                flag = 1
                break
        if flag ==1:
            break
    if flag ==1 :
        t=10000000
        continue
    for w in range(n):
        if temp < max(M[w]):
            temp = max(M[w])
    t = temp
    #print(t)
    #print(M)
    if mtime > t:
        mtime = t
if mtime == 1000000:
    print(-1)
else:
    print(mtime)