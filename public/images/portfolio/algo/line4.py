snapshots =[
  ["ACCOUNT2", "100"], 
  ["ACCOUNT1", "150"]
]
transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"], 
  ["1", "SAVE", "ACCOUNT2", "100"], 
  ["4", "SAVE", "ACCOUNT3", "500"], 
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]
account = {}
for i in range(len(snapshots)):
    account[snapshots[i][0]] = int(snapshots[i][1])
#print(account) 
visit = [0 for _ in range(100000)]
for i in range(len(transactions)):
    ID, SW, to, money = transactions[i]
    money = int(money) #문자열 -> int
    ID = int(ID)
    #print(ID)
    if visit[ID] == 1: # 중복제거
        continue
    else:
        visit[ID] = 1 # 중복체크
        if to in account.keys(): # 계좌정보에 있는지
            if SW == 'SAVE':
                account[to] = account[to] + money
            elif SW == 'WITHDRAW':
                account[to] = account[to] - money
        else: # 계좌정보에 없던 거면 추가해주기 + 돈 계산
            account[to] = money
print(account)
ans = [] #[[] for _ in range(len(account))]
for i in account.items(): # list로 바꾸기 다시
    print(i)
    ans.append([i[0],str(i[1])])
ans = sorted(ans, key = lambda x : x[0]) # Count에 따른 정렬

print(ans)
