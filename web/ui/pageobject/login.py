'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8
from selenium.webdriver.common.by import By


class Login():
    
    @property
    def userNameTextBox(self):
        return (By.CSS_SELECTOR, "input.ng-valid-email")
    
    @property
    def passwordTextBox(self):
        return (By.XPATH, "//input[contains(@name, 'password')]")
    
    @property
    def signInButton(self):
        return (By.XPATH, "//input[contains(@class, 'btn btn-primary js-loader')]")
    
    @property
    def homePageLogInButton(self):
        return (By.ID, "sign-in-btn")
    
    @property
    def homePageDeveloperPortalLink(self):
        return (By.CSS_SELECTOR, "(href*='https://developer')")
    
    @property
    def acceptAgreementButton(self):
        return (By.LINK_TEXT, "I Accept These Agreements")
    
