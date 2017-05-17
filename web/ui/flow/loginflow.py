'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.login import Login as LoginPageElements


class LoginFlow():
    
    def __init__(self, driver, checkURL = False):
        #configuration
        self.username = "" 
        self.password = ""
        self.elements = LoginPageElements()
        self.controlMethod = ControlMethod(driver)
        self.onPageLoad(checkURL)
    
    def onPageLoad(self, checkURL = False):
        pass
            
    def login(self):
        autoLog.info("Click Login Button on Home screen")
        self.controlMethod.click(self.elements.homePageLogInButton)
        autoLog.info("Click Login sign in button on login screen")
        self.controlMethod.click(self.elements.signInButton)
        autoLog.info("Input uername")
        self.controlMethod.sendKeys(self.username, self.elements.userNameTextBox)
        autoLog.info("Input password")
        self.controlMethod.sendKeys(self.password, self.elements.passwordTextBox)
        autoLog.info("Click the signin")
        self.controlMethod.click(self.elements.signInButton)
        return 
    