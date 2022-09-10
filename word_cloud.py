from wordcloud import WordCloud
import jieba


def trans_CN(txt):
    # 将文件分割
    word_list = jieba.cut(txt)
    result = "".join(word_list)
    return result


with open(r'D:\FakeC\Files\Seven\K\send.txt', encoding='utf-8') as fp:
    text = fp.read()
    # print(text)

    # 进行词云的生成
    text = trans_CN(text)
    wordcloud = WordCloud(
        font_path=r"dx.ttf",
        width=2000,
        height=1000
    ).generate(text)
    res = wordcloud.to_image()
    res.show()
