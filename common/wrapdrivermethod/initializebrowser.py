'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from selenium import webdriver

class InitializeBrowser():
    
    def __init__(self, timeout = 120):
        #currently firefox is default
        self.driver = webdriver.Firefox()
        #self.browser.implicitly_wait(timeout);
        self.driver.get('https://cloud-hoth.illumina.com')
        # to do create a configuration  profile and so on 
        #self.driver.find_element(by, value)