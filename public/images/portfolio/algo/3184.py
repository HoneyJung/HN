import sys
x,y = map(int,sys.stdin.readline().split())
data = [[0]*y for _ in range(x)]
visit = [[0]*y for _ in range(x)]
temp = []
for i in range(x):
    temp = sys.stdin.readline()
    for j in range(y):
        data[i][j] = temp[j]
#######입력받기

dx = [1,-1,0,0]
dy = [0,0,1,-1]
#print(data)
que = []
que.append((0,0))
visit[0][0] = 1
while que:
    a,b = que.pop(0)
    if a == x-1 and b == y-1:   #########################도착
        print(visit[a][b])
        sys.exit()  
    for i in range(4):
        ax = a + dx[i]
        ay = b + dy[i]
        #print(ax,ay)       
        if ax >= 0 and ay >= 0 and ax < x  and ay < y and visit[ax][ay] == 0 and data[ax][ay] == '1':
        #    print("data :",data[ax][ay])            
            visit[ax][ay] = visit[a][b] + 1
            que.append((ax,ay))


#    print("eiqnhfioqh")


