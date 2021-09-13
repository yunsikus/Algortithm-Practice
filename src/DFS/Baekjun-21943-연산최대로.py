import sys
from itertools import permutations

max_v = -sys.maxsize

N = int(input())
my_list = list(map(int, input().split()))
P, Q = map(int, input().split())

def dfs(my_list, q, answer): # q개의 집합으로 분리
    global max_v
    if q == 1:
        if answer*sum(my_list) > max_v:
            max_v = answer*sum(my_list)
        return
    for i in range(1, len(my_list)-q+2):
        dfs(my_list[i:], q-1, answer*sum(my_list[:i]))

result = list(permutations(my_list,len(my_list)))
result = set(result)

for a in result:
    dfs(a,Q+1,1)

print(max_v)