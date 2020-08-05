def solution(road, n):
    if n > 0:
        begin = end = 0
        zeroCnt = 1 if road[begin] == '0' else 0
    else:
        begin = end = road.find('1')
        zeroCnt = 0
        if begin == -1:
            return 0
    res = 1
    
    # begin을 1씩 늘려가면서 end (정상 도로의 마지막 idx)를 구함, 시간 복잡도 O(n)
    while True:
        # end 구하기
        while True:
            end += 1
            if end == len(road):
                end -= 1
                break
            zeroCnt += 1 if road[end] == '0' else 0
            if zeroCnt > n:
                end -= 1
                zeroCnt -= 1
                break
        
        # res 갱신
        if res < end - begin + 1:
            res = end - begin + 1
        
        # loop 탈출조건
        if end == len(road) - 1:
            break
        
        zeroCnt -= 1 if road[begin] == '0' else 0
        begin += 1
        if begin == len(road):
            break
        if begin > end:
            end = begin
            zeroCnt = 1 if road[begin] == '0' else 0
    
    return res

res = solution("001100111111110011"  , 7 )
print(res)