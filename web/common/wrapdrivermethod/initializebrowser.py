'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from web.common.utility.automationlogger import autoLog
from selenium import webdriver
import os


PATH = lambda path : os.path.abspath(os.path.join(os.path.dirname(__file__), path))

class InitializeBrowser():
    
    def __init__(self, timeout=120):
        autoLog.info("init web driver")
        # currently firefox is default
        self.driver = webdriver.Firefox(executable_path=PATH(r"../../source/webdriver/firefox/geckodriver.exe"))
        # self.browser.implicitly_wait(timeout);
        self.driver.get('')
        # to do create a configuration  profile and so on 
        # self.driver.find_element(by, value)
