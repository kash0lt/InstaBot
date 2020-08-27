from time import sleep
from selenium import webdriver
from twittersec import TwitAuth


class TwitterBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
#        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com/login")
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input").send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div").click()
        sleep(2)
        # try:
        #     self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        # except:
        #     sleep(1)
        # sleep(2)

    def follower_count(self, page):
        self.driver.get("https://twitter.com/" + page)
        sleep(5)
        following_count = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a").get_attribute("title")
        followers_count = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a").get_attribute("title")

        return (int(following_count) - int(followers_count))


Auth = TwitAuth()
my_bot = TwitterBot(Auth.username, Auth.password)
twit_follows = my_bot.follower_count(Auth.username)
print(twit_follows)
del my_bot
if (twit_follows > 0):
    print("You follow more than follow back.")
else:
    print("More or equal number of people follow you as you follow.")
