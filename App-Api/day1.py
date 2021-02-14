# import appium.webdriver
from appium import webdriver
import base64
# 启动参数
desired_caps = {}
# 系统
desired_caps['platformName'] = 'Android'
# 版本
desired_caps['platformVersion'] = '7.1.2'
# 设备号
desired_caps['deviceName'] = '127.0.0.1:62001'
# 包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 发送文件到手机
# data = str(base64.b64encode("push 2222222".encode('utf-8')), 'utf-8')
# driver.push_file("/storage/emulated/0/push.txt", data)

# 从手机中拉取文件
# get_data = driver.pull_file('/storage/emulated/0/push.txt')
# print(str(base64.b64decode(get_data),'utf-8'))

# 获取当前屏幕内元素结构
print(driver.page_source)
driver.quit()