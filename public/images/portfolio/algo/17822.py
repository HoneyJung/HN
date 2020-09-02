import sys
N,M, T = map(int,sys.stdin.readline().split())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]

for _ in range(T):
    #print(Map)
    x,d,k = map(int,sys.stdin.readline().split())
    for i in range(N):
         if (i+1) % x == 0: # 배수이면
            #print("hi")
            #Map[i] = rotate(Map[i],d,k)
            if d==0:
                s = len(Map[i])
                temp = []
                temp+=Map[i][s-k:]
                temp+=Map[i][:s-k]
            else:
                s= len(Map[i])
                temp = []
                temp += Map[i][k:]
                temp += Map[i][:k]
            Map[i] = temp
        ##############회전 완료
    flag = 0
    #print(Map)
    temp = []
    for x in range(N):
        for y in range(M):
            if y+1 == M:
                if Map[x][y] == Map[x][0] and Map[x][y] !=0:
                    if (x,0) not in temp:
                        temp.append((x,0))
                    if (x,y) not in temp:
                        temp.append((x,y)) 
            elif Map[x][y] == Map[x][y+1]and Map[x][y] !=0:
                if (x,y+1) not in temp:
                    temp.append((x,y+1))
                if (x,y) not in temp:
                    temp.append((x,y))
            elif y-1 == -1:
                if Map[x][y] == Map[x][M-1] and Map[x][y] !=0:
                    if (x,M-1) not in temp:
                        temp.append((x,M-1))
                    if (x,y) not in temp:
                        temp.append((x,y))
            elif Map[x][y] == Map[x][y-1] and Map[x][y] !=0:
                if (x,y-1) not in temp:
                    temp.append((x,y-1))
                if (x,y) not in temp:
                    temp.append((x,y))
            ######################################################################### 양옆   
            if x + 1 < N:
                if Map[x][y] == Map[x+1][y]and Map[x][y] !=0:
                    if (x+1,y) not in temp:
                        temp.append((x+1,y))               
                    if (x,y) not in temp:
                        temp.append((x,y))
            if x - 1 >= 0:
                if Map[x][y] == Map[x-1][y]and Map[x][y] !=0:
                    if (x-1,y) not in temp:
                        temp.append((x-1,y))
                    if (x,y) not in temp:
                        temp.append((x,y))
                    ################################################################## 위아래



    if len(temp) != 0: # 같은게 있으면
        for n1,n2 in temp:
            Map[n1][n2] = 0
    else: #같은게 없으면
        #print("hi")
        Sum = 0
        count = 0
        for n1 in range(N):
            for n2 in range(M):
                if Map[n1][n2] != 0:
                    count = count + 1
                    Sum = Sum + Map[n1][n2]
        if count !=0:
            avg = Sum / count
        else:
            break
        for n1 in range(N):
            for n2 in range(M):
                if Map[n1][n2] > (avg) and Map[n1][n2] !=0:
                    Map[n1][n2] = Map[n1][n2] - 1
                elif Map[n1][n2] < (avg) and Map[n1][n2] !=0:
                    Map[n1][n2] = Map[n1][n2] + 1
       # print(avg)
    #print(Map)

Sum = 0
for n1 in range(N):
    for n2 in range(M):
        Sum = Sum + Map[n1][n2]
print(Sum)

