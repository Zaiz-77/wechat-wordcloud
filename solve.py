import re

with open(r'D:\FakeC\Files\Seven\K\七七.txt', encoding="utf-8") as fp:
    # 把双方记录预处理至 received and send 代表自己收到的和发出的
    for s in fp.readlines():
        idx = s.find(")")
        # 使用正则剔除所有[表情]
        s1 = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s[(idx + 2):])
        # 使用正则剔除所有非中文内容
        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        ed = re.sub(pattern, '', s1)
        # 看自己的昵称而改变
        if s.startswith("K"):
            with open(r'D:\FakeC\Files\Seven\K\send.txt', mode='a', encoding="utf-8") as to1:
                to1.write(ed)
                to1.write("\n")
        else:
            with open(r'D:\FakeC\Files\Seven\K\received.txt', mode='a', encoding="utf-8") as to2:
                to2.write(ed)
                to2.write("\n")
