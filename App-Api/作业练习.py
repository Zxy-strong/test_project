from appium import webdriver
import time
import base64

from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboadr'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 发送文件到手机目录下
# with open("./python.txt", "r") as f:
#     data = str(base64.b64encode(f.read().encode('utf-8')), 'utf-8')
#     driver.push_file('/storage/emulated/0', data)
# 拉取手机文件到电脑
# data = driver.pull_file("storage/emulated/0/push.txt")
# with open("C:/Users/ZXY/Desktop/phone.txt", "a")as f:
#     f.write(str(base64.b64decode(data),"utf-8"))

# 屏幕滑动
# driver.close_app()
#
# w_h = driver.get_window_size()
# w = w_h.get("width")
# h = w_h.get("height")
# driver.swipe(w*0.8, h*0.5, w*0.2, h*0.5, 1000)

# 手指轻敲操作
# 通过元素定位
# WL_T = driver.find_element_by_xp ath("//*[contains(@text, 'WLA')]")
# TouchAction(driver).tap(WL_T).perform()

# 通过位置定位
WL_T = driver.find_element_by_xpath("//*[contains(@text, 'WLA')]")
TouchAction(driver).tap(x=WL_T.location.get("x"), y=WL_T.location.get("y")).perform()