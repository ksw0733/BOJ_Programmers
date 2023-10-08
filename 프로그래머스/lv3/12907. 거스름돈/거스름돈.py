def solution(n, money):
    dp = [0] * (n + 1)
    
    for typ in money:
        dp[typ] += 1
        for price in range(typ + 1, n + 1):
            dp[price] += dp[price - typ] 
            
    return dp[-1] % 1000000007