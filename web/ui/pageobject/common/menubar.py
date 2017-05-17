'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from selenium.webdriver.common.by import By

class MenuBar():
    
    @property
    def dashboard(self):
        return (By.CSS_SELECTOR, "a[ng-href='/dashboard']")
    
    @property
    def prep(self):
        return (By.CSS_SELECTOR, "a[ng-href='/lab']")
    
    @property
    def runs(self):
        return (By.CSS_SELECTOR, "a[ng-href='/runs']")