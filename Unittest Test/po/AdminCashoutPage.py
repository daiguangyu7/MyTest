from utils.seleniumtools import find_element

class AdminCashoutPage():

    def __init__(self, driver):
        self.driver = driver

        self.click_cashout_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')

        self.search_tel = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/input')
        self.s_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.search_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[4]/div')

        self.verify = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[8]/td[12]/div/button/span')
        self.sel_status = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/div/input')
        self.sel_verify = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]')
        self.v_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]/span')
        self.verify_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[8]/td[11]/div/span')
    def search_by_tel(self, tel):
        # 根据用户手机号搜索
        find_element(self.driver, self.search_tel).send_keys(tel)
        find_element(self.driver, self.s_confirm).click()

    def cashout_verify(self):
        # 审核提现申请
        find_element(self.driver, self.verify).click()
        find_element(self.driver, self.sel_status).click()
        find_element(self.driver, self.sel_verify).click()
        find_element(self.driver, self.v_confirm).click()