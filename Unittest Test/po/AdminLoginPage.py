from utils.seleniumtools import find_element

class AdminLoginPage():
    def __init__(self, driver):
        self.driver = driver
        
        self.url = "http://hxtx.testgoup.com/"
        self.username = ('xpath', '//*[@id="app"]/div/div/form/div[1]/div/div/input')
        self.password = ('xpath', '//*[@id="app"]/div/div/form/div[2]/div/div/input')
        self.loginbtn = ('xpath', '//*[@id="app"]/div/div/form/div[3]/button')

    def open_url(self):
        self.driver.get(self.url)

    def login(self, username, password):
        find_element(self.driver, self.username).send_keys(username)
        find_element(self.driver, self.password).send_keys(password)
        find_element(self.driver, self.loginbtn).click()