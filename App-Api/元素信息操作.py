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

try:
    driver.find_element_by_id("com.android.settings:id/search").click()
    for i in ("wi", "vp", "123"):
        driver.find_element_by_id("android:id/search_src_text").clear()
        driver.find_element_by_id("android:id/search_src_text").send_keys(i)
        el_list = driver.find_elements_by_id("com.android.settings:id/title")
        for a in el_list:
            print(a.text)
        if el_list:
            print(True)
        else:
            print(False)

except Exception as e:
    print(e)
finally:
    driver.quit()


