import sys
import collections
dx = [1,-1,0,0]
dy = [0,0,1,-1]
###########
case = int(input())
for _ in range(case):
    m,n = map(int,sys.stdin.readline().split())
    M = [list(input().strip()) for _ in range(n)]
    me = [[0]*m for _ in range(n)]
    F = collections.deque([])

###############bfs
    def bfs():        
        while F:
            #print("M",M)
            #print("me",me)
            #print("F",F)
            a,b,flag = F.popleft()
            for i in range(4):
                if a+dx[i] >= n or a+dx[i] < 0 or b+dy[i] >= m or b+dy[i] < 0:
                    if flag == 0: ###### 사람이면 탈출 성공
                        print(me[a][b])
                        return
                    continue #######불이면 pass
                
                
                if M[a+dx[i]][b+dy[i]] == '*' or M[a+dx[i]][b+dy[i]] == '#' or me[a+dx[i]][b+dy[i]] != 0: 
                    continue
                if flag == 0:
                    me[a+dx[i]][b+dy[i]] = me[a][b] + 1
                if flag == 1:
                    M[a+dx[i]][b+dy[i]] = '*'
                F.append((a+dx[i],b+dy[i],flag))
        print("IMPOSSIBLE")


#초기화
    for i in range(n):
        for j in range(m):
            if M[i][j] == '*':
                F.append((i,j,1)) ##################################### 불이면 flag = 1 
            if M[i][j] == '@':
                xx,yy = i,j
                M[i][j] = '.'
                me[i][j] = 1
    #시작.
    F.append((xx,yy,0))
    bfs()
