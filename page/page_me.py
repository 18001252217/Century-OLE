from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageMe(BaseAction):
    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    def get_nick_name_text(self):
        return self.base_get_value(self.nick_name_text_view)

    # 点击设置按钮
    def click_setting(self):
        self.base_click_element(self.setting_button)
