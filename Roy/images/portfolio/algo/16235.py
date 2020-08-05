import sys
import pprint
N,L,R = map(int,sys.stdin.readline().split())
M = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
#A = [[ N*j+i for i in range(N)] for j in range(N)] 
vis = [[0 for _ in range(N)] for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#Q = [[[] for _ in range(N)] for _ in range(N)]
##print(Q)
#print(A)
time = 0
while(1):
    count = 0
    vis = [[0 for _ in range(N)] for _ in range(N)]
    #Q = [[[(i,j)] for i in range(N)] for j in range(N)]
    #A = [[ N*j+i for i in range(N)] for j in range(N)] 
    for i in range(N):
        for j in range(N):
            if vis[i][j] == 1: # 이미 한 곳이라면
                continue
            else:
                vis[i][j] = 1
                Q = []
                temp = []
                Q.append((i,j))
            #print("start : ",Q)
            while Q:
                x,y = Q.pop()
                #print("pop : ",x,y)
                temp.append((x,y))
                for t in range(4):
                    xx = x+dx[t]
                    yy = y+dy[t]
                    #print(xx,yy,dx[t],dy[t])
                    if xx < 0 or yy <0 or xx >= N or yy >= N or vis[xx][yy] == 1:
                        continue
                    #print(M[x][y] - M[xx][yy])
                    if abs(M[x][y] - M[xx][yy]) >= L and abs(M[x][y] - M[xx][yy]) <=R: # 국경열어야한다면!?
                        count = count + 1
                        vis[xx][yy] = 1
                        Q.append((xx,yy))
                        #print("append: ",xx,yy)
            #print(temp)
            S = 0
            for x,y in temp:
                S = S + M[x][y]
            S = S//len(temp)
            for x,y in temp:
                M[x][y] = S
            # print(M)
    if count == 0:
        break 
    time = time + 1
    #print(M)
print(time)