import re
import time
import pytest
import driver as driver
from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from functools import partial
from pytest_bdd import scenarios, given, when, then
from colorama import Fore, Back, Style

from POM.LandingPage import LandingPage
from POM.LoginPage import LoginPage
from POM.MyAccountPage import MyAccountPage
from POM.LipsPage import LipsPage
from POM.ProductPage import ProductPage
from POM.ShoppingCartPage import ShoppingCartPage
from POM.CheckoutConfirmationPage import CheckoutConfirmationPage
from POM.My_Order_History import My_Order_History
from POM.ContactUsPage import ContactUsPage
import HtmlTestRunner
import logging
from Utils import utils as utils

@pytest.mark.slow
@pytest.mark.usefixtures("test_setup")
class TestVerifyOrder():


    def test_Verify_ContactUsForm(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        # ir a login page
        lp = LandingPage(driver)
        lp.click_Go_Login()
        logpa = LoginPage(driver)
        time.sleep(2)
        # Esto permite el logueo
        logpa.do_Login("gonza_mol", "Chicharito10")

        account = MyAccountPage(driver)
        account.seleccionar_ContactUs_Option()
        time.sleep(2)
        cu = ContactUsPage(driver)
        print(cu.verificar_ContactUs_Form())
        time.sleep(2)
        assert cu.verificar_ContactUs_Form() == "Contact Us Form"
        print(Fore.GREEN + "Estoy en la página de Contact Us")
        time.sleep(2)
        cu.fill_FirstName("gonza")
        time.sleep(2)
        cu.fill_Email("gonzalo.molina@darwoft.com")
        time.sleep(2)
        cu.fill_Enquiry("Por favor me pueden regalar un millón de pesos?")
        time.sleep(2)
        cu.sendForm()

        message = cu.Verify_Enquiry_Success()
        assert message == "Your enquiry has been successfully sent to the store owner!"



        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Reports'), verbosity=2)



