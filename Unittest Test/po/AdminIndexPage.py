from utils.seleniumtools import find_element

class AdminIndexPage():

    def __init__(self, driver):
        self.driver = driver

        self.log = ('xpath', '//*[@id="app"]/div/div[1]/div[2]')
        self.user_menu = ('xpath', '//*[@id="app"]/div/div[1]/div[3]/div/div[3]/span')
        self.ht_text = "后台管理系统"
        self.user = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[2]/span')
        self.goods = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[4]/span')
        self.banner = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[1]/span')
        self.agent = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[3]/span')
        self.sort = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[5]/span')
        self.postage = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[6]/span')
        self.order = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[7]/span')
        self.cashout = ('xpath','//*[@id="app"]/div/div[2]/ul/li[8]/span')
        self.commission_bt = ('xpath', '//*[@id="app"]/div/div[2]/ul/li[9]/span')
        self.commission_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')
        
        self.comment = ('xpath', '//*[text()="评论管理"]')
        self.sys_bt = ('xpath', '//*[text()="系统配置"]')
        self.limit_menu = ('xpath', '//*[text()="权限管理"]')

        self.comment_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')
        self.sys_bt_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')
    def open_url(self):
        self.driver.get(self.url)

    def click_user(self):
        # 点击用户管理
        find_element(self.driver, self.user).click()

    def click_goods(self):
        # 点击商品管理
        find_element(self.driver, self.goods).click()
    
    def click_banner(self):
        # 点击轮播图管理
        find_element(self.driver, self.banner).click()
    
    def click_agent(self):
        # 点击代理管理
        find_element(self.driver, self.agent).click()
    
    def click_sort(self):
        # 点击分类管理
        find_element(self.driver, self.sort).click()
    
    def click_postage(self):
        # 点击邮费管理
        find_element(self.driver, self.postage).click()
    
    def click_order(self):
        # 点击订单管理
        find_element(self.driver, self.order).click()
    
    def click_cashout(self):
        # 点击提现管理
        find_element(self.driver, self.cashout).click()
    
    def click_commission(self):
        # 点击佣金记录
        find_element(self.driver,self.commission_bt).click()
    
    def click_limit(self):
        # 点击权限管理
        find_element(self.driver,self.limit_menu).click()

    def click_comment(self):
        # 点击评论管理
        find_element(self.driver, self.comment).click()
    
    def click_sys(self):
        # 点击系统管理
        find_element(self.driver, self.sys_bt).click()

