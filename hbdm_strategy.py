#!/usr/bin/env python
# encoding: utf-8
'''
@author: Justin Fu
@contact: justin_jingxuan_fu@163.com
@time: 07/03/2020 17:01
'''

from hbdm_tools import HuobiDM
import math
import time

#### input huobi dm url
# URL = 'https://api.hbdm.com'
URL = 'https://api.btcgateway.pro'

### input your api

ACCESS_KEY = ''
SECRET_KEY = ''

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

# ==============================  parameters  =================================
ori_cash = 1  # margin
multi = 0.005  # percentage range to increase position
leverage = 20  # nominal leverage
real_leverage = 5  # planned real leverage
number = 10  # maximum number of trigger order
open_price = 10000  # start price to set orders
close_price = 20000  # end price
symbol = 'BTC'      # coin symbol
contract_code = 'BTC200327' # contract code
contract_value = 100    # usd per contract
contract_type = 'quarter'
above_price = 'ge'     # open trigger order above the price
below_price = 'le'    # open trigger order below the price
# ===========================================================================
account_info = dm.get_contract_account_info(symbol)
balance = account_info['data'][0]['margin_balance']
# print(account_info)
print(symbol, 'Account Balance： ', round(balance, 3))
position = dm.get_contract_position_info(symbol)['data']
print('%s Position： '%symbol, position)


if not position:
    print("current position is none, no order will be pushed")

elif position[0]['direction'] == 'sell':
    print('current short position, no order will be pushed')

else:
    get_position = position[0]['volume']
    print('current position： ', int(get_position))
    get_cost = position[0]['cost_open']
    print('average price： ', round(get_cost, 2))
    get_profit_un = position[0]['profit_unreal']
    print('unrealised profit： ', round(get_profit_un, 3))
    expected_growth = round(close_price / open_price - 1, 4)
    print('expected growth', round(expected_growth, 2) * 100, '%')
    print('long open price：', open_price)
    total_available = int(get_cost * ori_cash * real_leverage / contract_value)
    print('total_available: ', total_available)
    expected_cash = ori_cash * (math.pow(1 + multi + multi * (real_leverage - 1),
                                         round(math.log(1 + expected_growth, multi + 1), 2)) - 1)
    print('expected gain：', round(expected_cash, 6))
    print('================================')
    for i in range(0, number):
        price = round(open_price * math.pow((1 + multi), i), 2)
        print('order%dprice: ' % i, price)
        a = round(math.log(price / open_price, (1 + multi)), 2)
        b = 1 + multi + multi * (real_leverage - 1)
        c = math.pow(b, a)
        new_cash = round(ori_cash * c, 6)
        print('new cash: ', new_cash)
        new_total_available = int(price * new_cash * real_leverage / contract_value)
        qty = max(
            min(int(new_total_available - total_available),
                int(new_total_available - int(get_position))),
            0)
        total_available = new_total_available
        print('order%dcontracts：' % i, qty)
        print('new total: ', total_available)
        print('================================')

        ###     uncommont the following if you are ready to execute the strategy
        
        # sendOrder = dm.send_plan_order(symbol=symbol, contract_type=contract_type, contract_code=contract_code,
        #                                trigger_type=above_price,trigger_price=price, order_price_type='optimal_5',
        #                                order_price=price , volume=qty, direction='buy',
        #                                offset='open', lever_rate=leverage)
        # print(sendOrder)

        time.sleep(0.5)