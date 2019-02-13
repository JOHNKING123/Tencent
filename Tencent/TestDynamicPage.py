# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS()

# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path="C:\Program Files\phantomjs-2.1.1-windows\\bin\phantomjs")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
driver.get("https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=0")



# 生成当前页面快照并保存
#driver.save_screenshot("baidu.png")


# 打印网页渲染后的源代码
#print driver.page_source


data = driver.find_element_by_class_name("j_thread_list")
print data

# 获取当前url
print driver.current_url

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()