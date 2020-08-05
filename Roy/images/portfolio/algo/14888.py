import sys
import collections
import copy
N = int(input())
number = [int(x) for x in sys.stdin.readline().split()]
deq = collections.deque([])
deq1 = collections.deque([])
a,b,c,d = sys.stdin.readline().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
'''
if (a)!=0:
    deq.append([0])
if (b)!=0:
    deq.append([1])
if (c)!=0:
    deq.append([2])
if (d)!=0:
    deq.append([3])
'''
#print(number)
#print(a,b,c,d)

def per(a,b,c,d,x,depth): ###### 순열 -> 하나짜리부터 a+b+c+d개 까지.
    t = a+b+c+d
    #print(depth)
    if t == 0:
        deq.append(x)
        return
    
    if a>0:
        xx = x+[0]
        per(a-1,b,c,d,xx,depth+1)
    if b>0:
        xx = x+[1]
        per(a,b-1,c,d,xx,depth+1)
        t=t-b
    if c>0:
        xx = x+[2]
        per(a,b,c-1,d,xx,depth+1)
        t=t-c
    if d>0:
        xx = x+[3]
        per(a,b,c,d-1,xx,depth+1)
        t=t-d
#print(a,b,c,d)

per(a,b,c,d,[],0)
#print(deq)
#print(a,b,c,d)
Min = 10000000000
Max = -1000000000

while deq:
    i = 0
    total = number[i]
    i = i + 1 
    x = deq.popleft()
    while x:
        y = x.pop(0)
        if y ==0:
            total = total + number[i]
        if y ==1:
            total = total - number[i]
        if y ==2:
            total = total * number[i]
        if y ==3:
            if total < 0:
                total = total*(-1)
                total = total / number[i]
                total = int(total) * (-1)
            else:
                total = total / number[i]
                total = int(total)
        i = i+1

    if Min > total:
        Min = total
    if Max <total:
        Max = total
print(Max)
print(Min)