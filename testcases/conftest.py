import os

import pytest
from selenium import webdriver
import configparser

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("----chrome launched----")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("-----firefox launched-----")
    else:
        driver=webdriver.Ie()
        print("------ Ie Launched------ ")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(pytestconfig):
     pytestconfig._metadata["project name"] =os.environ["login sauce page"]
     pytestconfig._metadata["Module name"] = os.environ["login"]
     pytestconfig._metadata["tester"] = os.environ["Rezwana"]

