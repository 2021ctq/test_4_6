# -*- codeing = utf-8 -*-
# @Time :2022/9/27 13:40
# @Author :ctq
# @File : log.py
# @Desc :日志
import  logging
from study.web自动化测试.config.config import log_path

#创建日志器
loggers=logging.getLogger()
#定义日志器的级别
loggers.setLevel(logging.INFO)
#定义处理器的格式
format=logging.Formatter("%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s")
#创建处理器
f=logging.FileHandler(log_path,mode='a',encoding='utf-8')
#设置处理器的级别
f.setLevel(logging.INFO)
#设置处理器的格式
f.setFormatter(format)
#添加到日志器
loggers.addHandler(f)
