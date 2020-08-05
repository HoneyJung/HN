import sys
import collections
N,K,D = map(int,sys.stdin.readline().split())
M = []
for i in range(K):
    a,b,c = map(int,sys.stdin.readline().split())
    M.append([a,b,c])

#print(M)
start = 0
end = N
mid = int(N//2)
#tempd = D
while 1:
    count = 0
    #print(start,mid,end)
    if start == mid:
        print(end)
        break
    if mid == end:
        print(start)
        break
    for i in range(len(M)):
        if M[i][0] < mid:
            count = count + (min(M[i][1],mid) - M[i][0]) // M[i][2] + 1
        elif M[i][0] == mid:
            count = count + 1
    if count >= D:
        end = mid
        mid = int((end + start) // 2)
        #print("front")
    else:
        #print("back")
        start = mid
        mid = int((end + start) // 2)
    #print(count)
#print(int(mid))
