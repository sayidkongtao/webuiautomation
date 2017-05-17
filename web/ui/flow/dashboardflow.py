'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.dashboard import Dashboard as DashboardElements
from web.ui.flow.common.menubarflow import MenuBarFlow

class DashboardFlow():
    
    def __init__(self, driver, checkURL=False):
        # configuration
        self.__elements = DashboardElements()
        self.__controlMethod = ControlMethod(driver)
        self.__onPageLoad(checkURL)
        self.menuBar = MenuBarFlow(driver)
        
    def __onPageLoad(self, checkURL):
        autoLog.info("Wait for dashboard loaded")
        self.__controlMethod.waitForEleToBeDisplayed(self.__elements.pageTitle)
        # to do contains url if checkURL is true
        
