'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from web.common.utility.automationlogger import autoLog
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ControlMethod():
    
    def __init__(self, driver):
        self.driver = driver
        
    def delayTodo(self, delaytime=0):
        if delaytime > 0:
            time.sleep(delaytime)
        
    def click(self, webElementLocator, delaytime=0, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        autoLog.info("Click: " + str(webElementLocator))
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.element_to_be_clickable(webElementLocator))
        self.delayTodo(delaytime)
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).click()
    
    def sendKeys(self, value, webElementLocator, delaytime=0, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        autoLog.info("Input: " + value +"__" + str(webElementLocator))
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.presence_of_element_located(webElementLocator))
        self.delayTodo(delaytime)
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).send_keys(value)
        
    def clear(self, webElementLocator, delaytime=0, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        autoLog.info("Clear: "+ webElementLocator.tostring())
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.visibility_of_element_located(webElementLocator))
        self.delayTodo(delaytime)
        self.driver.find_element(webElementLocator[0], webElementLocator[1]).clear()
        
    def getText(self, webElementLocator, delaytime=0, timeout=15, poll_frequency=0.5, ignored_exceptions=None):
        autoLog.info("Get text: " + str(webElementLocator))
        WebDriverWait(self.driver, timeout, poll_frequency, ignored_exceptions).until(EC.visibility_of_element_located(webElementLocator))
        self.delayTodo(delaytime)
        return self.driver.find_element(webElementLocator[0], webElementLocator[1]).text
    
    # continue to add
