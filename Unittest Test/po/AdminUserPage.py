from utils.seleniumtools import find_element
class AdminUserPage():

    # 构造方法: 实例化类的时候，首先调用这个方法来初始化成员变量，类自带的方法
    def __init__(self, driver):
        self.driver = driver
        
        # 1.把要用到的元素提前封装到成员变量
        self.url = "http://hxtx.testgoup.com/"
        self.input_username = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/input')
        self.searchbt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]/span')
        self.freezebt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[13]/div/button[1]')
        self.f_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]')
        self.f_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr/td[11]/div/span')
        self.page_to = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[3]/div/ul/li[4]')
        self.userinfo = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/button[2]/span')

    # 2.封装方法到成员方法
    def open_url(self):
        self.driver.get(self.url)

    # 2.2 封装搜索方法
    def search(self, input_username):
        find_element(self.driver, self.input_username).send_keys(input_username)
        find_element(self.driver, self.searchbt).click()

    def freeze_unfreeze(self):
        # 冻结，解冻用户
        find_element(self.driver, self.freezebt).click()
        find_element(self.driver, self.f_confirm).click()
    
    def page(self):
        # 跳转到指定页面
        find_element(self.driver,self.page_to).click()
        
    def user_info(self):
        # 用户详细信息
        find_element(self.driver, self.userinfo).click()
