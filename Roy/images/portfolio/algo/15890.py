import sys
N, L = map(int, input().split())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
Map2 = [[0 for _ in range(N)] for _ in range(N)]
flag = [[0 for _ in range(N)] for _ in range(N)]


count = 0
for i in range(N):
    temp = 1 # 같은 높이 유지된 길이
    flag2 = 0
    for j in range(N):
        if j+1 >= N:
            break
        elif Map[i][j] == Map[i][j+1]: # same height
            temp = temp + 1
            continue
        
        elif Map[i][j] + 1 == Map[i][j+1]: # 1 higher
            if temp < L or flag[i][j-L+1] == 1: # 안되면!
                #print("here")
                break
            else: # 설치
                temp = 1
                for k in range(L): # 설치했다고 flag 변경 ! 
                    flag[i][j-k] = 1
                continue        

        elif Map[i][j] == Map[i][j+1] + 1: # 1 lower
            if j+L >= N:# 넘어갈 경우.
                break
            flag[i][j+1] = 1
            for k in range(L-1):
                if Map[i][j+1 + k+1] == Map[i][j+1]:
                    flag[i][j+1 + k+1] = 1
                else:
                    flag2 = 1
                    break
            if flag2 == 1:
                break
            j = j + L    

        else:
            break
    
    #print("j : " ,j)
    if j == N-1:
        count = count + 1

#print("//////////////////////////\n")
for i in range(N):
    #print("\n")
    for j in range(N):
        Map2[i][j] = Map[j][i]
        #print(Map2[i][j])
flag = [[0 for _ in range(N)] for _ in range(N)]


for i in range(N):
    temp = 1 # 같은 높이 유지된 길이
    flag2 = 0
    for j in range(N):
        if j+1 >= N:
            break
        elif Map2[i][j] == Map2[i][j+1]: # same height
            temp = temp + 1
            continue
        
        elif Map2[i][j] + 1 == Map2[i][j+1]: # 1 higher
            if temp < L or flag[i][j-L+1] == 1: # 안되면!
                #print("here")
                break
            else: # 설치
                temp = 1
                for k in range(L): # 설치했다고 flag 변경 ! 
                    flag[i][j-k] = 1
                continue        

        elif Map2[i][j] == Map2[i][j+1] + 1: # 1 lower
            if j+L >= N:# 넘어갈 경우.
                break
            flag[i][j+1] = 1
            for k in range(L-1):
                if Map2[i][j+1 + k+1] == Map2[i][j+1]:
                    flag[i][j+1 + k+1] = 1
                else:
                    flag2 = 1
                    break
            if flag2 == 1:
                break
            j = j + L    

        else:
            break
    
    #print("j : " ,j)
    if j == N-1:
        count = count + 1


print(count)
