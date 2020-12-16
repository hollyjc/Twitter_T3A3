from dotenv import load_dotenv
load_dotenv()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        twitter_password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.usermame)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    
    def like_tweet(self,hashtag):
        bot = self.bot
        botbot.get('https://twitter.com/search?q=' + hash '%23otter&src=typed_query')


otter_twitter= TwitterBot('email', 'password')
otter_twitter.login()