import sys

M,N = map(int,(input().split()))
r,c,Dir = map(int,(input().split()))
Map = [[0 for _ in range(M)] for _ in range(N)]
Map = [input().split() for _ in range(M)]

# print(M,N)
#print(r,c,Dir)
# print(Map)
count = 1
while(1):
    Map[r][c] = 2 # 청소하고 ! 2번임!
    #print("r,c : ",r,c)
    #print("Dir : ",Dir%4)
    flag = 0 
    for i in range(4):
        Dir = Dir - 1
        
        if Dir % 4 == 0: # 결국 위로 보게 되면!
            ########### 넘어가거나 청소 못하는 곳이면
            if r-1 < 0:
                continue
            if Map[r-1][c] == '1' or Map[r-1][c] == 2:
                continue
            else: # 비어있으면!
                Map[r-1][c] = 2
                r = r -1
                count = count + 1 
                Dir = 0
                flag = 1 
                break
        if Dir % 4 == 1: # 동쪽
            if c + 1 >= N:
                continue
            if Map[r][c+1] == '1' or Map[r][c+1] == 2:
                continue
            else: # 비어있으면!
                Map[r][c + 1] = 2
                c = c + 1 
                Dir = 1
                count = count + 1
                flag = 1 
                break
        if Dir % 4 == 2: # 결국 아래 보게 되면!
            if r+1 >= M:
                continue
            if Map[r+1][c] == '1' or Map[r+1][c] == 2:
                continue
            else: # 비어있으면!
                Map[r+1][c] = 2
                r = r +1
                flag = 1 
                count = count + 1
                Dir = 2
                break    
        if Dir % 4  == 3: # 결국 서쪽!
            if c - 1 < 0 :
                continue
            if Map[r][c-1] == '1' or Map[r][c-1] == 2:
                continue
            else: # 비어있으면!
                Map[r][c-1] = 2
                c = c - 1
                count = count + 1
                flag = 1 
                Dir = 3
                break    
        

    if flag == 0: # 4방향 모두 청소할 수 없으면
        #print("i : ")
        #print("Dir : ",Dir%4) 
        if r+1 < M and Dir % 4 == 0 and Map[r+1][c] == 2:
            if  Map[r+1][c] == 2:
                r = r + 1
                continue
        elif c-1 >= 0 and Dir % 4 == 1 and Map[r][c-1] == 2:
            if Map[r][c-1] == 2:
                c = c - 1
                continue
        elif r-1 >= 0  and Dir % 4 == 2 and Map[r-1][c] == 2:
            if Map[r-1][c] == 2:
                r = r - 1
                continue
        elif c+1 < N and Dir % 4 == 3 and Map[r][c+1] == 2:
            
            c = c + 1
            continue
        else:
            #print("break")
            break
print(count)
