# encoding=utf-8

import time
from lib.api.okex.account_api import AccountApi
from lib.api.okex.spot_api import SpotApi
from lib.api.okex.index_api import IndexApi

# instrument_id = 'BTC-USDT'
# kline = SpotApi.get_kline(instrument_id=instrument_id)
# kline = list(reversed(kline))
# for item in kline:
#     print(item)


# 资金账户API
# 账户信息
# result = AccountApi.get_wallet()

# result = AccountApi.get_currencies()
# result = AccountApi.get_coin_fee('btc')
# 资金划转
# 资金账户:6 -> 币币:1
# currency = 'USDT'
# amount = '10'
# account_from = '6'
# account_to = '1'
# result = AccountApi.coin_transfer(currency=currency, amount=amount, account_from=account_from, account_to=account_to,
#                                   sub_account='', instrument_id='', to_instrument_id='')

###################### 币币API ######################
# 账户信息
# result = SpotApi.get_account_info()
# 指定币种的账户信息
# result = SpotApi.get_coin_account_info('USDT')
# for item in result:
#     print(item)
# exit()
# 币对信息
# result = SpotApi.get_coin_info('USDT')
# 交易手续费费率
# result = SpotApi.get_trade_fee()
################ 下单 ################
# 买入
# instrument_id = 'EOS-USDT'
# side = 'buy'
# 限价单
price = '20'
size = '1'
# result = SpotApi.take_order(instrument_id=instrument_id, side=side, price=price, size=size)
######################################
# 全部卖出
# 获取币币账户信息
# result = SpotApi.get_account_info()
# 获取未成交订单
# result = SpotApi.get_orders_pending('EOS-USDT')

currency_info = SpotApi.get_coin_account_info('EOS')

instrument_id = 'EOS-USDT'
side = 'sell'
# 市价单
size = str(currency_info['available'])
notional = '5'
result = SpotApi.take_order(instrument_id=instrument_id, side=side, size=size, notional=notional)

# 撤销挂单
# result = SpotApi.revoke_order('EOS-USDT', '4438881476487168')


################### 指数API ##################
# 公共-获取指数成分
# result = IndexApi.get_index_constituents('BTC-USD')


# for item in result:
#     print(item)
print(result)
