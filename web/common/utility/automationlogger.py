'''
Created on May 16, 2017

@author: Wind
'''
# encoding: utf-8
import logging.handlers
import os
#########################################
#logger operation
# StreamHandler
#FileHandler
#########################################

# Basic Path ---------------------------------------------------------------
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class UIControl_Log():
    def __init__(self,log_name = None,loglevel = logging.INFO,backup_file_path = PATH(r"../../testreport/automationlog/log.log")):
        self.logger = logging.getLogger()
        
        if len(self.logger.handlers) == 0:
            #create handler, to save the log to file "bat_fw_log/log.log"
            File_handler = logging.handlers.RotatingFileHandler(filename=backup_file_path,maxBytes=1024*1024*10,backupCount=5,encoding="utf-8")          
            #create handler, to print log to control Panel
            control_hander = logging.StreamHandler()            
            # Set format for handler
            formatter = logging.Formatter("%(asctime)s-%(name)s-%(module)s-%(lineno)d -%(levelname)s-%(message)s ")
            File_handler.setFormatter(formatter)
            control_hander.setFormatter(formatter)
            # add handler to logger
            self.logger.addHandler(File_handler)
            self.logger.addHandler(control_hander)        
        self.logger.setLevel(loglevel)
        
    def getlog(self):
        return self.logger
    
    def setLogLevel(self,level):
        self.logger.setLevel(level)
     
autoLog = UIControl_Log().getlog()