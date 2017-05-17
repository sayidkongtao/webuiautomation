'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.login import Login as LoginPageElements
from web.ui.flow.dashboardflow import DashboardFlow

class LoginFlow():
    
    def __init__(self, driver, checkURL = False):
        #configuration
        self.__driver = driver
        self.__username = "kongtao01@beyondsoft.com" 
        self.__password = "Kt123456"
        self.__elements = LoginPageElements()
        self.__controlMethod = ControlMethod(driver)
        self.__onPageLoad(checkURL)
    
    def __onPageLoad(self, checkURL = False):
        pass
            
    def login(self):
        autoLog.info("Click Login Button on Home screen")
        self.__controlMethod.click(self.__elements.homePageLogInButton)
        autoLog.info("Click Login sign in button on login screen")
        self.__controlMethod.click(self.__elements.signInButton)
        autoLog.info("Input uername")
        self.__controlMethod.sendKeys(self.__username, self.__elements.userNameTextBox)
        autoLog.info("Input password")
        self.__controlMethod.sendKeys(self.__password, self.__elements.passwordTextBox)
        autoLog.info("Click the signin")
        self.__controlMethod.click(self.__elements.signInButton)
        
        autoLog.info("Get Dashboard flow")
        return DashboardFlow(self.__driver)
    