r,c,t = map(int, input().split())
my_mat = [list(map(int, input().split())) for x in range(r)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(r):
    if my_mat[i][0] == -1:
        start = i+1
        break

def dust_move():
    move = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if my_mat[i][j] > 0:
                d = my_mat[i][j] // 5
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if (0<=nx<r) and (0<=ny<c):
                        if my_mat[nx][ny] != -1:
                            my_mat[i][j] -= d # 확산 시작 지역의 먼지를 차감
                            move[nx][ny] += d # 확산하는 먼지의 양을 move에 기록
    for i in range(r): 
        for j in range(c):
            my_mat[i][j] += move[i][j]

def cleanAir(start, dir): # start:시작행, dir:1 -> 반시계, dir:-1 -> 시계
    if dir == 1:
        for i in range(start-2,0,-1): # 아래
            my_mat[i][0] = my_mat[i-1][0]
        for i in range(0,c-1,1): # 왼
            my_mat[0][i] = my_mat[0][i+1]
        for i in range(0,start,1): # 위
            my_mat[i][c-1] = my_mat[i+1][c-1]
        for i in range(c-1,1,-1): # 오른
            my_mat[start-1][i] = my_mat[start-1][i-1]

        my_mat[start-1][1] = 0

    else:
        for i in range(start+1,r-1,1): # 위
            my_mat[i][0] = my_mat[i+1][0]
        for i in range(0,c-1,1): # 왼
            my_mat[r-1][i] = my_mat[r-1][i+1] 
        for i in range(r-1,start,-1): # 아래
            my_mat[i][c-1] = my_mat[i-1][c-1]
        for i in range(c-1,0,-1): # 오른
            my_mat[start][i] = my_mat[start][i-1]

        my_mat[start][1] = 0

i = 0
while True:
    dust_move()
    cleanAir(start,1)
    cleanAir(start,-1)
    i+=1
    if i == t:
        break

total_sum = sum(map(sum,my_mat)) + 2
print(total_sum)
