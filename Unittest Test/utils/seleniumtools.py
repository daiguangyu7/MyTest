"""
    固定用法，会用就行
"""
from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver, locator, timeout=10):
    """
        方法：显示等待，动态查找元素
        参数：
            driver：浏览器的把柄
            locator：元素定位的方式和值
                - ('id', 'kw')                      # driver.find_element_by_id
                - ('xpath', 'xxxxx')
                - ('name', 'xxx')
                - ('css selector', 'xxxx')
                - ('class name', 'xxxx')            # driver.find_element_by_class_name
                - ('link text', 'xxxx')             # driver.find_element_by_link_text
                - ('partial link text', 'xxx')      # driver.find_element_by_partial_link_text
            timeout：找元素的超时时间，默认60
        
        返回值：
            找到元素就返回元素，没有找到元素就报错：timeout错误
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))