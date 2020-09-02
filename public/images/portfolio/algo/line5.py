def solution(dataSource, tags):
    dataSource = sorted(dataSource, key = lambda x : x[0]) # 파일 이름 알파벳 순 정렬
    Count = [[0,dataSource[i][0]] for i in range(len(dataSource))] # 각 파일별로 count
    for i in range(len(dataSource)):
        for j in range(len(tags)):
            if tags[j] in dataSource[i]: # 테그가 들어있으면?
                Count[i][0] = Count[i][0] + 1
    Count = sorted(Count, key = lambda x : x[0],reverse = True) # Count에 따른 정렬
    ans = []
    c = 0 # pagination
    for i in range(len(Count)):
        if c == 10:
            break
        if Count[i][0] == 0:
            continue
        else:
            c = c + 1 # 하나 넣어줄때마다 +1
            ans.append(Count[i][1])
    #print(ans)
    return ans