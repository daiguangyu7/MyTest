from utils.seleniumtools import find_element

class AdminAgentPage():

    def __init__(self, driver):
        self.driver = driver

        self.verify_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[9]/td[10]/div/button/span')
        self.v_status = ('xpath' ,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div/div/div/div/input')
        self.v_status_choice_sele = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
        self.v_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]')
        self.result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[6]/td[9]/div/span')
        self.v_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[9]/td[9]/div/span')

        self.search_tel = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div/input')
        self.search_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.search_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[4]/div')
    def agent_verify(self):
        # 审核
        find_element(self.driver, self.verify_bt).click()
        find_element(self.driver, self.v_status).click()
        find_element(self.driver, self.v_status_choice_sele).click()
        find_element(self.driver, self.v_confirm).click()
    
    def search_user(self,tel):
        # 搜索用户
        find_element(self.driver, self.search_tel).send_keys(tel)
        find_element(self.driver, self.search_bt).click()