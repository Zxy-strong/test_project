from appium import webdriver
import time

desirde_caps = {}
desirde_caps['platformName'] = 'Android'
desirde_caps['platformVersion'] = '7.1.2'
desirde_caps['deviceName'] = '127.0.0.1:62001'
desirde_caps['appPackage'] = 'com.android.settings'
desirde_caps['appActivity'] = '.Settings'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desirde_caps)


# 定位一组元素
# try:
#     driver.find_element_by_id("com.android.settings:id/search").click()
#     time.sleep(2)
#     driver.find_element_by_class_name("android.widget.ImageButton").click()
#     time.sleep(2)
# except Exception as e:
#     print(e)
# finally:
#     driver.quit()


# 定位多组元素
ele_list = driver.find_elements_by_id("android:id/title")
for i in ele_list:
    print(i.text)
    # if i.text =="更换壁纸":
    #     i.click()
    #     break

driver.quit()