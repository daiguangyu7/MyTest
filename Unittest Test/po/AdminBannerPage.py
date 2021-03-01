from utils.seleniumtools import find_element

class AdminBannerPage():

    def __init__(self, driver):
        self.driver = driver

        self.search = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input')
        self.resetbt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[2]')
        self.search_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.b_text = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div')
        self.update_banner = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[10]/div/button[3]/span')
        self.clear_desc = ('xpath', '//*[@id="bannerList"]/div[1]/div/div/div/div/input')
        self.update_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/button[1]')
    def reset_search(self):
        # 重置搜索
        find_element(self.driver, self.search).send_keys('aaa')
        find_element(self.driver, self.resetbt).click()
    
    def search_banner(self, search):
        # 搜索banner
        find_element(self.driver, self.search).send_keys(search)
        find_element(self.driver, self.search_bt).click()

    def update_banner_desc(self,update_desc):
        # 修改banner描述信息
        find_element(self.driver, self.update_banner).click()
        find_element(self.driver, self.clear_desc).clear()
        find_element(self.driver, self.clear_desc).send_keys(update_desc)
        find_element(self.driver, self.update_bt).click()