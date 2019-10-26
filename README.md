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
