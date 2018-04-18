from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
import requests

session = requests.Session()  # params = {'username': 'username', 'password': 'password'}
s = session.post("http://www.czce.com.cn/portal/index.htm")

print(s.cookies.get_dict())
print("-----------")
print("Going to profile page...")
# s = session.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")
# http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20171026/FutureDataDaily.xls
url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataTradeamt.htm'
s = session.get(url)
s.encoding = 'gbk' 
print(s.text)

import pandas as pd
df = pd.read_html(s.content, encoding='gbk')
# df.to_csv('test.csv')
# print(df)
for i, a_df in enumerate(df):
    print(a_df)
    a_df.to_csv(str(i)+'.csv', encoding='gbk')