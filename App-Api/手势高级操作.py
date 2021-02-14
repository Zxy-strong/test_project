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

el = driver.find_element_by_xpath('//*[contains(@text, "WLA")]')
TouchAction(driver).tap(el).perform()
time.sleep(2)
el_1 = driver.find_element_by_id("android:id/title")
# TouchAction(driver).press(el_1).wait(2000).release().perform()
TouchAction(driver).long_press(el=el_1, duration=2000).perform()
driver.quit()