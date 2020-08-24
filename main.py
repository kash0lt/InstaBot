from time import sleep
from selenium import webdriver


class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
#        self.driver = webdriver.Firefox()
        self.driver.get("https://instagram.com")
        sleep(3)
#        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
#        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            sleep(1)
        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            sleep(1)
        sleep(2)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()

        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        not_following_back.sort()
        print(not_following_back)
        return not_following_back

    def _get_names(self):
        sleep(2)
#        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
#        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
#        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names


my_bot = InstaBot('***', '***')
no_follow = my_bot.get_unfollowers()
del my_bot
with open("not_follow.txt", "w") as f:
    f.write("Instagram people I follow that do not follow back:\n")
    for person in no_follow:
        f.write("@" + person + "\n")
