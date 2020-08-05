import sys
#test = [1,2,3]
##test2 = [4,5]
#test.extend(test2)
#print(test)
N, H = map(int,sys.stdin.readline().split())
M = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
L = []
M2 = [[ [] for _ in range(N)] for _ in range(N)]
for i in range(H):
    a,b,c = map(int,sys.stdin.readline().split())
    M2[a-1][b-1].append([a-1,b-1,c-1,i])
    L.append((a-1,b-1))

# print(L) # 
# print("map : ",M)
# print("내가 만든 거 :",M2)

turn = 0
turnf = 0
success = 0
while 1:
    if turn > 1000:
        turnf = 1
        break
    if success == 1:
        break
    turn  = turn + 1
    for q in range(H):
        i,j = L[q]
        #p#rint(i,j)
        for p in range(len(M2[i][j])): # find
            x = M2[i][j][p]
            #print(x)
            if x[3] == q:
                break
        d = x[2] # 방향
        if d==0: # ->
            ii = i
            jj = j+1
        if d==1: # <-
            ii = i
            jj = j-1
        if d==2: # up
            ii = i-1
            jj = j
        if d==3:
            ii = i+1
            jj = j
        flag = 0
        if ii < 0 or jj < 0 or ii>=N or jj>=N:
            flag = 1
        elif M[ii][jj] == 0: # white
            for o in M2[i][j][p:]:
                o[0] = ii
                o[1] = jj
            temp = M2[i][j][p:]
            M2[ii][jj]+=(M2[i][j][p:])
            M2[i][j] = M2[i][j][:p]
        elif M[ii][jj] == 1: # red
            for o in M2[i][j][p:]:
                o[0] = ii
                o[1] = jj
            temp = M2[i][j][p:]
            temp.reverse()
            M2[ii][jj]+=(temp)
            M2[i][j] = M2[i][j][:p]
        elif M[ii][jj] == 2:# blue
            flag = 1

        if flag ==1:
            #print(d)
            # print(M2)
            # print(x)
            if d==0: # <-
                ii = i
                jj = j-1
                d=1
            elif d==1: # ->
                ii = i
                jj = j+1
                d=0
            elif d==2: # down
                ii = i+1
                jj = j
                d=3
            elif d==3: #up
                ii = i-1
                jj = j
                d=2
            M2[i][j][p][2] = d
            flag = 0
            #print(ii,jj)
            if ii >= N or ii < 0 or jj >= N or jj < 0:
                temp = M2[i][j][p:]
                ii = i
                jj = j
                #print("hi")
            elif M[ii][jj] == 0: # white
                for o in M2[i][j][p:]:
                    o[0] = ii
                    o[1] = jj
                temp = M2[i][j][p:]
                M2[ii][jj]+=(M2[i][j][p:])
                M2[i][j] = M2[i][j][:p]
            elif M[ii][jj] == 1: # red
                for o in M2[i][j][p:]:
                    o[0] = ii
                    o[1] = jj
                temp = M2[i][j][p:]
                temp.reverse()
                M2[ii][jj]+=temp
                M2[i][j] = M2[i][j][:p]
            elif M[ii][jj] == 2: # blue
                temp = M2[i][j][p:]
                ii = i
                jj = j
        for y in temp:
            L[y[3]] = (ii,jj)
        
       
        if len(M2[ii][jj]) >= 4:
            success = 1
            break
        #print(M2)
        # for i in range(len(M2)):
        #     print(M2[i])
        # print("\n")
    

        
if success == 1:
    print(turn)
else:
    print(-1)