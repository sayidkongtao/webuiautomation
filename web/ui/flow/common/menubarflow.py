'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.common.menubar import MenuBar as menubarElments
# PLEASE NOTE: Don't directly use following flow type
# following modules just loaded as type reference, the real module will be loaded in runtime
# so that we can avoid the circular dependecy issue
import web.ui.flow.dashboardflow
import web.ui.flow.runlistflow

class MenuBarFlow:
    
    def __init__(self, driver):
        #configuration
        self.__driver = driver
        self.__elements = menubarElments()
        self.__controlMethod = ControlMethod(driver)

        
    def navigateToDashboard(self):
        autoLog.info("Click Dashboard button on main menu")
        self.__controlMethod.click(self.__elements.dashboard)
        
        autoLog.info("Get Dashboard Flow")
        return web.ui.flow.dashboardflow.DashboardFlow(self.__driver)
     
    def navigateToRunList(self):
        autoLog.info("Click RUNS button on main menu")
        self.__controlMethod.click(self.__elements.runs)
        
        autoLog.info("Get RunList Flow")
        return web.ui.flow.runlistflow.RunListFlow(self.__driver) 