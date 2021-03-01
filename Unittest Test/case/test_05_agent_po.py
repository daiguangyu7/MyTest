import time
import unittest
from selenium import webdriver
from po.AdminLoginPage import AdminLoginPage
from po.AdminIndexPage import AdminIndexPage
from po.AdminAgentPage import AdminAgentPage
class TestCaseLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        cls.driver.maximize_window()
        cls.admin_login_page = AdminLoginPage(cls.driver)
        cls.admin_index_page = AdminIndexPage(cls.driver)
        cls.admin_agent_page = AdminAgentPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def setUp(self):
        self.admin_login_page.open_url()
        # 判断是否已经登录，如果已经登陆了，就不要再的登陆
        # 如果没有登录，就去登录
        e = self.driver.find_elements_by_xpath(self.admin_index_page.log[-1])
        if len(e) == 0:
            self.admin_login_page.login('admin', '123456')
    
    def test_01_agent_verify(self):
          #审核用户
        self.admin_index_page.click_agent()
        time.sleep(2)

        self.admin_agent_page.agent_verify()
        time.sleep(3)
        e = self.driver.find_element_by_xpath(self.admin_agent_page.v_result[-1])
        assert e.text in ('正常', '未通过')
    
    def test_02_search(self):
          #搜索用户
        self.admin_index_page.click_agent()
        time.sleep(2)

        self.admin_agent_page.search_user('15831041439')
        time.sleep(2)
        e = self.driver.find_element_by_xpath(self.admin_agent_page.search_result[-1])
        assert len(e.text) != 0
    
