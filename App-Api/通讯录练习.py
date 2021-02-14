from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboadr'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[contains(@text, '本地')]").click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[contains(@text,"姓名")]').send_keys("124")
# time.sleep(2)
# driver.find_element_by_xpath('//*[contains(@text, "电话")]').send_keys("123456")
# time.sleep(2)
# driver.find_element_by_id("com.android.contacts:id/menu_save").click()
# time.sleep(2)

# 页面滑动
# 方法一
# driver.swipe(208,604,208,420,5000)
# 方法二
# start_ai = driver.find_element_by_xpath('//*[contains(@text, "WLAN")]')
# end_ai = driver.find_element_by_xpath('//*[contains(@text, "锁定")]')
# # driver.scroll(start_ai, end_ai)
# # 方法三
# driver.drag_and_drop(start_ai, end_ai)
# 将app至于后台
# driver.background_app(2)

print(driver.device_time)
print(driver.get_window_size())
driver.open_notifications()
driver.keyevent(3)
print(driver.network_connection)
driver.set_network_connection(1)
print(driver.network_connection)
driver.quit()