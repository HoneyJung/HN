##################################3
import copy
import sys
import collections
'''
걍 빈곳 3개 골라서 다 세워본다.
그리고 각 상황에서 바이러스로부터 bfs돌려서 다 전염시키고 전염안된곳 count해서 max에 저장.

'''
maxi = 0
def f2():
    global maxi
    global dx,dy
    tempQ = []
    tempV = []
    tempM = [[int(x) for x in M[i]] for i in range(n)]
    for x in virus:
        tempV.append(x)

    #print(dx,dy)
    visited = [[0] * m for _ in range(n)]  ############## visited
    #print("initial visited",visited)
    #print("initial tempM",tempM)
    #print("initial tempV",tempV)
    #visited[0][1] = 100
    #print(visited,"fuck")
    while tempV:                                     
        a,b = tempV.pop(0)
        if(visited[a][b] == 1):
            continue
        tempQ.append((a,b))
        while tempQ:
            x, y = tempQ.pop()
            #print("x,y : ",x,y)
            if visited[x][y] == 1:
                continue
            visited[x][y] = 1
            
            for i in range(4):
                #print("tempM",tempM)
                #print("visited",visited)
                if( (x + dx[i] < 0) or (x + dx[i] >= n) or (y + dy[i] < 0 ) or (y + dy[i] >= m)): ################ 범위넘어가면
                    #print("범위 넘어감", x+dx[i],y+dy[i])
                    continue
                if visited[x+dx[i]][y+dy[i]] == 1:
                    #print("이미 방문", x+dx[i],y+dy[i])
                    continue    
                if tempM[x + dx[i] ][ y + dy[i] ] == 0:
                   # print("wrjoiroi")
                    #print("전염 " ,x+dx[i],y+dy[i])
                    tempQ.append((x+dx[i],y+dy[i]))
                    tempM[x+dx[i]][y+dy[i]] = 3

    #print(tempM)
    #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    #print(tempM)
    count = 0
    for i in range(n):
        for j in range(m):
            if tempM[i][j] == 0:
                count = count + 1
    #print(count)
    if maxi < count:
        maxi = count

def f1(z):
    if z == 3: #######3개 벽 치면
        f2()
    else:
        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    M[i][j] = 1
                    f1(z+1)
                    M[i][j] = 0

    return

#############################################################################################################################  recursion.
Q = []
virus = []
n, m = map(int,sys.stdin.readline().split())
M = [[int(x) for x in input().split()] for _ in range(n)]
#print(M)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    for j in range(m):
        if M[i][j] == 2:
            virus.append((i,j)) ################## virus append 해준다.

for i in range(n): ################### 벽을 다 세워본다.....
    for j in range(m):
        if M[i][j] == 0 :
            M[i][j] = 1
            f1(1) 
            M[i][j] = 0

print(maxi)
