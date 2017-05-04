'''
Created on May 4, 2017

@author: Wind
'''
# encoding: utf-8

import unittest

from common.wrapdrivermethod.initializebrowser import InitializeBrowser


class BaseTest(unittest.TestCase):


    def setUp(self):
        self.initializebrowser = InitializeBrowser()


    def tearDown(self):
        self.initializebrowser.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()