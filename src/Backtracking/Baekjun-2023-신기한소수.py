import math

N = int(input())

# 제곱근까지만 보고 소수를 판별하는 함수
def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def dfs(n, num):
    if n == N:
        print(num)
        return
    for i in range(10):
        if is_prime_number(num*10+i): # 가능한 경우만 탐색
            dfs(n+1, num*10+i)

for num in [2,3,5,7]:
    dfs(1,num)  