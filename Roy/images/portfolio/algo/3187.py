import sys
a,b = map(int,sys.stdin.readline().split())
X = [sys.stdin.readline() for _ in range(a)] 
visited  = [[0]*b for _ in range(a)]

v=0
k=0
res1=0
res2=0
bfs = list()
mx = [1,-1,0,0]
my = [0,0,1,-1] ###움직임.
for i in range(a):
    for j in range(b):        
        if(visited[i][j]==1):
            continue
        for m in range(4):
            if (i + mx[m] < 0 or j + my[m] < 0 or i + mx[m] >= a or j + my[m] >= b):
                if(X[i][j] != '#'):
                    bfs.append((i,j)) ###########넣고.
                    visited[i][j] = 1
                    #print(i,j)
                    break

        while bfs: ###bfs 시작.
            c,d = bfs.pop(0)
            for n in range(4):
                if (c+mx[n] < 0 or c + mx[n] >= a or d+my[n] < 0  or d + my[n] >= b): ########### 범위넘어간거 무시.
                    continue 
                else:
                    if( X[c + mx[n] ][d + my[n]] == '#' or visited[c+mx[n]][d+my[n]] == 1 ):
                        continue
                    bfs.append((c+mx[n],d+my[n]))
                    #print(c+mx[n],d+my[n])
                    visited[c+mx[n]][d+my[n]] = 1       
                break
###########################################################################################울타리 밖에꺼 -> visited 1로 처리했음.
#print(visited)
#print(X)
for i in range(a):
    for j in range(b):        
        v=0
        k=0
        if(visited[i][j]==1):
            continue
        if(X[i][j] != '#'):
            bfs.append((i,j))
            #print("here")
            #print(i,j)
        else:
            continue

        while bfs: ###bfs 시작.
            c,d = bfs.pop(0)
            visited[c][d] = 1
            if(X[c][d] == 'k'):
                k = k+1
            #    print("k위치")
            #    print(c,d)
            if(X[c][d] == 'v'):
                v = v+1
             #   print("v위치")
              #  print(c,d)
            for n in range(4):
                if (visited[c+mx[n]][d+my[n]] == 1): 
                    continue 
                if(X[c + mx[n] ][d + my[n]] == '#'):
                    continue
               # print("들어가는거 : ",c+mx[n],d+my[n])
                bfs.append((c+mx[n],d+my[n]))
                visited[c+mx[n]][d+my[n]] = 1
        
        #print("중간")
        #print(v,k)
        if(v>=k):
            res1 = res1 + v
        else:
            res2 = res2 + k
#print("최종")
print(res2,res1)
        
                
