import sys
import collections

firebfs = collections.deque([])
mebfs = collections.deque([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[0 for _ in range(1005)] for _ in range(1005)]
case = int(input())
for zz in range(case):
    firebfs.clear()
    mebfs.clear()
    m,n = map(int,sys.stdin.readline().split())
    M = [[x for x in sys.stdin.readline()] for _ in range(n)]
    for i in range(n):
        M[i].pop()


######################################################################입력받기
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
            if M[i][j] == '@':
                mebfs.append((i,j,0))
                visited[i][j] = 1
                M[i][j] = '.'
            if M[i][j] == '*':
                firebfs.append((i,j,0))
####################################################################################
    flag = 0
    before1 = 0
    before2 = 0
    while mebfs:
        #print(M)
        if flag == 1:
            break
        bbatta1=0
        bbatta2=0
        while mebfs: ################## 사람이 먼저다.
            #print("mebfs",mebfs)
            a,b,depth = mebfs.popleft()

            if depth > before1:
                if bbatta1==0:
                    bbatta1 = bbatta1 + 1
                else:
                    mebfs.append((a,b,depth))
                    break


            before1 = depth 
            #print("a,b : " ,a,b)
            for i in range(4):
                flag = 0###############################탈출성공하면 flag = 1
                if(a+dx[i] >= n or a+dx[i] < 0 or b+dy[i] >= m or b+dy[i] < 0): # 탈출
                    flag = 1
                    break
                if(M[a+dx[i]][b+dy[i]] == '#' or M[a+dx[i]][b+dy[i]] == '*' or visited[a+dx[i]][b+dy[i]] == 1): # 벽이나 * 만나면 pass
                    continue
                f = 0
                for j in range(4):
                    if(a+dx[i]+dx[j] >= n or a+dx[i]+dx[j] < 0 or b+dy[i]+dy[j] >= m or b+dy[i]+dy[j] < 0): # 불이랑 동시에 만나는 경우 pass
                        continue
                    if(M[a+dx[i]+dx[j]][b+dy[i]+dy[j]] == '*' ):
                        f = 1
                        break
                if f == 1:
                    continue
                mebfs.append((a+dx[i],b+dy[i],depth+1)) #####push
                visited[a+dx[i]][b+dx[i]] = 1
            if flag ==1:
                break
        
        if flag == 1:   #탈출성공!
            print(depth+1)
            break
        if not mebfs: ########## 더 이상 갈 곳이 없엉...fail
            print("IMPOSSIBLE")
            break      

        #print("firebfs",firebfs)
        while firebfs: ############## 불은 그냥 옮겨 붙기만 하면 된다.
            a,b,depth = firebfs.popleft()
            if depth > before2: 
                if bbatta2==0:
                    bbatta2 = bbatta2 + 1
                else:
                    firebfs.append((a,b,depth))
                    break
            before2 = depth
            for i in range(4):
                if( a+dx[i] >= n or a+dx[i] < 0 or b+dy[i] >= m or b+dy[i] < 0):
                    continue
                if(M[a+dx[i]][b+dy[i]] == '#' or M[a+dx[i]][b+dy[i]] == '*' or visited[a+dx[i]][b+dy[i]] == 1):
                    continue
                firebfs.append((a+dx[i],b+dy[i],depth+1))   
                M[a+dx[i]][b+dy[i]] = '*'
        #print("M" ,M)
        #print("firebfs",firebfs)