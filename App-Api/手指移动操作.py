from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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

el_1 = driver.find_element_by_xpath('//*[contains(@text, "WLA")]')
el_2 = driver.find_element_by_xpath('//*[contains(@text, "设置屏幕锁定")]')
# TouchAction(driver).press(el_1).move_to(el_2).release().perform()

driver.drag_and_drop(el_1, el_2)
el_3 = driver.find_element_by_xpath('//*[contains(@text, "更多")]')
el_4 = driver.find_element_by_xpath('//*[contains(@text, "WLA")]')
driver.drag_and_drop(el_3, el_4)

el_5 = driver.find_element_by_xpath('//*[contains(@text, "通知")]')
el_6 = driver.find_element_by_xpath('//*[contains(@text, "蓝牙")]')
driver.drag_and_drop(el_5, el_6)

el_7 = driver.find_element_by_xpath('//*[contains(@text, "电池")]')
el_8 = driver.find_element_by_xpath('//*[contains(@text, "通知")]')
driver.drag_and_drop(el_7, el_8)

# 点击安全
driver.find_element_by_xpath('//*[contains(@text, "安全")]').click()
time.sleep(2)
# 点击屏幕锁定
driver.find_element_by_xpath('//*[contains(@text, "屏幕锁定")]').click()
time.sleep(2)
# 点击图案
driver.find_element_by_xpath('//*[contains(@text, "图案")]').click()
time.sleep(2)
# 950,210   1210,210   1210,470
# TouchAction(driver).press(x=949, y=207).wait(2000).move_to(x=261, y=0).wait(2000).move_to(x=0, y=261).perform()
TouchAction(driver).press(x=1210, y=210).move_to(x=1210, y=470).release().perform()
# TouchAction(driver).press(x=950, y=210).move_to(x=260, y=0).move_to(x=0, y=260).perform()

driver.quit()