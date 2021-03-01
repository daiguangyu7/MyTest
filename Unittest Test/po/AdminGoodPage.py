from utils.seleniumtools import find_element

class AdminGoodPage():

    def __init__(self, driver):
        self.driver = driver

        self.good_status = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/span')

        self.on_sale_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[10]/div/button[1]/span')
        self.confirm = ('xpath', '/html/body/div[3]/div/div[3]/button[2]')
        self.on_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/span')

        self.pic = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[3]/td[10]/div/button[4]/span')
        self.pic_start_stop = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/button/span')
        self.p_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
        self.p_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span')

        self.pic_status = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span')
        self.update_good = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[10]/div/button[3]/span')
        self.update_good_info = ('xpath', '')

        self.update = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[10]/div/button[3]/span')
        self.click_sort = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/form/div[2]/div/div/div/input')
        self.sel_sort = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/form/div[2]/div/div/div/input')
        self.s_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/form/div[10]/div/button')
        
        self.search_good_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/input')
        self.search_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.s_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[4]/div')

        self.click_specs = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[10]/div/button[5]/span')
        self.update_spe = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[12]/div/button[2]/span')
        self.price = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/form/div[5]/div/div/input')
        self.p_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/form/div[12]/div/button/span')
        self.u_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div')
        
        self.del_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[4]/td[10]/div/button[6]/span')
        self.d_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
    def on_sale(self):
        # 上架/下架商品
        find_element(self.driver, self.on_sale_bt).click()
        find_element(self.driver, self.confirm).click()
    
    def start_stop_pic(self):
        # 启用/禁用商品图片
        find_element(self.driver, self.pic).click()
        find_element(self.driver, self.pic_start_stop).click()
        find_element(self.driver, self.p_confirm).click()

    def update_good_sort(self):
        # 修改商品分类
        find_element(self.driver, self.update).click()
        find_element(self.driver, self.click_sort).click()
        find_element(self.driver, self.sel_sort).click()
        find_element(self.driver, self.s_confirm).click()
    
    def search_name(self, name):
        # 搜索商品名称
        find_element(self.driver, self.search_good_name).send_keys(name)
        find_element(self.driver, self.search_bt).click()
    
    def update_specs(self, price):
        # 修改商品价格
        find_element(self.driver, self.click_specs).click()
        find_element(self.driver, self.update_spe).click()
        find_element(self.driver, self.price).clear()
        find_element(self.driver, self.price).send_keys(price)
        find_element(self.driver, self.p_confirm).click()

    def del_good(self):
        # 删除商品
        find_element(self.driver, self.del_bt).click()
        find_element(self.driver, self.d_confirm).click()

