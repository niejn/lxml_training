'''

str=’cheng_cheng’

第一种 b’cheng_cheng’
第二种bytes(‘cheng_cheng’,encoding=’utf-8’)
第三种(‘cheng_cheng’).encode(‘utf-8’)
bytes_gb2312.decode(encoding="gb2312")
'''

with open('./test.html', 'rb') as myfile:
    content = myfile.read()
    # content = myfile.readlines()
    # print(c1)
    content = content.decode(encoding="utf-8")
    print(content)
    from lxml import etree
    from io import StringIO, BytesIO

    string = "<p><code>git clone https://github.com/AlexeyAB/darknet.git</code></p>"
    parser = etree.HTMLParser()
    # content = content.
    root = etree.fromstring(content, parser)
    print(root.tag)
    for element in root.iter("td"):
        print("%s - %s" % (element.tag, element.text))