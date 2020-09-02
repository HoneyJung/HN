n = input("input n ")
s1 = input()

s1 = s1.strip("[]") ###########[] 없애기
print(s1)

list1 = s1.split(',')  ########### ',' 기준으로
print(list1)

s2 = input()

s2 = s2.strip("[]") ###########[] 없애기
print(s2)

list2 = s2.split(',')  ########### ',' 기준으로
print(list2)

mylist = list()

for i in range(0,int(n)):

    mylist.insert(i, bin(int(list1[i]) | int(list2[i]))) #### or 연산 후 이진수로 변환
    print(mylist[i])
    mylist[i] = mylist[i].replace('1','#')
    mylist[i] = mylist[i].replace('0b','')
    mylist[i] = mylist[i].replace('0',' ')
    mylist[i] = mylist[i].rjust(int(n),'0')
    
#    print(type(mylist[i]))
#    print(type('0b11'))
#    a = '0b11'.replace("0b11","#") 
#    print(a)
print(mylist)

