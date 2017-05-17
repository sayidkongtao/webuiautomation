'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from selenium.webdriver.common.by import By


class Dashboard():
    
    @property
    def pageTitle(self):
        return (By.CSS_SELECTOR, ".page-title")
    