'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.dashboard import Dashboard as DashboardElements


class DashboardFlow():
    
    def __init__(self, driver, checkURL = False):
        #configuration
        self.elements = DashboardElements()
        self.controlMethod = ControlMethod(driver)
        self.onPageLoad(checkURL)

    def onPageLoad(self,checkURL):
        autoLog.info("Wait for dashboard loaded")
        