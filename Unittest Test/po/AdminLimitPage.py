from utils.seleniumtools import find_element

class AdminLimitPage():

    def __init__(self, driver):
        self.driver = driver

        self.admin_limit = ('xpath', '//*[text()="管理员管理"]')
        self.admin_role = ('xpath', '//*[text()="角色管理"]')

        self.add_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button/span')
        self.add_account = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input')
        self.add_nickname = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/input')
        self.add_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[3]/div/div/input')
        self.a_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]/span')

        self.reset_pass = ('xpath', '//*[@id="tableDiv"]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/button[5]')
        self.reset_pass_confirm = ('xpath', '/html/body/div[3]/div/div[3]/button[2]')

        self.add_role_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button')
        self.add_role_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[2]/form/div/div/div/input')
        self.add_role_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[3]/span/button[2]')

        self.set_limit_bt = ('xpath', '//*[@id="tableDiv"]/div[4]/div[2]/table/tbody/tr[10]/td[3]/div/button[1]')
        self.set_limit_one = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[5]/div/div/section/div[1]/div[1]/div[1]/label/span/span')
        self.set_limit_two = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[5]/div/div/section/div[1]/div[2]/div[1]/label/span/span')
        self.set_limit_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[5]/div/div/section/div[2]/button[1]/span')

        self.update_role_bt = ('xpath', '//*[@id="tableDiv"]/div[4]/div[2]/table/tbody/tr[6]/td[3]/div/button[2]/span')
        self.role_name = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[4]/div/div[2]/form/div/div/div/input')
        self.update_role_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[4]/div/div[3]/span/button[2]/span')
        self.update_role_result = ('xpath', '//*[@id="tableDiv"]/div[3]/table/tbody/tr[6]/td[2]/div')
    def click_admin_limit(self):
        # 点击管理员权限管理
        find_element(self.driver, self.admin_limit).click()
    
    def add_admin(self, account, nickname, name):
        # 添加管理员
        find_element(self.driver,self.add_bt).click()
        find_element(self.driver, self.add_account).send_keys(account)
        find_element(self.driver, self.add_nickname).send_keys(nickname)
        find_element(self.driver, self.add_name).send_keys(name)
        find_element(self.driver, self.a_confirm).click()
    
    def reset_pass(self):
        # 重置密码
        find_element(self.driver, self.reset_pass).click()
        find_element(self.driver, self.reset_pass_confirm).click()
    
    def click_admin_role(self):
        # 点击角色管理
        find_element(self.driver, self.admin_role).click()
    
    def add_role(self,role_name):
        # 新增角色
        find_element(self.driver, self.add_role_bt).click()
        find_element(self.driver, self.add_role_name).send_keys(role_name)
        find_element(self.driver, self.add_role_confirm).click()

    def set_limit(self):
        # 设置权限
        find_element(self.driver, self.set_limit_bt).click()
        find_element(self.driver, self.set_limit_one).click()
        find_element(self.driver, self.set_limit_two).click()
        find_element(self.driver, self.set_limit_confirm).click()

    def update_role(self,role_name):
        # 修改角色名
        find_element(self.driver, self.update_role_bt).click()
        find_element(self.driver, self.role_name).clear()
        find_element(self.driver, self.role_name).send_keys(role_name)
        find_element(self.driver, self.update_role_confirm).click()
