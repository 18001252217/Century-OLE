from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll=1):
        """
        根据特征，找元素
        :param loc: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)\
            .until(lambda x:x.find_element(*loc))

    def base_find_elements(self, loc, timeout=30, poll=1):
        """
        根据特征，找多个符合条件的元素
        :param loc: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)\
            .until(lambda x:x.find_elements(*loc))

    def base_click_element(self, loc):
        """
        封装点击操作函数
        """
        self.base_find_element(loc).click()

    def base_input_text(self, loc, text):
        """
        封装输入操作函数
        """
        self.fm = self.base_find_element(loc)
        self.fm.clear()  # 需要先清空输入框，防止有默认内容
        self.fm.send_keys(text)

    def base_input_clear(self, loc):
        """
        封装清空操作函数
        """
        self.base_find_element(loc).clear()

    def base_get_value(self, loc):
        """
        获取元素的值
        """
        return self.base_find_element(loc).text

    def base_press_back(self):
        """
        点击返回健
        """
        self.driver.press_keycode(4)

    def base_press_enter(self):
        """
        点击回车
        """
        self.driver.press_keycode(66)
