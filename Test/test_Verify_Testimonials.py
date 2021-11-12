from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
import pytest
import sys
import os

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
import logging
from Utils import utils as utils
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup")
class TestVerify_Testimonials():


    def test_Verify_Testimonials(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)
        driver.execute_script("window.scrollTo(0, 4000)")
        t = account.getTestimonials()
        # print("Cantidad de elementos: "+str(len(t)))
        lista1 = ['Sub_cero', '1er', '2do', '3er', '4to', '5to']
        n = 0
        for test in t:
            if n == 0 or n == 5:
                n = n + 1
            else:
                assert test.text in "Regular customer and products" or "Returns were easy and my" or "I found this store to be very reasonably" or "Really great products"
                print(Fore.GREEN + "El título del " + lista1[n] + " Testimonials es: " + Fore.RESET + test.text)
                # time.sleep(7)
                n = n + 1
                time.sleep(7)

            # lista1.append(test.text)






    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
