import os,sys
sys.path.append(os.getcwd())

import pytest
from appium import webdriver

class Test_01():
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicodeKeyboadr'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    def teardown_class(self):
        self.driver.quit()

    def test01(self):
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.driver.find_element_by_id("android:id/search_src_text").send_keys("1")
        el_list = self.driver.find_elements_by_id("com.android.settings:id/title")
        a_list = []
        for i in el_list:
            a_list.append(i.text)
        assert "2" in a_list, "失败了"

# if __name__ == '__main__':
#     pytest.main()