from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageLogin(BaseAction):
    # 账号
    username_input = By.ID, "com.yunmall.lc:id/logon_account_textview"
    # 密码
    password_input = By.ID, "com.yunmall.lc:id/logon_password_textview"
    # 登录按钮
    # login_button = By.XPATH, "//*[@text='登录']"
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    # 输入账号
    def input_username_text(self, text):
        self.base_input_text(self.username_input, text)

    # 输入密码
    def input_password_text(self, text):
        self.base_input_text(self.password_input, text)

    # 点击登录按钮
    def click_login_button(self):
        self.base_click_element(self.login_button)