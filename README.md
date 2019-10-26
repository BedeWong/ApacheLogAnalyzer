# ApacheLogAnalyzer

### userage
#### 运行
> 直接运行或加-h参数查看帮助
```
PYTHONPATH=../ python analyzer.py
PYTHONPATH=../ python analyzer.py -h
```

##### 帮助信息
```
usage: analyzer.py [-h] [--type TYPE [TYPE ...]] [--domain DOMAIN]
                   [--outpath OUTPATH]
                   files [files ...]

positional arguments:
  files                 待分析的日志文件 file1.log [file2.log [...]]

optional arguments:
  -h, --help            show this help message and exit
  --type TYPE [TYPE ...]
                        描述报表类型 [all[,ip[, article[, full]]]]
  --domain DOMAIN       服务器域名
  --outpath OUTPATH     报表输出目录
```

#### demo运行结果
===========
|URL|IP|访问次数|
|:---:|:---:|:---:|
|/coding/miniprj/material.html|200.200.76.130|1|
|/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip|200.200.76.130|1|
|/designing/tools/image/UML_classes.docx|177.1.81.42|1|

=============
|IP|访问数|访问文章数|
|:---:|:---:|:---:|
|200.200.76.130|2|1|
|177.1.81.42|1|1|

===========================
|URL|标题|访问人次|访问ip数|
|:---:|:---:|:---:|:---:|
|/coding/miniprj/material.html|Error response|1|1|
|/coding/style/%E7%BC%96%E7%A0%81%E9%A3%8E%E6%A0%BC.zip|Error response|1|1|
|/designing/tools/image/UML_classes.docx|Error response|1|1
