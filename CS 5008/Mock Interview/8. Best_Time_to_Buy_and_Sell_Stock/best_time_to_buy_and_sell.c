// time complexity = O(1)
// space complexity - O(1)


int maxProfit(int* prices, int pricesSize)
{
    // profit is the maximum profit we can gain so far
    // buy is the minimum price we have seen so far
    int profit = 0, buy = INT_MAX;
    
    // Loop through the array of prices
    for (int i = 0; i < pricesSize; i++) {
        // Update buy to be the minimum of the previous buy and the current price
        buy = fmin(buy, prices[i]);
        // Update the profit to be the maximum of the previous profit and the current profit
        profit = fmax(profit, prices[i] - buy);
    }
    
    // Return the profit
    return profit;
}