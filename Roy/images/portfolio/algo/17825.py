import sys
ary = list(map(int,sys.stdin.readline().split()))
Map = [ i*2  for i in range(85)]
#Map2 = [0 for _ in range(31)]
a = 0
b = 0
c = 0
d = 0
for i in range(9):
    Map[21+i] = 0
for i in range(12):
    Map[38+i] = 0
for i in range(13):
    Map[57+i] = 0
for i in range(7):
    Map[78+i] = 0

Map[30] = 10
Map[31] = 13
Map[32] = 16
Map[33] = 19
Map[34] = 25
Map[35] = 30
Map[36] = 35
Map[37] = 40
Map[50] = 20
Map[51] = 22
Map[52] = 24
Map[53] = 25
Map[54] = 30
Map[55] = 35
Map[56] = 40
Map[70] = 30
Map[71] = 28
Map[72] = 27
Map[73] = 26
Map[74] = 25
Map[75] = 30
Map[76] = 35
Map[77] = 40
score = 0
temp = 0
def dfs(w,a,b,c,d,temp): # w번째 턴
    global score
    horse = [a,b,c,d]
    for i in range(4): # i는 움직일 말
        #print(i,w,ary)
        temphorse = horse[i] + ary[w] # 옮길 곳.
        #temp = temp + Map[horse[i]] # 스코어 더하기
        
        if temphorse == 5:
            temphorse = 30
        if temphorse == 10:
            temphorse = 50
        if temphorse == 15:
            temphorse = 70

        if temphorse == 37:
            temphorse = 20
        if temphorse == 56:
            temphorse = 20
        if temphorse == 77:
            temphorse = 20
        if temphorse == 34 or temphorse == 53:
            temphorse = 74
        if temphorse == 35 or temphorse == 54:
            temphorse = 75
        if temphorse == 36 or temphorse == 55:
            temphorse = 76            
            
        
        if horse[i] == 40:
            #print("이미 나간거야",horse,i,ary[w])
            continue

        if temphorse in horse and temphorse != 40: # 이미 있으면
            #print(horse,horse[i] + ary[w])
            #print("here")
            #print("이미 occupied",horse,i,ary[w])
            continue
        
        if (horse[i] + ary[w] > 37 and horse[i] + ary[w] < 50) or (horse[i] + ary[w] > 56 and horse[i] + ary[w] < 70) or (horse[i] + ary[w] > 77 and horse[i] + ary[w] < 90 ) or (horse[i] + ary[w] > 20 and horse[i] + ary[w] < 30): # 넘어가면.
            #print(horse,horse[i] + ary[w])
            #horse[i] = 40 # 넘어가면 그 말은 끝
            if w != len(ary)-1:
                if i == 0:
                    dfs(w+1,40,horse[1],horse[2],horse[3],temp)
                    #print("위치 : ",40,horse[1],horse[2],horse[3])
                    
                if i == 1:
                    dfs(w+1,horse[0],40,horse[2],horse[3],temp)
                    #print("위치 : ",horse[0],40,horse[2],horse[3])
                    
                if i == 2:
                    dfs(w+1,horse[0],horse[1],40,horse[3],temp)
                    #print("위치 : ",horse[0],horse[1],40,horse[3])
                    
                if i == 3:
                    dfs(w+1,horse[0],horse[1],horse[2],40,temp)
                    #print("위치 : ",horse[0],horse[1],horse[2],40)
                    
                continue      

        if w == len(ary)-1:
            if temp + Map[horse[i] + ary[w]] > score:
                score = temp + Map[horse[i] + ary[w]]
           
            # if temp + Map[horse[i] + ary[w]] > 200:
            #     print("위치 : ", a,b,c,d)
            #     print(i,ary[w])
            #     print("finish")
            #     print("temp : ",temp + Map[horse[i] + ary[w]])
            #print("score : ",score)
            continue



        if i == 0:
            #print ("위치 : ",temphorse,b,c,d)
            dfs(w+1,temphorse,b,c,d,temp + Map[temphorse])
        if i == 1:
            #print ("위치 : ",a,temphorse,c,d)            
            dfs(w+1,a,temphorse,c,d,temp + Map[temphorse])
        if i == 2:
            #print ("위치 : ",a,b,temphorse,d)
            dfs(w+1,a,b,temphorse,d,temp + Map[temphorse])
        if i == 3:
            #print ("위치 : ",a,b,c,temphorse)
            dfs(w+1,a,b,c,temphorse,temp + Map[temphorse])
        
        # print("temp : ",temp)
        # print(Map[horse[i]])



dfs(0,a,b,c,d,temp)
print(score)