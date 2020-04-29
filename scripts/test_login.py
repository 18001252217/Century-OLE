import time

import pytest

from base.init_driver import init_driver
from base.read_yaml import getData
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", getData("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 1.首页 点击 我
        self.page.home.click_me_button()
        # 2.注册 点击 登录
        self.page.register.click_login_button()
        # 3.登录 输入 用户名
        self.page.login.input_username_text(username)
        # 4.登录 输入 密码
        self.page.login.input_password_text(password)
        # 5.登录 点击 登录
        self.page.login.click_login_button()
        if toast is None:
            # 6.断言，如果"我"页面的用户名 和 输入的用户名 一致，那么脚本通过
            assert self.page.me.get_nick_name_text() == username, "登录的用户名和输入的用户名不一致"
        else:
            assert self.page.login.is_toast_exist(toast)

