from telnetlib import EC#

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.by import By#
from selenium.webdriver.support.wait import WebDriverWait#
from selenium.webdriver.support import expected_conditions as EC



from selenium.webdriver.common.keys import Keys




































"""
driver.get("https://mail.163.com")
driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[1]/div/div[3]/div[1]/div[1]/iframe"))
driver.find_element_by_name("email").send_keys("zhanlantest@163.com")
driver.find_element_by_name("password").send_keys(a)

WebDriverWait(driver,3,0.1).until(EC.presence_of_element_located((By.ID,'dologin'))).click()
"""
#driver.get("https://jd.com")

#zhuye=driver.current_window_handle
#sleep(3)
#driver.find_element_by_css_selector("[id='key']").send_keys("笔记本电脑")
#driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div[1]/div/div/div/a[2]/div[1]/img").click()
#all=driver.window_handles

#多窗口切换
#driver.switch_to.window(driver.window_handles[1])#多窗口切换 下标从0开始
#sleep(2)
#driver.find_element_by_xpath('//*[@id="super_seckill"]/div/ul/li[2]/a/img').click()
"""
for handle in all:
    if handle!=zhuye:
        driver.switch_to.window(handle)
        print("现在是第二个页面")

#print(driver.window_handles)
#print(driver.current_window_handle)
print(driver.get_cookies())
for cookie in driver.get_cookies():
    print(cookie['name'])

"""

#操作js弹框
#driver.switch_to.alert.accept()#确定
#driver.switch_to.alert.dissmiss()#取消
#driver.switch_to.window(driver.window_handles[0])

#driver.find_elements_by_tag_name("input")[0].send_keys("666")

#driver.find_elements_by_tag_name("input").pop(0).send_keys("666")

"""
element1=driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[18]/a")
element2=driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div/div[2]/input")
#1.悬停
ActionChains(driver).move_to_element(element1).perform()
#2.右击
ActionChains(driver).context_click(element1).perform()
#3.双击
ActionChains(driver).double_click(element2).perform()
#4.拖拽
ActionChains(driver).drag_and_drop(element1,element2).perform()
"""

"""
e2=driver.find_elements_by_tag_name("input")
for e3 in e2:
    sleep(1)
print(len(e2))


for e in range(0,len(e2)):
    print(e)
"""






"""
from selenium.webdriver.common.keys import Keys#引入键盘事件
driver.find_element_by_xpath("//input").send_keys(Keys.CONTROL,'a')#全选
driver.find_element_by_xpath("//input").send_keys(Keys.CONTROL,'x')#剪切
driver.find_element_by_xpath("//input").send_keys(Keys.CONTROL,'v')#粘贴
driver.find_element_by_xpath("//input").send_keys(Keys.CONTROL,'c')#复制
driver.find_element_by_xpath("//input").send_keys(Keys.BACK_SPACE)#删除
driver.find_element_by_xpath("//input").send_keys(Keys.SPACE)#空格键
driver.find_element_by_xpath("//input").send_keys(Keys.TAB)#制表键
driver.find_element_by_xpath("//input").send_keys(Keys.F1)#f1键
driver.find_element_by_xpath("//input").send_keys(Keys.F2)#f2键
driver.find_element_by_xpath("//input").send_keys(Keys.F12)#F12键

"""





















#driver.find_element_by_css_selector("").send_keys("")
#driver.find_element_by_css_selector("").click()
"""
class demo():
    def chandao(self,driver):
        driver.get("http://www.zhanlantest.com:81/zentao/user-login-L3plbnRhby8=.html")
        #print(driver.get_cookies())
        driver.delete_all_cookies()
        a={'domain': 'www.zhanlantest.com', 'httpOnly': False, 'name': 'windowWidth', 'path': '/zentao', 'secure': False, 'value': '929'}
        b= {'domain': 'www.zhanlantest.com', 'httpOnly': False, 'name': 'windowWidth', 'path': '/zentao/my', 'secure': False, 'value': '833'}
        c={'domain': 'www.zhanlantest.com', 'expiry': 1664011680, 'httpOnly': False, 'name': 'tab', 'path': '/zentao/', 'secure': False, 'value': 'my'}
        d={'domain': 'www.zhanlantest.com', 'httpOnly': False, 'name': 'windowHeight', 'path': '/zentao', 'secure': False,'value': '884'}
        e={'domain': 'www.zhanlantest.com', 'expiry': 1664011683, 'httpOnly': False, 'name': 'theme', 'path': '/zentao/', 'secure': False, 'value': 'default'}
        f={'domain': 'www.zhanlantest.com', 'expiry': 1664011683, 'httpOnly': True, 'name': 'device', 'path': '/zentao/', 'secure': False, 'value': 'desktop'}
        g={'domain': 'www.zhanlantest.com', 'httpOnly': False, 'name': 'windowHeight', 'path': '/zentao/my', 'secure': False, 'value': '844'}
        h={'domain': 'www.zhanlantest.com', 'expiry': 1664011683, 'httpOnly': False, 'name': 'lang', 'path': '/zentao/', 'secure': False, 'value': 'zh-cn'}
        i={'domain': 'www.zhanlantest.com', 'httpOnly': True, 'name': 'zentaosid', 'path': '/zentao/', 'secure': False, 'value': '055084c04c66247956be48cbaf57e57c'}

        driver.add_cookie(a)
        driver.add_cookie(b)
        driver.add_cookie(c)
        driver.add_cookie(d)
        driver.add_cookie(e)
        driver.add_cookie(f)
        driver.add_cookie(g)
        driver.add_cookie(h)
        driver.add_cookie(i)

        print(driver.get_cookies())
        for cookie in driver.get_cookies():
            print(cookie['name'],cookie['value'])
        #driver.find_elements_by_tag_name("input")[0].send_keys("admin")
        #driver.find_elements_by_tag_name("input")[1].send_keys("12345678admin")
        #driver.find_elements_by_tag_name("button")[1].click()
        sleep(5)
        #print(driver.get_cookies())
        print(driver.get_cookies())
        driver.refresh()
        print("第二段")
        for cookie in driver.get_cookies():
            print(cookie['name'],cookie['value'])
        #driver.add_cookie({'name': 'zentaosid', 'value': 'b4b35ce2e22f23c64a470eb307d62f58'})
        #driver.add_cookie({'name': 'zentaosid', 'value': 'b4b35ce2e22f23c64a470eb307d62f58'})
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/nav/ul[1]/li[6]/a/span").click()
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[2]/div[2]/iframe"))
        driver.find_element_by_xpath("/html/body/main/div/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a").click()
        driver.find_element_by_xpath("/html/body/main/div/div[1]/div[2]/a").click()
        #print(driver.get_cookies())
        #print(driver.get_cookies())
        #print(driver.get_cookies())


        #driver.find_element_by_xpath("/html/body/main/div/div[2]/div[3]/div[2]/a").click()#测试

        driver.find_element_by_xpath("/html/body/main/div/div/div/form/table/tbody/tr[10]/td/div/div/div[1]/button").click()
        sleep(2)
        os.system("d:\\a2.exe")

    def baidu(self,driver):
        driver.get("http://www.baidu.com")
        driver.set_window_size(600,600)
        sleep(5)
        js="window.scrollTo(10,10)"
        driver.execute_script(js)
    def xuanpin(self,driver):
        driver.get("http://192.168.6.191:9081")
        driver.set_window_size(600,600)
        sleep(5)
        driver.delete_all_cookies()
        print(driver.get_cookies())
        #driver.find_element_by_css_selector('[placeholder="用户名"]').send_keys("admin")
        #driver.find_element_by_css_selector('[placeholder="密码"]').send_keys("1234567")
        #driver.find_element_by_tag_name('button').click()
        sleep(3)
        a={'domain': '192.168.6.191', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': '86946982B8D34381A74BF660DE2EF930'}
        driver.add_cookie(a)
        print(driver.get_cookies())
        driver.refresh()
        driver.find_element_by_link_text('简历管理').click()
        driver.find_element_by_link_text('简历录入').click()
        print(driver.get_cookies())
    def chandao2(self,driver):
        driver.get("http://www.zhanlantest.com:81")
        driver.find_element_by_xpath("")
    def duqu(self,driver):
        user_file=open('d:\\ls\\555.txt','r')
        lines=user_file.readlines()
        user_file.close()
        for line in lines:
            username=line.split(',')[0]
            password=line.split(',')[1]
            print(username,password)
    def csv(self):
        import csv
        date=csv.reader(open("d:\\ls\\666.csv",'r'))
        for user in date:
            print(user)


"""
#demo().xuanpin()
#demo().baidu()
#demo().chandao()
#demo().csv()
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
#装饰器
@allure.epic("总描述,这是选聘系统的测试用例")
@allure.testcase('http://192.168.6.191:9081',name='选聘系统登录链接地址')
@allure.feature('登录用例')

class TestXuanpin():
    def setup_method(self, method):#前置方法（函数）
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.vars = {}

    def teardown_method(self, method):#后置方法（函数）
        self.driver.quit()

    @allure.title("1.验证用例名称是不是主题")
    @allure.story("1.验证正确的账号密码登录成功")
    @allure.step("1.输入正确的账号：admin和密码：1234567,点击登录")
    @allure.severity("trivial")
    def test_login(self):
        self.driver.get("http://192.168.6.191:9081/admin/loginUI")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("1234567")
        self.driver.find_element(By.ID, "submit").click()

        a=self.driver.find_element_by_xpath("/html/body/div[2]/header/nav/div/ul/li/a/span").text
        assert a=='湛蓝软件测试'

    @allure.title("2.验证用例名称是不是主题2")
    @allure.story("2.验证登录后的title是否正确")
    @allure.step("1.输入正确的账号：admin和密码为空,点击登录")

    @allure.severity("normal")
    def test_login2(self):
        self.driver.get("http://192.168.6.191:9081/admin/loginUI")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.NAME, "password").send_keys("1234567")
        self.driver.find_element(By.ID, "submit").click()
        assert self.driver.title=="选聘系统管理后台"

    @allure.title("3.验证用例名称是不是主题")
    @allure.story("3.验证正确的账号空的密码登录失败,并给出相关提示")
    @allure.step("1.账号和密码为空,点击登录")
    @allure.severity("blocker")
    def test_login3(self):
        self.driver.get("http://192.168.6.191:9081/admin/loginUI")

        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "username").send_keys("admin")
        self.driver.find_element(By.ID, "submit").click()
        b = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/p").text
        print("验证正确的账号空的密码登录失败,并给出相关提示")
        assert b=="密码不能为空!"
if __name__ == '__main__':
    pytest.main(['-s','demo3_email.py'])









