'''
Created on May 18, 2017

@author: Wind
'''
# encoding: utf-8
import os
PATH = lambda path : os.path.abspath(os.path.join(os.path.dirname(__file__), path))

import sys
sys.path.append(PATH(r"../../../webuiautomation"))


from web.ui.flow.loginflow import LoginFlow
from web.common.utility.automationlogger import autoLog
from selenium.common.exceptions import TimeoutException
import web.ui.flow.runlistflow
import json
import time
import shutil
from selenium import webdriver

stopTest = True

def getRunStatus():
    try:
        global stopTest
        
        if stopTest is not True:
            with open("runstatus.json","r") as f:
                dictRunStatus = json.loads(f.read())
        else:
            dictRunStatus = {} 
            # save the result timely
            with open("runstatus.json", "w") as f:
                f.write(json.dumps(dictRunStatus, indent=4, separators=(',', ': ')))   
            
        autoLog.info("init driver")
        driver = webdriver.Firefox(executable_path=PATH(r"../source/webdriver/firefox/geckodriver.exe"))
        driver.get('')
        
        loginFlow = LoginFlow(driver)
        dsFlow = loginFlow.login("", "")
        runListFlow = dsFlow.menuBar.navigateToRunList()
            
        # Run status
        
        stopRun = False
        
        # Get the run name from runname.json
        with open("runname.json", "r") as f:
            dictRunName = json.loads(f.read())
        
        autoLog.info("Get the run name: " + str(dictRunName["runName"]))
        
        while(stopRun is not True):
            stopRun = True
            for i in dictRunName["runName"]:
                tempList = dictRunStatus.get(i, {})
                try:
                    if runListFlow.getRunStatusByRunName(i) != "Complete":
                        stopRun = False
                        
                    # judge that key is exists
                    if not tempList.has_key(runListFlow.getRunStatusByRunName(i)):
                        tempList[runListFlow.getRunStatusByRunName(i)] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        dictRunStatus[i] = tempList
                        
                        # save the result timely
                        with open("runstatus.json", "w") as f:
                            f.write(json.dumps(dictRunStatus, indent=4, separators=(',', ': ')))
                except TimeoutException:
                    stopRun = False
                    autoLog.error("Cannot find the status of run: " + i + ", will find it again after refresh the browser")
            # refresh the browser after 5s 
            time.sleep(5)
            autoLog.info("refresh the browser after 5s")
            driver.refresh()
            web.ui.flow.runlistflow.RunListFlow(driver)
            
        backupFile = "runstatus" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".json";    
        shutil.copy("runstatus.json", backupFile)
        autoLog.info("back up the result to: " + backupFile)
        autoLog.info("complete the run status testing")
        stopTest = True
    except Exception as e:
        autoLog.error(str(e) + ", will rerun this test with previous run status")
        stopTest = False
        try:
            driver.quit()
        except:
            pass
        getRunStatus()

if __name__ == '__main__':
    getRunStatus()