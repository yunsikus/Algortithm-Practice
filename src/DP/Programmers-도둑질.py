def solution(money):
    d = [[0,0],[0,0],[money[0],0]]
    for i in range(3, len(money)+3):
        if i-2 == len(money):
            break
        a = max(d[i-2][0] + money[i-2], d[i-1][0])
        b = max(d[i-2][1] + money[i-2], d[i-1][1])
        d.append([a,b])
        
    return max(d[-2][0], d[-1][1])