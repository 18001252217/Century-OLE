import time

from base.init_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_update(self):
        # 首页判断是否登录，如果没有则登录 (跳转到 "我" 页面)
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 关于百年奥莱
        self.page.setting.click_about()
        # 关于百年奥莱 点击 版本更新
        self.page.about.click_update()
        # 断言 toast 内容是否是 "当前已是最新版本"
        assert self.page.about.is_toast_exist("当前已是最新版本")