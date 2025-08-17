#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.


prices=[7,1,5,3,6,4]


profit=0

mini=prices[0]

for i in range(len(prices)):
    cost=prices[i]-mini
    profit=max(profit,cost)
    mini=min(mini,prices[i])

print(profit)