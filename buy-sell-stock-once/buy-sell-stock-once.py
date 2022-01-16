def maximun_profit_on2 (low_prices, high_prices, starting_prices):
    max_profit = 0
    for i in range(len(starting_prices)):
        for j in range(len(starting_prices)):
            if (starting_prices[j] - starting_prices[i]) > max_profit:
                max_profit = starting_prices[j] - starting_prices[i]
    return max_profit

def maximun_profit_on(low_prices, high_prices, starting_prices):
    max_profit = 0
    min_price_so_far = float('inf')
    for price in starting_prices:
        max_price_sell_today = price - min_price_so_far
        max_profit = max(max_price_sell_today, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

def main():
    L = [1,2,5,4,4,4,3,2,6,4]
    H = [5,4,10,6,7,5,8,9,8,10]
    S = [2,2,6,5,4,4,6,3,7,7]
    print(maximun_profit_on2(L, H, S))
    print(maximun_profit_on(L, H, S))

if __name__ == '__main__':
    main()