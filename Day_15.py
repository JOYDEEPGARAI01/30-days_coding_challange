#Minimum number of coins for a given amount
n, amount = map(int, input().split())
coins = list(map(int, input().split()))

denom = [float('inf')] * (amount + 1)
denom[0] = 0

for coin in coins:
    for i in range(coin, amount + 1):
        denom[i] = min(denom[i], denom[i - coin] + 1)

if denom[amount] == float('inf'):
    print(-1)
else:
    print(denom[amount])
