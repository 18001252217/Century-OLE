from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageRegister(BaseAction):
    # 登录按钮
    login_button = By.ID, "com.yunmall.lc:id/gotologon"

    # 点击登录
    def click_login_button(self):
        self.base_click_element(self.login_button)

