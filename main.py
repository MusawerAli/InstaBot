from selenium import webdriver
from time import sleep
from secrets import pwd
class InstBot:
    def __init__(self, username ,pwd):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pwd)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('//html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(3)

    def get_profile(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username)).click()
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_el, ht = 0, 1
        while last_el != ht:
            last_el = ht
            sleep(2)
            ht = self.driver.execute_script("""
                   arguments[0].scrollTo(0, arguments[0].scrollHeight);
                   return arguments[0].scrollHeight;
                   """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names


Insta_bot = InstBot('chmusawerali',pwd)

Insta_bot.get_profile()