def maxProfit(prices):
    # maxProfit = 0
    # left, right = 0, 1

    # while right<len(prices):
    #     if prices[right]>prices[left]:
    #         currProfit = prices[right]-prices[left]
    #         maxProfit= max(currProfit, maxProfit)
    #     else:
    #         left = right
    #     right+=1

    # return maxProfit
    maxProfit = 0
    minPrice = prices[0]

    for price in prices:
        if price-minPrice > maxProfit:
            maxProfit = price-minPrice
        if price < minPrice:
            minPrice = price
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([2, 4, 1]))
