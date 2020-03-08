# Huobi_Futures_Bullish_Bot
## Introduction
This strategy is applied to huobi.com futures contracts aiming to achieve the maximum wealth in a bullish trend. Futures contracts in huobi.com is not traded by stable coins just like in Bitmex. So if you buy long at some point, your profit comes from both coin value and leverage. But when the price goes up, you will find your real leverage go down which will definitely limit your profit. To solve this issue is the key point of this strategy.
### Example
if you use 1 BTC to open buy long position at 8000 with *10 real leverage without this strategy, you can get 1.25 BTC if you close at 10000. But with this strategy you can get 7.56 BTC. This is really massive difference!
## How to use it?
1. Set up a risk level you can handle.
  -"real_leverage" is the param for you to set up based on your risk management opinion. The strategy will always increase your position to your "real_leverage" base on my algorithm.
2. Test before Send.
  - Test in the terminal before you uncomment the "sendOrder"
  - When you are testing, you can see your expected gains.
## Description
1. “ori_cash” is the coin you want to trade as margin
2. "multi" is the price growth percentage you want to reinvest
3. "leverage" is the leverage you set on the exchange
4. "real_leverage" is leverage you want to have
5. "number" is the orders you want to send totally
### Attention: 
- This strategy is not helping you to make trading decision, buy help you to get the maximum money based on your judgement.
- This strategy should be used ONLY when you think there will be a upward trend.
