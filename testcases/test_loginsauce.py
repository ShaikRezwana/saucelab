import pytest
from selenium import webdriver
import time
import logging

from pageObjects.loginsauce import LoginSauce
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen

class Test_01_sauce:

    baseurl=Readconfig.getbaseurl()
    username=Readconfig.enterusername()
    password=Readconfig.enterpassword()

    logger=LogGen.loggen()

    def test_title(self,setup):
        self.logger.info("------ Verifying Sauce Labs page -----")
        self.logger.info("------- test_tile TC started --------")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Swag Labs":
            assert True
            self.logger.info("------ act_tile is equal to expected title ----")
        else:
            self.driver.save_screenshot(r"C:\\Users\\rezwana.shaik\\PycharmProjects\\sauce.py\\screenshots\\" + "Test_01_sauce.png")
            self.logger.error(" act_title doesnt match with exp_title-----")
            assert False
        self.driver.close()
        print(act_title)

    def test_saucelogin(self,setup):
        self.logger.info("----- Verify login function ------")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginSauce(self.driver)
        self.lp.enter_username(self.username)
        time.sleep(3)
        self.lp.enter_password(self.password)
        time.sleep(3)
        self.lp.click_login()
        time.sleep(3)
        self.lp.click_options()
        time.sleep(3)
        self.lp.click_logout()
        self.logger.info("------ Successfully logged into sauce labs -----")
        time.sleep(10)