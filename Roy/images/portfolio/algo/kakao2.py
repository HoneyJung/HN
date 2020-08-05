come = input("input : ")
b = list()
flag1=0
flag2=0
flag3=0
x=''
y=''
z=''
a = come.split('T')
if '*' in a[1]:
    z = a[1].strip('*')
    flag1 = 1 ############# 젤 마지막에 * 있으면 flag1 = 1
if '#' in a[1]:
    z = a[1].strip('#')
    flag1 = 2 ######### 젤 마지막에 # 있으면 flag2 = 2

print(a)

come = a[0]

a = come.split('D')
if '*' in a[1]:
    flag2 = 1
    y = a[1].strip('*')

if '#' in a[1]:
    flag2 = 2 
    y = a[1].strip('#')
print(a)
come = a[0]

a = come.split('S')
if '*' in a[1]:
    x = a[1].strip('*')
    flag3 = 1
if '#' in a[1]: 
    x = a[1].strip('#')
    flag3 = 2



print(a)
print(x)
print(y)
print(z)