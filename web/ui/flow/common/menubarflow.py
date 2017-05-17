'''
Created on May 17, 2017

@author: Wind
'''
# encoding: utf-8
from web.common.utility.automationlogger import autoLog
from web.common.wrapdrivermethod.controlmethod import ControlMethod
from web.ui.pageobject.common.menubar import MenuBar as menubarElments



class MenuBarFlow:
    
    def __init__(self, driver, checkURL = False):
        #configuration
        self.elements = menubarElments()
        self.controlMethod = ControlMethod(driver)

        
    def navigateToDashboard(self):
        autoLog.info("Click Dashboard button on main menu")
        self.controlMethod.click(self.elements.dashboard)
        return 
    