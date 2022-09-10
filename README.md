# WeChat Exporter and WordCloud

## Step1: 下载安装并使用 WeChat Exporter导出记录

已经有链接 https://github.com/BlueMatthew/WechatExporter 按照老哥的操作就没有问题

我将主要步骤整理如下，可参考

* 拥有一台IOS或者iPad OS设备并将记录备份至这个设备
* 电脑下载iTunes
* 打开iTunes 并将刚刚的设备连接电脑
* 根据iTunes提示操作备份，注意不要选择加密
* 打开下载的工具软件，自动定位了刚刚的备份
  * ![image-20220910233426636](https://github.com/Zaiz-77/wechat-wordcloud/blob/main/imgs/image-20220910233426636.png)

* 选择输出目录
  * ![image-20220910233451712](https://github.com/Zaiz-77/wechat-wordcloud/blob/main/imgs/image-20220910233451712.png)
* 上方修改模式为文本即可
  * ![image-20220910233523717](https://github.com/Zaiz-77/wechat-wordcloud/blob/main/imgs/image-20220910233523717.png)
* 导出目标目录便可

## Step2: 安装wordcloud和jieba库

* 打开Pycharm软件在底部寻找**Terminal**并点击，然后输入安装命令，使用豆瓣源会快很多，分别粘贴以下命令回车运行即可

  ![image-20220910233950439](https://github.com/Zaiz-77/wechat-wordcloud/blob/main/imgs/image-20220910233950439.png)

  ```
  pip install selenium -i https://pypi.doubanio.com/simple wordcloud
  pip install selenium -i https://pypi.doubanio.com/simple jieba
  ```

## Step3: 使用代码即可

## 仅供娱乐，如有任何问题请联系KandQwangkai@163.com
