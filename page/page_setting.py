from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class PageSetting(BaseAction):
    # 清理缓存
    clear_cache_button = By.XPATH, "//*[@text='清理缓存']"
    # 关于百年奥莱
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 点击 清理缓存按钮
    def click_clear_cache(self):
        self.find_element_with_scroll(self.clear_cache_button).click()

    # 点击 关于百年奥莱
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()