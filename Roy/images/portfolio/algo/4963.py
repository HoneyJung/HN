import sys
while(1):
    N, M = map(int,sys.stdin.readline().split())
    if N==0 and M ==0:
        break

    Map = [sys.stdin.readline().split() for _ in range(M)]
    Map2 = [[0 for _ in range(N)] for _ in range(M)]
    dx = [1,1,0,-1, -1,-1,0,1]
    dy = [0,-1,-1,-1, 0,1,1,1]
    cnt = 0
    #print(Map)
    #print(Map2)
    for p in range(M):
        for q in range(N):
            if Map2[p][q] != 0 or Map[p][q]=='0': ## 이미 돈 곳이면
                continue
            cnt = cnt + 1 
            Q = []
            Q.append((p,q))
            #print("kkkkkkkkkkkkkkkkkkkkkkkkkk")
            while Q:
                i,j = Q.pop()
                #print(i,j)
                for k in range(8):
                    ii = i+dx[k]
                    jj = j+dy[k]
                    if ii < 0 or jj < 0 or ii >= M or jj >= N:
                        #print("1")
                        continue
                    elif Map[ii][jj] == '1' and Map2[ii][jj] == 0:
                        Q.append((ii,jj))
                        Map2[ii][jj] = cnt
                        #print("eat : ",ii,jj)
                    else:
                        #print("2 : ", ii,jj)
                        #print(Map[ii][jj],Map2[ii][jj])
                        continue
    print(cnt)
    #print(Map)