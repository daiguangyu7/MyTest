from utils.seleniumtools import find_element

class AdminOrderPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_order_result = ('xpath', '//*[@id="Loading"]/div[1]/div/span/span[1]')
        self.search_num = ('xpath', '//*[@id="Loading"]/div[2]/div[1]/div[1]/div/input')
        self.search_bt = ('xpath', '//*[@id="Loading"]/div[2]/div[1]/div[5]/button[1]')
        self.search_result = ('xpath', '//*[@id="Loading"]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')

        self.ord_status = ('xpath', '//*[@id="Loading"]/div[2]/div[1]/div[5]/div[1]/div/div/input')
        self.sel_status_unfini = ('xpath', '//*[text()="支付完成/待发货"]')

        self.send = ('xpath', '//*[@id="Loading"]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[16]/div/button[1]')
        self.send_ord_num = ('xpath', '//*[@id="Loading"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input')
        self.send_ord_name = ('xpath', '//*[@id="Loading"]/div[3]/div/div[2]/form/div[2]/div/div[1]/input')
        self.s_confirm = ('xpath', '//*[@id="Loading"]/div[3]/div/div[3]/span/button[2]')

        self.import_bt = ('xpath', '//*[@id="Loading"]/div[2]/div[1]/div[5]/button[3]')
        self.i_confirm = ('xpath' ,'//*[text()="确认"]') 
    def search_order(self, oder_num):
        # 根据订单编号搜索订单
        find_element(self.driver, self.search_num).send_keys(oder_num)
        find_element(self.driver, self.search_bt)
    
    def order_status(self):
        # 根据订单状态搜索
        find_element(self.driver, self.ord_status).click()
        find_element(self.driver, self.sel_status_unfini).click()
        find_element(self.driver, self.search_bt).click()
    
    def order_send(self, ord_num, ord_name):
        # 订单发货
        find_element(self.driver, self.send).click()
        find_element(self.driver, self.send_ord_num).send_keys(ord_num)
        find_element(self.driver, self.send_ord_name).send_keys(ord_name)
        find_element(self.driver, self.s_confirm).click()
    
    def import_order(self):
        # 导出订单
        find_element(self.driver, self.import_bt).click()
        find_element(self.driver, self.i_confirm).click()