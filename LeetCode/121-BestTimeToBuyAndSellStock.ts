// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

var maxProfit = function(prices: number[]): number {
  let minimumPrice: number = prices[0]; //1
  let maximumProfit: number = 0; //5

  for (let i = 1; i < prices.length; i++) {
      let currentPrice: number = prices[i]; // 4

      if (currentPrice < minimumPrice) minimumPrice = currentPrice;
      if (maximumProfit < currentPrice - minimumPrice) maximumProfit = currentPrice - minimumPrice;
  }

  return maximumProfit;
};