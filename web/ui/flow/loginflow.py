'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.login import Login as LoginPageElements


class LoginFlow():
    
    def __init__(self, driver, checkURL = False):
        #configuration
        self.username = "username" 
        self.password = "password"
        self.elements = LoginPageElements()
        self.controlMethod = ControlMethod(driver)
        self.onPageLoad(checkURL)
    
    def onPageLoad(self, checkURL = False):
        pass
            
    def login(self):
        self.controlMethod.click(self.elements.signInButton)
        self.controlMethod.sendKeys(self.username, self.elements.userNameTextBox)
        self.controlMethod.sendKeys(self.username, self.elements.passwordTextBox)
        self.controlMethod.click(self.elements.signInButton)
        return 
    