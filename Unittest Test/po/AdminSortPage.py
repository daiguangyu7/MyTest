from utils.seleniumtools import find_element

class AdminSortPage():

    def __init__(self, driver):
        self.driver = driver

        self.sort_title = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/span/span[1]')

        self.dis_hid_sort = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/button[1]/span')
        self.d_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
        self.sort_status = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span')

        self.update_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/button[2]/span')
        self.update_sort_num = ('xpath', '//*[@id="bannerList"]/div[2]/div/div/div/div/input')
        self.u_confirm = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div/div/div/button[1]/span')
        self.sort_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div')

        self.mass_del_one = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[1]/div/label/span/span')
        self.mass_del_two = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[6]/td[1]/div/label/span/span')
        self.mass_del_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[4]')
        self.mass_del_confirm = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')
    def display_hide_sort(self):
        # 显示/隐藏分类
        find_element(self.driver, self.dis_hid_sort).click()
        find_element(self.driver, self.d_confirm).click()

    def update_sort(self, sort):
        # 修改分类排序
        find_element(self.driver, self.update_bt).click()
        find_element(self.driver, self.update_sort_num).clear()
        find_element(self.driver, self.update_sort_num).send_keys(sort)
        find_element(self.driver, self.u_confirm).click()

    def mass_del(self):
        # 批量删除分类
        find_element(self.driver, self.mass_del_one).click()
        find_element(self.driver, self.mass_del_two).click()
        find_element(self.driver, self.mass_del_bt).click()
        find_element(self.driver, self.mass_del_confirm).click()