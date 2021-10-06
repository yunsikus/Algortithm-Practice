import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

a,b = map(int, input().split())
my_mat = []
for _ in range(a):
    my_mat.append(list(map(lambda a: ord(a) - 65, input())))

alphabets = [False]*26
alphabets[my_mat[0][0]] = True
history = [[False]*b for _ in range(a)]

def dfs(n,x,y):
    global max_v
    if n > max_v:
        max_v = n

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<a) and (0<=ny<b):
            if not history[nx][ny]:
                if not alphabets[my_mat[nx][ny]]:
                    history[nx][ny] = True
                    alphabets[my_mat[nx][ny]] = True
                    dfs(n+1,nx,ny)
                    history[nx][ny] = False
                    alphabets[my_mat[nx][ny]] = False

max_v = -sys.maxsize
dfs(1,0,0)
print(max) 