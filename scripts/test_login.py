import time

from base.init_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        # 1.首页 点击 我
        self.page.home.click_me_button()
        # 2.注册 点击 登录
        self.page.register.click_login_button()
        # 3.登录 输入 用户名
        self.page.login.input_username_text("itheima_test")
        # 4.登录 输入 密码
        self.page.login.input_password_text("itheima")
        # 5.登录 点击 登录
        self.page.login.click_login_button()
        # 6.断言，如果"我"页面的用户名 和 输入的用户名 一致，那么脚本通过
        assert self.page.me.get_nick_name_text() == "itheima_test", "登录的用户名和输入的用户名不一致"
