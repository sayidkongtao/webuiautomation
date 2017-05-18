'''
Created on May 4, 2017

@author: Wind
'''
# encoding: utf-8
from base.basetest import BaseTest
from web.ui.flow.loginflow import LoginFlow
from web.common.utility.automationlogger import autoLog
from selenium.common.exceptions import TimeoutException
import json
import time
import shutil

class LoginTest(BaseTest):
    
    def Login(self):
        loginFlow = LoginFlow(self.initializebrowser.driver)
        dsFlow = loginFlow.login()
        runListFlow = dsFlow.menuBar.navigateToRunList()
        print runListFlow.getRunStatusByRunName("HiSeq_WG")
        
    def test_tempRun(self):
        loginFlow = LoginFlow(self.initializebrowser.driver)
        dsFlow = loginFlow.login()
        runListFlow = dsFlow.menuBar.navigateToRunList()
        
        #Run status
        dictRunStatus= {}
        stopRun = False
        
        #Get the run name from runname.json
        with open("runname.json","r") as f:
            dictRunName = json.loads(f.read())
        
        autoLog.info("Get the run name: " + str(dictRunName["runName"]))
        
        while(stopRun is not True):
            stopRun = True
            
            for i in dictRunName["runName"]:
                try:
                    tempList = {}
                    
                    if runListFlow.getRunStatusByRunName(i) != "Complete":
                        stopRun = False
                        
                    #judge that key is exists
                    if not tempList.has_key(runListFlow.getRunStatusByRunName(i)):
                        tempList[runListFlow.getRunStatusByRunName(i)] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        dictRunStatus[i] = tempList
                        
                        #save the result timely
                        with open("runstatus.json","w") as f:
                            f.write(json.dumps(dictRunStatus, indent=4, separators=(',', ': ')))
                except TimeoutException:
                    autoLog.error("Cannot find the status of run: " + i)
            #refresh the browser after 5s 
            time.sleep(5)
            self.initializebrowser.driver.refresh()
            
        shutil.copy("runstatus.json", "runstatus" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".json")    
            
            
        
        