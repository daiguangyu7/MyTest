from utils.seleniumtools import find_element

class AdminSysPage():

    def __init__(self, driver):
        self.driver = driver
        self.sale = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/form/div/div/div/input')
        self.s_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/button') 
    def update_sys(self, sale):
        # 修改销售额
        find_element(self.driver, self.sale).clear()
        find_element(self.driver, self.sale).send_keys(sale)
        find_element(self.driver, self.s_confirm).click()