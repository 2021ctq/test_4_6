# -*- codeing = utf-8 -*-
# @Time :2022/9/27 18:42
# @Author :ctq
# @File : run_pytest.py
# @Desc :
import subprocess

import  pytest
pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean',shell=True)
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)
