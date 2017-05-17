'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8

from selenium.webdriver.common.by import By

class RunList():
    
    @property
    def runPageTitle(self):
        return (By.CSS_SELECTOR, ".page-title")
    
    
    def runLinkByRunName(self, runName):
        return (By.XPATH, "//div[contains(@class, 'bs-runs-name')]/a[text() = '" + runName + "']")
    
    
    def runStatus(self, runName):
        return (By.XPATH, "//div[contains(@class, 'bs-runs-name')]/a[text() = '" + runName + "']/ancestor::tr/td[12]//span")

