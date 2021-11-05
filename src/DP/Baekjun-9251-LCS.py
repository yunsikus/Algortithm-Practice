S1 = input()
S2 = input()

# S1 = 'ACAYKP'
# S2 = 'CAPCAKA'

my_mat = [[0]*(len(S1)+1) for _ in range(len(S2)+1)]

for i in range(1, len(S2)+1):
    for j in range(1, len(S1)+1):
        if S1[j-1] == S2[i-1]:
            my_mat[i][j] = my_mat[i-1][j-1]+1
        else:
            my_mat[i][j] = max(my_mat[i-1][j], my_mat[i][j-1])

print(my_mat[-1][-1])