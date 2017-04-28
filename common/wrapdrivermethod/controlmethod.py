'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from initializebrowser import InitializeBrowser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ControlMethod():
    
    def __init__(self):
        self.initializebrowser = InitializeBrowser()
        
    def click(self, webElementLocator, timeout=15):
        WebDriverWait(self.initializebrowser.driver, timeout, poll_frequency=0.5, ignored_exceptions=None).until(EC.element_to_be_clickable(webElementLocator))
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).click()
    
    def sendKeys(self, webElementLocator, timeout=15):
        WebDriverWait(self.initializebrowser.driver, timeout, poll_frequency=0.5, ignored_exceptions=None).until(EC.presence_of_element_located(webElementLocator))
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).sendKeys()
        
    