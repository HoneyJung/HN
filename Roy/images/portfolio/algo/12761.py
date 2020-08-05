import sys
A, B, N, M = map(int,sys.stdin.readline().split())

#print (A,B,N,M)
doldary = []
dolstep = [0]*100000
dx = [A,B,-A,-B,+1,-1,'a','b']
#print (dx)
doldary.append(N)


while doldary:
    #print(doldary)
    x = doldary.pop(0)
        
    for i in range(8):
        if dx[i] == 'a':
            xx = x * A
        elif dx[i] == 'b':
            xx = x * B    
        else:
            xx = x + dx[i]
           
        if xx >= 0 and xx <= 100000:
            if dolstep[xx] == 0:
                if xx == M:
                    print(dolstep[x]+1)
                    sys.exit()
                doldary.append(xx)
                dolstep[xx]=dolstep[x]+1
            