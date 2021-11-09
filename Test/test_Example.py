from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from functools import partial
from pytest_bdd import scenarios, parsers, given, when, then, scenario
from colorama import Fore, Back, Style
import time
from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.ProductPage import ProductPage
from POM.MyAccountPage import MyAccountPage
import conftest
import HtmlTestRunner
from Utils import utils as utils
import logging

@pytest.mark.usefixtures("test_setup")
class TestGiveReview():

    def test_setUpClass(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        title = driver.title
        print(title)
        currenturl = driver.current_url
        print(currenturl)
        driver.get("https://courses.letskodeit.com/login")
        currenturl = driver.current_url
        print(currenturl)
        time.sleep(2)
        driver.back()
        currenturl = driver.current_url
        print(currenturl)
        time.sleep(2)
        driver.forward()
        currenturl = driver.current_url
        print(currenturl)
