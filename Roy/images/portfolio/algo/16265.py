import sys
import collections
import copy
import itertools
N,M,K = map(int, input().split())
add = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
Map = [ [ [] for _ in range(N) ] for _ in range(N)]
remain = [[5]*N for _ in range(N)]
#print ("add : ",add)
#print ("remain : ",remain)

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    Map[a-1][b-1].append(c)
#print("Map : ",Map) 
for fuc in range(K): # K번 반복한다.
    for i in range(N):
        for j in range(N):
            temp = []
            temp1 = 0
            while Map[i][j]:
                age = Map[i][j].pop()
                if age <= remain[i][j]:
                    remain[i][j] = remain[i][j] - age
                    temp.append(age+1)
                else: # 여름  
                    age = int(age/2)
                    temp1 = temp1 + age
            temp.reverse()
            Map[i][j]=temp
            #########
            remain[i][j] = remain[i][j] + temp1                
    ##############################################################3
    
    for i in range(N): # 가을 
        for j in range(N):
            if Map[i][j]: # 나무가 있다면 !?
                for age in Map[i][j]:
                    if age % 5 == 0:
                        for ii in range(8):
                            iii = i+dx[ii]
                            jjj = j+dy[ii]
                            if 0<=iii<N and 0<=jjj<N:
                                Map[iii][jjj].extend([1])
    for i in range(N): # 겨울.
        for j in range(N):
            remain[i][j] = remain[i][j] + add[i][j]
    #print("fuc")
    #for i in range(N):
    #   print(Map[i])
count = 0
for i in range(N):
    for j in range(N):
        while Map[i][j]:
            temp = Map[i][j].pop()
            count = count+1

print(count)
                #######################################################
                
                

                        