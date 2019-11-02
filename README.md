# ApacheLogAnalyzer

### userage:
#### 0. 运行
> 直接运行或加-h参数查看帮助
```shell script
PYTHONPATH=../ python analyzer.py
PYTHONPATH=../ python analyzer.py -h
```

##### 1. 帮助信息
```shell script
usage: analyzer.py [-h] [--type TYPE [TYPE ...]] [--domain DOMAIN]
                   [--outfile OUTFILE] [--fetch-title FETCH_TITLE]
                   files [files ...]

positional arguments:
  files                 待分析的日志文件 file1.log [file2.log [...]]

optional arguments:
  -h, --help            show this help message and exit
  --type TYPE [TYPE ...]
                        描述报表类型 [all[,ip[, article[, full]]]]
  --domain DOMAIN       服务器域名
  --outfile OUTFILE     报表输出文件
  --fetch-title FETCH_TITLE
                        预处理文章标题
```

#### 2. demo运行结果
##### 2.0 处理日志标题信息
```shell script
PYTHONPATH=../ python analyzer.py ./apache.log --fetch-title=true

output: <.titlecache>
{
    "/lei0213/p/7506130.html": "python\u722c\u866b\u4e4bxpath\u7684\u57fa\u672c\u4f7f\u7528 - Charles.L - \u535a\u5ba2\u56ed",
    "/coding/miniproject/material.htm": "404_\u9875\u9762\u4e0d\u5b58\u5728 - \u535a\u5ba2\u56ed",
    "/coding/miniproject/material1.html": "404_\u9875\u9762\u4e0d\u5b58\u5728 - \u535a\u5ba2\u56ed"
}
```  

#### 2.1 分析报告
```shell script
PYTHONPATH=../ python analyzer.py
```
> 输出结果：
## 完整报告
|URL|IP|访问次数|
|:---:|:---:|:---:|
|/lei0213/p/7506130.html|200.200.76.130|1|
|/coding/miniproject/material.htm|200.200.76.130|1|
|/coding/miniproject/material1.html|200.200.76.130|1|

## IP报告
|IP|访问数|访问文章数|
|:---:|:---:|:---:|
|200.200.76.130|3|3|

## 文章报告
|URL|标题|访问人次|访问ip数|
|:---:|:---:|:---:|:---:|
|/lei0213/p/7506130.html|python爬虫之xpath的基本使用 - Charles.L - 博客园|1|1|
|/coding/miniproject/material.htm|404_页面不存在 - 博客园|1|1|
|/coding/miniproject/material1.html|404_页面不存在 - 博客园|1|1|

#### 3 单元测试
```
collected 13 items

unit/tests/test_cmd.py .                                                                                                                   [  7%]
unit/tests/test_http_utils.py .                                                                                                            [ 15%]
unit/tests/test_record.py .......                                                                                                          [ 69%]
unit/tests/test_report.py ....                                                                                                             [100%]

---------- coverage: platform linux2, python 2.7.5-final-0 -----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
__init__.py                         0      0   100%
analyzer.py                        52     52     0%
cmd/__init__.py                     0      0   100%
cmd/user_options.py                18      0   100%
parser/__init__.py                  0      0   100%
parser/record.py                   71      6    92%
report/__init__.py                  0      0   100%
report/report.py                  114      9    92%
unit/__init__.py                    0      0   100%
unit/tests/__init__.py              0      0   100%
unit/tests/test_cmd.py             20      0   100%
unit/tests/test_http_utils.py      15      0   100%
unit/tests/test_record.py          46      0   100%
unit/tests/test_report.py          72      0   100%
utils/__init__.py                   0      0   100%
utils/http_utils.py                70     5    93%
---------------------------------------------------
TOTAL                             466     84    92%
```