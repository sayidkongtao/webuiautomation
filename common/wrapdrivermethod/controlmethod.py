'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ControlMethod():
    
    def __init__(self, driver):
        self.driver = driver
        
    def click(self, webElementLocator, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.element_to_be_clickable(webElementLocator))
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).click()
    
    def sendKeys(self, value, webElementLocator, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.presence_of_element_located(webElementLocator))
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).sendKeys(value)
        
    def clear(self, webElementLocator, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.visibility_of_element_located(webElementLocator))
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).clear()
        
    def getText(self, self, webElementLocator, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.visibility_of_element_located(webElementLocator))
        return self.driver.find_element(webElementLocator[0], webElementLocator[1]).text
    
    # continue to add
