import time

from appium import webdriver


def init_driver():
    # 服务端启动参数
    desired_caps = {}
    # 手机 系统信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 设备号
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # 包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 启动名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # appium每次启动都会重置应用，不想重置，添加这行
    desired_caps['noReset'] = 'True'

    # 手机驱动对象
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
