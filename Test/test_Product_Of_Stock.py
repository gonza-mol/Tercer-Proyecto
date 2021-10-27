import re
import time
import pytest
import driver as driver
from pytest_bdd.parsers import string
from selenium import webdriver
import unittest
import sys
import os

from selenium.common.exceptions import NoSuchElementException

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
class TestProductOfStock():


    def test_Product_Of_Stock(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(2)
        my = MyAccountPage(driver)
        my.seleccionar_Producto_Books_Paperback()
        driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(2)
        pp = ProductPage(driver)
        leyend = pp.getLblOutofStock()
        title = pp.getTitleofPaperbackWithoutStock()
        assert "OUT OF STOCK" == leyend
        #este de assert de abajo lo que hace es traer el objeto del btn que dice out of stock y con el método
        #is_displayed() lo que hace es devolver un true si existe y false si no y ahi lo compara con el True
        assert pp.getObjectOutofStock().is_displayed() == True
        #Este print de abajo trae el componente que tiene out of stock y con el método value_of_css_property
        #capta el atributo que se llama background que es el color del fondo del label que dice out of stock
        color = pp.getObjectOutofStock().value_of_css_property('background')
        colorOutofStock = color[0:18]
        print(Fore.YELLOW +"El color del label de Out of Stock es: ----> "+colorOutofStock)
        #este assert de abajo lo que hace es verificar que el color de fondo del lable de out of stock
        #su color es convertido en rgb y eso significa color gris, y hago un assert para ver si ese
        #color coincide con lo del label
        assert 'rgb(204, 204, 204)' in pp.getObjectOutofStock().value_of_css_property('background')

        print(Fore.GREEN +"El producto seleccionado es :"+title+" y está "+leyend+" y el color es :"+colorOutofStock)
        try:
            btnAddCart = driver.find_element_by_css_selector("div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>a")
            btnAddCart.click()
            print(Fore.RED + "El btn ADD TO CART se está visualizando en el producto seleccionado y no debería")

        except NoSuchElementException as e:
            print(Fore.GREEN + "El botón ADD TO CART No está")
            print(e)




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)

