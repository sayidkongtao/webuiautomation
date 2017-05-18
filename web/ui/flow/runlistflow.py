'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8

from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.runlist import RunList as RunListElements

class RunListFlow():
    
    def __init__(self, driver, checkURL = False):
        self.__elements = RunListElements()
        self.__controlMethod = ControlMethod(driver)
        self.__onPageLoad(checkURL)
        
    def __onPageLoad(self, checkURL):
        autoLog.info("Wait for runlist flow loaded")
        self.__controlMethod.waitForEleToBeDisplayed(self.__elements.runPageTitle)
        
    def getRunStatusByRunName(self, runName):
        autoLog.info("Get status of run: " + runName)
        return self.__controlMethod.getText(self.__elements.runStatus(runName),timeout= 60)
        