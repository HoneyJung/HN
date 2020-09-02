import sys
import collections
import copy
def calid(a,b,c,d,k): #############바뀐 id 구해주는 함수.

    if (k) < 100000000:  ########### 1번째가 0인경우.
        z = k
        z = '0'+str(z)
        
        #print("z",z)
        t1 = int(z[3*a+b])
        t2 = int(z[3*c+d])
        return k + pow(10,8-(3*a+b)) * (t2 - t1) + pow(10,8-(3*c+d)) * (t1 -t2)
    else:
        z = k
        z = str(z)
        #print("z",z)
        t1 = int(z[3*a+b])
        t2 = int(z[3*c+d])
            
        return k + pow(10,8-(3*a+b)) * (t2 - t1) + pow(10,8-(3*c+d)) * (t1 -t2)
    
'''def calid(a,b,c,d,k): #############바뀐 id 구해주는 함수.
    #print("calid" ,a,b,c,d,k)
    return int(k) + pow(10,8-(3*a+b)) * (calculate(c,d,k) - calculate(a,b,k))+ pow(10,8-(3*c+d)) * (calculate(a,b,k) -calculate(c,d,k))
def calculate(a,b,idid):
    if idid < 100000000:
        idid = '0' + str(idid) 
    kk = str(idid)
    return int(kk[3*a+b])
    #return int(idid / pow(10,8-(3*a+b))) %10
'''
ary = [[int(x) for x in sys.stdin.readline().split()] for _ in range(3)]
Q = collections.deque([])
Id = set([])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
###################### 0위치 찾아서 큐에 넣기 
mapid1 = 0
for i in range(3):  
    for j in range(3):
        if ary[i][j] == 0:
            p = i
            q = j
        mapid1 = mapid1 + pow(10,(8 - (3*i+j))) * ary[i][j]
Q.append((p,q,0,mapid1,0))###########
#if mapid1 < 100000000:
#    mapid1 = '0' + str(mapid1) 
Id.add(mapid1) #################문자열로 바꾸자.

if mapid1 == 123456780: ########첨부터 잘됐으면
    print("0")
    sys.exit(1)
else:
    while Q:########### BFS시작
        a,b,depth,mapid2,bef = Q.popleft()
        #bef = mapid2
        #print("info",a,b,depth,mapid2)
        #print("before",bef)
        bef = mapid2
        for i in range(4):
            if (a+dx[i] >= 3 or a+dx[i] < 0 or b+dy[i] >= 3 or b+dy[i] <0): ######범위 체크
                continue
            #print("calid" ,a+dx[i],b+dy[i],depth+1,mapid2)
            mapid = calid(a,b,a+dx[i],b+dy[i],mapid2)
            #print("after : ",mapid)
            if mapid in Id:
                continue
            elif mapid == 123456780:
                print(depth+1)
                sys.exit(1)
            else:
                Id.add(mapid)
                #print("calid" ,a+dx[i],b+dy[i],depth+1,mapid)
                Q.append((a+dx[i],b+dy[i],depth+1,mapid,bef))
    print("-1")


    
