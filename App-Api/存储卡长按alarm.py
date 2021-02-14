from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.amaze.filemanager'
desired_caps['appActivity'] = '.activities.MainActivity'
desired_caps['unicodeKeyboadr'] = True
desired_caps['resetKeyboard'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)


driver.find_element_by_xpath('//*[contains(@text, "允许")]').click()
time.sleep(2)
el_list = driver.find_elements_by_id("com.amaze.filemanager:id/firstline")
for i in el_list:
    if i.text =="Alarms":
        TouchAction(driver).long_press(i).perform()
        break
driver.quit()