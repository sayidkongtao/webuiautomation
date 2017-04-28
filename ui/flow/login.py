'''
Created on Apr 28, 2017

@author: Wind
'''
# encoding: utf-8

from ui.pageobject.login import Login as LoginPageElements
from common.wrapdrivermethod.initializebrowser import InitializeBrowser

class Login():
    
    def __init__(self, username, password, basespaceTest):
        self.username = username 
        self.password = password
        self.basespaceTest = basespaceTest
        self.elements = LoginPageElements()
        self.initializeBrowser = InitializeBrowser();
        
    
        
        
    