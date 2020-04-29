from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageHome(BaseAction):

    # 提示跟新关闭按钮
    close_button = By.ID, "com.yunmall.lc:id/img_close"
    # 我的按钮
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 点击我的按钮
    def click_me_button(self):
        self.base_click_element(self.close_button)
        self.base_click_element(self.me_button)

    def login_if_not(self, page):
        # 判断登录状态
        self.click_me_button()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 没有登录，就去登录
        page.register.click_login_button()
        page.login.input_username_text("itheima_test")
        page.login.input_password_text("itheima")
        page.login.click_login_button()


