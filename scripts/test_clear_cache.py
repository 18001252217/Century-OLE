import time

from base.init_driver import init_driver
from page.page import Page


class TestClearCache:

    def setup(self):
        self.driver = init_driver(no_reset=True)
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_clearcache(self):
        # 首页判断是否登录，如果没有则登录 (跳转到 "我" 页面)
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 清楚缓存
        self.page.setting.click_clear_cache()

        # 断言 toast 内容是否是 "清理成功"
        assert self.page.setting.is_toast_exist("清理成功")