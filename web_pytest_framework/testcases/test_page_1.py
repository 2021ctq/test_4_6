# -*- codeing = utf-8 -*-
# @Time :2022/9/26 15:46
# @Author :ctq
# @File : test_page_1.py
# @Desc :
# import  unittest
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from  time import sleep
from objectpage.login_page import LoginPage
from config.config import driver_path,url
from data.data import ReadWrite
from log.log import loggers
class TestLoginCases:
    def test_1(self,login):
        """
        验证有效的用户名和密码登录成功
        """
        print("登录的第一测试用例")
        self.driver=login
        self.loginpage=LoginPage(self.driver)
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(0.5)

        # self.assertIn("我的地盘 - 禅道",self.driver.title,'页面不显示')
        assert  '我的地盘 - 禅道' in self.driver.title
        self.loginpage.click_logout()
        loggers.info("有效的用户名和密码成功登录系统")
    # @unittest.skip('不执行该测试用例')
    # @unittest.skipIf(system_version=='1.1',reason='只有版本号1.2才执行')
    # def test_2(self):
    #     """
    #     验证密码为空的时候变化
    #     """
    #     print("登录的第二个测试用例")
    #     self.loginpage.input_username("admin")
    #     self.loginpage.click_login()
    #     sleep(1)
    #     alert_log=self.driver.switch_to.alert
    #     alert_log.accept()


