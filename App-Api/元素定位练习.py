from appium import webdriver
import time

desirde_caps = {}
desirde_caps['platformName'] = 'Android'
desirde_caps['platformVersion'] = '7.1.2'
desirde_caps['deviceName'] = '127.0.0.1:62001'
desirde_caps['appPackage'] = 'com.android.settings'
desirde_caps['appActivity'] = '.Settings'
desirde_caps['unicodeKeyboadr'] = True
desirde_caps['resetKeyboard'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desirde_caps)


driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_id("android:id/search_src_text").send_keys("中文")
driver.find_element_by_class_name("android.widget.ImageButton").click()

driver.quit()