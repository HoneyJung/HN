import sys

Map = [list(sys.stdin.readline().strip('\n')) for _ in range(4)]
# Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
# a = [list(map(int, input().split())) for _ in range(n)]
N = int(input())
#print("Map :" , Map)  
#print("N : ", N)
for i in range(N):
    x = [0 for _ in range(4)] 
    a,b = map(int,input().split())
    x[a-1] = b
    for i in range(a-1,3):
        if Map[i][2] == Map[i+1][6]:
            break
        else:
            x[i+1] = x[i] * -1  
            
    for i in range(a-1,0,-1):
        if Map[i][6] == Map[i-1][2]:
            break
        else:
            x[i-1] = x[i] * -1
    #print(x)

    for i in range(4):
        if x[i] == 1:
            temp = Map[i][7]
            for j in range(7,0,-1):
                Map[i][j] = Map[i][j-1]
            Map[i][0] = temp
        elif x[i] == -1:
            temp = Map[i][0]
            for j in range(7):
                Map[i][j] = Map[i][j+1]
            Map[i][7]= temp
        else:
            continue
    #print("Map :",Map)
su = 0
for i in range(4):
    su = su + pow(2,i) * int(Map[i][0])
print(su)