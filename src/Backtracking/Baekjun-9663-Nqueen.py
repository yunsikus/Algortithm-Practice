n = int(input())

answer = 0
col = set()
diagonal1 = set()
diagonal2 = set()

def dfs(n,row,col,diagonal1, diagonal2):
    global answer
    if row==n:
        answer += 1
        return
    
    for hubo in range(n): # 매 row마다 가능한 col을 탐색
        if (hubo in col) or (row+hubo in diagonal1) or (row-hubo in diagonal2):
            continue

        col.add(hubo)
        diagonal1.add(row+hubo)
        diagonal2.add(row-hubo)

        dfs(n,row+1,col,diagonal1,diagonal2)

        col.remove(hubo)
        diagonal1.remove(row+hubo)
        diagonal2.remove(row-hubo)

def solution(n):
    dfs(n, 0, col, diagonal1, diagonal2)
    return answer

print(solution(n))