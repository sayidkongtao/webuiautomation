'''
Created on May 4, 2017

@author: Wind
'''
# encoding: utf-8
from base.basetest import BaseTest
from web.ui.flow.loginflow import LoginFlow


class LoginTest(BaseTest):
    
    def test_Login(self):
        loginFlow = LoginFlow(self.initializebrowser.driver)
        dsFlow = loginFlow.login()
        runListFlow = dsFlow.menuBar.navigateToRunList()
        print runListFlow.getRunStatusByRunName("HiSeq_WG")