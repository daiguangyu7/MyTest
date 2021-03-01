from utils.seleniumtools import find_element

class AdminPostagePage():

    def __init__(self, driver):
        self.driver = driver

        self.postage_title = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')

        self.search_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input')
        self.search_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.search_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/div')

        self.add_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[3]/span')
        self.add_postage_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div[1]/input')
        self.add_postage_price = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/input')
        self.add_status = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div[1]/div/input')
        self.add_status_valid = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
        self.a_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]/span')

        self.update_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button[3]/span')
        self.update_price = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[2]/div/div/input')
        self.u_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]')
        self.price_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div')

        self.prov_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/button[2]/span')
        self.sel_pro_one = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div/section/div[1]/div[9]/div/label/span/span')
        self.sel_pro_two = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div/section/div[1]/div[10]/div/label/span/span')
        self.p_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[5]/div/div/section/div[2]/button[1]/span')

        self.del_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[10]/td[5]/div/button[4]/span')
        self.d_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.del_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[10]/td[2]/div')
        
    def search_postage(self,name):
        # 搜索邮费
        find_element(self.driver, self.search_name).send_keys(name)
        find_element(self.driver, self.search_bt).click()

    def add_postage(self,name,price):
        # 新增邮费模板
        find_element(self.driver, self.add_bt).click()
        find_element(self.driver, self.add_postage_name).send_keys(name)
        find_element(self.driver, self.add_postage_price).send_keys(price)
        find_element(self.driver, self.add_status).click()
        find_element(self.driver, self.add_status_valid).click()
        find_element(self.driver, self.a_confirm).click()
    
    def update_postage_price(self, price):
        # 修改邮费价格
        find_element(self.driver, self.update_bt).click()
        find_element(self.driver, self.update_price).clear()
        find_element(self.driver, self.update_price).send_keys(price)
        find_element(self.driver, self.u_confirm).click()
    
    def update_prov(self):
        # 分配省份
        find_element(self.driver, self.prov_bt).click()
        find_element(self.driver, self.sel_pro_one).click()
        find_element(self.driver, self.sel_pro_two).click()
        find_element(self.driver, self.p_confirm).click()
    
    def del_postage(self):
        # 删除邮费模板
        find_element(self.driver, self.del_bt).click()
        find_element(self.driver, self.d_confirm).click()