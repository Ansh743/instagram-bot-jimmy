# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from random import randint
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
    
    def srch_tags():
        #
        
def main():
    jimmy = Bot()
    
if __name__ == '__main__':
    main()