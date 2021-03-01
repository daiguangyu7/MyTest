from utils.seleniumtools import find_element

class AdminCommentPage():

    def __init__(self, driver):
        self.driver = driver

        self.comment_info = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/div[3]/input')
        self.comment_search = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[1]/button[1]')
        self.search_comment_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/button')

        self.dis_hi = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[1]/span')
        self.d_confirm = ('xpath', '/html/body/div[4]/div/div[3]/button[2]/span')
        self.dis_hi_result = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/span')

        self.top_bt = ('xpath', '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]/span')
        self.t_confirm = ('xpath', '/html/body/div[4]/div/div[3]/button[2]/span')
    def search_comment(self, comment):
        # 搜索评论内容
        find_element(self.driver, self.comment_info).send_keys(comment)
        find_element(self.driver, self.comment_search).click()
    
    # def dis_hid_comment(self):
    #     # 展示/隐藏评论
    #     find_element(self.driver, self.dis_hi).click()
    #     find_element(self.driver, self.d_confirm).click()
    
    # def top_comment(self):
    #     # 置顶评论
    #     find_element(self.driver, self.top_bt).click()
    #     find_element(self.driver, self.t_confirm).click()