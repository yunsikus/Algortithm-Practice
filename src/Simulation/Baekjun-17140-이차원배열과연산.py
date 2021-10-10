from collections import Counter

r,c,k = map(int,input().split())
my_mat = [list(map(int, input().split())) for _ in range(3)]

def transpose(my_mat):
    new_mat =  [list(x) for x in zip(*my_mat)]
    return new_mat

# r연산
def row_c(my_mat):
    for i in range(len(my_mat)):
        my_mat[i].sort()
        c = Counter(my_mat[i]) # 1) 각 row에 차례로 접근하여 원소의 개수를 구함
        new_array = [x for x in c.items() if x[0] != 0] # 2) 0을 제외
        new_array.sort(key = lambda x: x[1]) # 3) 적게 등장하는 원소부터 등장하도록 정렬함 
        my_mat[i] = [y for x in new_array for y in x] # nested_list를 풀어줘야함 ex) [(2,1),(1,2)] -> [2,1,1,2]

    # 4) 최대 행길이를 찾고 나머지 행들을 0으로 채우기
    max_len = max([len(x) for x in my_mat])
    for i in range(len(my_mat)):
        if len(my_mat[i]) < max_len:
            my_mat[i] += [0]*(max_len - len(my_mat[i]))

    # 5) 행 또는 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지를 버림 
    my_mat = my_mat[:100]
    my_mat = [x[:100] for x in my_mat]

    return my_mat

# c연산
def col_c(my_mat):
    my_mat = transpose(my_mat)
    my_mat = row_c(my_mat)
    my_mat = transpose(my_mat)

    # 행 또는 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지는 버린다. 
    my_mat = my_mat[:100]
    my_mat = [x[:100] for x in my_mat]

    return my_mat

i = 0
while True:
    if len(my_mat) >= r and len(my_mat[0]) >= c:
        if my_mat[r-1][c-1] == k:
            print(i)
            break

    nrow = len(my_mat)
    ncol = len(my_mat[0])

    if nrow >= ncol:
        my_mat = row_c(my_mat)
    else:
        my_mat = col_c(my_mat)

    i += 1

    if i == 101:
        print(-1)
        break