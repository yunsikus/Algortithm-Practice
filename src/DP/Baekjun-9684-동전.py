T = int(input())
for i in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    dp = [[0]*(M+1) for _ in range(len(coin)+1)]

    for i in range(len(coin)+1):
        dp[i][0] = 1

    for i in range(1, len(coin)+1): 
        for j in range(1, M+1):
            if j >= coin[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i][j-coin[i-1]] 
            else:
                dp[i][j] = dp[i-1][j]
    
    print(dp[-1][-1]) 