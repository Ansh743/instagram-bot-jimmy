# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from credentials import id,pswd

class Bot(): 
    def __init__(self):
        self.login(id)
        
    def login(self, id):
        self.driver = webdriver.Chrome(r'.\chromedriver.exe')   
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.send_keys(id)
        password_input = self.driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.send_keys(pswd)
        submit_btn = self.driver.find_element_by_xpath(
            "//button[@type='submit']")
        submit_btn.click()
        sleep(5)
        not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_btn.click()
        sleep(5)
        not_now_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_btn.click()
    
    def srch_tags(self, tags, after):
        allTags = list()
        for each in tags:
            for every in after:
                allTags.append(each+every)
                
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
        search_bar.click()
        sleep(0.5)
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.click()
        
        for each in allTags:
            search_bar.send_keys('#'+each)
            sleep(3)
            tag = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
            tag.click()
            sleep(3)
            for x in range(1,4):
                for y in range(1,4):
                    currentPost = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+str(x)+']/div['+str(y)+']/a/div')

                    currentPost.click()
                    sleep(2)
                    
                    like_button = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    like_button.click()
                    
                    sleep(0.5)
                    close = self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/button')
                    close.click()
        

        
        
def main():
    jimmy = Bot()
    tags = ['car', 'bike', 'plane', 'helicopter']
    after = ['love', 'lover']
    jimmy.srch_tags(tags, after)
    
    
if __name__ == '__main__':
    main()