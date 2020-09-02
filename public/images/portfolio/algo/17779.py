import sys
N = int(input())
Map = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
Sum = 0
for i in range(N):
    for j in range(N):
        Sum = Sum + Map[i][j] # 총합.


MM = 40000
for x in range(N):
    for y in range(N): 
        for d1 in range(1,N):
            for d2 in range(1,N):
                if x + d1 >= N or x + d2 >= N or y - d1 <0 or y + d2 >= N or x + d1 + d2 >= N or y - d1 + d2 < 0 or y - d1 + d2 >= N :
                    continue
                temp1 = 0
                temp2 = 0
                temp3 = 0
                temp4 = 0
                t = 0

                for i in range(0,x+d1-1):
                    if i < x-1:
                        #print("here")
                        for j in range(0,y):
                            temp1 = temp1 + Map[i][j]
                        #print(temp)
                    else:
                        for j in range(0,y-t-1):
                            temp1 = temp1 + Map[i][j]
                        t = t + 1
                        #print(temp)

                t = 0
                
                for i in range(0,x+d2):
                    if i < x:
                        for j in range(y,N):
                            temp2 = temp2 + Map[i][j]
                    else:
                        for j in range(y+1+t,N):
                            temp2 = temp2 + Map[i][j]
                        t = t + 1

                t = 0
                for i in range(x+d1-1,N):
                    if i >= x + d1 + d2:
                        for j in range(0,y-d1+d2-1):
                            temp3 = temp3 + Map[i][j]

                    else:
                        for j in range(0,y-d1-1+t):
                            temp3 = temp3 + Map[i][j]
                        t = t + 1
                        #print(temp)

                t = 0

                for i in range(x+d2,N):
                    if i >= x + d1 + d2:
                        #print("here")
                        for j in range(y+d2-d1-1,N):
                            temp4 = temp4 + Map[i][j]
                        #print(temp)
                    else:
                        for j in range(y+d2-1-t,N):
                            temp4 = temp4 + Map[i][j]
                        t = t + 1
                        #print(temp)
                arr = [temp1,temp2,temp3,temp4,Sum - (temp1+temp2+temp3+temp4)]
                # if x ==2 and y==3 and d1 ==1 and d2 ==2:
                #     print(arr)  
                Min = min(arr)
                Max = max(arr)
                if MM > Max-Min:
                    MM = Max-Min
                    ii = x
                    jj = y
                    dd = d1
                    ddd = d2
# print(ii,jj, dd,ddd)
print(MM)
# print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

temp = 0
Min = 100
Max = 0
x = 2
y = 3
d1 = 1
d2 = 2 
t = 0
temp2 = 0
for i in range(0,x+d2):
    if i < x-1:
        for j in range(y,N):
            temp2 = temp2 + Map[i][j]
    else:
        for j in range(y+t,N):
            temp2 = temp2 + Map[i][j]
        t = t + 1

#print(temp2)

