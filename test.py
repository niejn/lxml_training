from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
import requests

session = requests.Session()  # params = {'username': 'username', 'password': 'password'}
root_html = 'http://www.czce.com.cn/portal/index.htm'
root_html = 'http://www.czce.com.cn/portal/index.htm'
s = session.post(root_html)
s = session.post('http://www.czce.com.cn/portal/jysj/qhjysj/ccpm/A09112003index_1.htm')

print(s.cookies.get_dict())
print("-----------")
# print("Going to profile page...")
# s = session.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")
# http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20171026/FutureDataDaily.xls
# http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataHolding.htm
url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataHolding.htm'
s = session.get(url)
s.encoding = 'gbk'
print(s.text)

from lxml import etree
from io import StringIO, BytesIO

string = "<p><code>git clone https://github.com/AlexeyAB/darknet.git</code></p>"
parser = etree.HTMLParser()
root = etree.fromstring(s.text, parser)
# print(etree.tostring(test, pretty_print=True, method="html"))
# build_text_list = etree.XPath("//tr")
# print(build_text_list)
# myfile=open('/tmp/data','w')
# for i,x in
# enumerate(tnodes):
#     y=x.text_content()
#     print type(y)
#     print y
#     myfile.write(y.encode('utf-8'))
#     myfile.write(lxml.html.tostring(x, pretty_print=True, encoding='utf-8'))
#
# myfile.close()
with open('./test.html', 'wb+') as myfile:
    myfile.write(etree.tostring(root, pretty_print=True, method="html",encoding='utf-8'))
print(root.tag)
for element in root.iter("tr"):
    print("%s - %s" % (element.tag, element.text))