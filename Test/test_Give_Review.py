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
from POM.ShampooPage import ShampooPage
import HtmlTestRunner
import logging
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestGiveReview():


    def test_Give_Review(self):
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
        my = MyAccountPage(driver)
        my.select_HairCare_Shampoo()
        time.sleep(4)
        sp = ShampooPage(driver)
        time.sleep(4)
        sp.viewPantene()
        time.sleep(4)
        sp.selectReview()
        time.sleep(4)
        sp.setCalification()
        time.sleep(4)
        sp.setName("Gonzalo")
        time.sleep(4)
        sp.setReview("Me gusta este perfume, pero me causó una reacción alérgica")
        time.sleep(4)
        sp.clickSubmitBtn()
        time.sleep(4)
        error = sp.errorWithoutCode()
        assert "Human verification has failed! Please try again." in sp.errorWithoutCode()
        print("Al no cargar el código requerido, se está mostrando un mensaje de error: "+sp.errorWithoutCode())





    if __name__ == '__main__':
         unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
