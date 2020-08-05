import sys
N = int(input())
M = list(sys.stdin.readline())

if N==1:
    q = int(M[0])
result = []
def per(l):
    if len(l) == 1:
        return 1
    for i in range(len(l)):
        if l[:i] + l[i+1:] in result:
            continue
        result.append(l[:i] + l[i+1:])
        per(l[:i]+l[i+1:])

L = [i for i in range((len(M)-1)//2+1)]
s = (len(M)-1)//2+1
#print(L)
#print(M)
result.append(L)
per(L)


def cal(a,b):
    temp = M[2*a:2*b+1]
    #print("temp :", temp)
    for i in range(1,len(temp),2): 
        if temp[1] == '+':
            res = int(temp[0]) + int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        if temp[1] == '*':
            res = int(temp[0]) * int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        if temp[1] == '-':
            res = int(temp[0]) - int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        #print(temp)
    return temp
#print(cal(0,3))

def cal2(a,b,QQQ):
    temp = QQQ[2*a:2*b+1]
    #print("temp :", temp)
    for i in range(1,len(temp),2):
        if temp[1] == '+':
            res = int(temp[0]) + int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        if temp[1] == '*':
            res = int(temp[0]) * int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        if temp[1] == '-':
            res = int(temp[0]) - int(temp[2])
            temp[0] = res
            if len(temp) == 3:
                temp = temp[:1]
                break
            temp[1:] = temp[3:]
        #print(temp)
    return temp
#print(cal(0,3))
#for i in range(len(result)):
   # if result[i] == [1,9]:
        #print("tlqkf")
        #print(result[i])
#print("----------------")
eee = []
for i in range(len(result)):
    flag = 0 
    if i >= len(result):
        break
    case = result[i]
    if len(case) % 2 == 1:
        continue
    for j in range(0,len(case),2):
        if case[j] + 1 != case[j+1]:
            flag = 1
    if flag == 1:
        continue
    eee.append(case)
result = eee
#print("-----------------")
#print(result)
#result.remove([1,9])
# if [1,9] in result:
#     print("there")
Max = -100000
for case in (result):
    QQ = M[:]
    #print(case)
    if len(case) % 2 == 0:
        for i in range(0,len(case),2):
            for j in range(case[i]*2,case[i+1]*2+1):
                QQ[j] = (cal(case[i],case[i+1]))[0]
    else:
        continue
    #print(case)
    #print("QQ : ",QQ)
    QQQ = []
    before = '.'
    for i in range(len(QQ)-1):
        if before == QQ[i]:
            continue
        QQQ.append(QQ[i])
        before = QQ[i]
    #print(QQQ)
    ans=cal2(0,len(QQQ)//2,QQQ)[0]
    #if ans == 32:
        #print(case)
        #print(ans)
    if Max < ans:
        Max = ans
if N==1:
    print(q)
else:
    print(Max)
