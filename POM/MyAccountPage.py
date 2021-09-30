import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style
from selenium.webdriver.common.keys import Keys


class MyAccountPageLocators():
      text_my_account1 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.subtext")
      text_my_account2 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext")
      btn_continue_register3 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>section>a")
      text_account_created = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>h1>span.maintext>i")
      makeup_btn = (By.CSS_SELECTOR, "#categorymenu>nav>ul>li:nth-child(3)>a")
      lips_option = (By.CSS_SELECTOR, "#categorymenu>nav>ul>li:nth-child(3)>div>ul:nth-child(1)>li:nth-child(4)>a")
      cart_option = (By.CSS_SELECTOR, "#main_menu_top>li:nth-child(3)>a>span")
      skincare_btn = (By.XPATH, "//body/div[1]/div[1]/div[1]/section[1]/nav[1]/ul[1]/li[4]/a[1]")
      welcomeback_btn = (By.CSS_SELECTOR, "#customer_menu_top>li>a>div")
      logoff = (By.CSS_SELECTOR, "#customer_menu_top>li>ul>li:nth-child(10)")
      searchbox = (By.ID, "filter_keyword")
      execute_search = (By.CSS_SELECTOR, "#search_form>div>div>i")
      footer = (By.CSS_SELECTOR, "#footer>footer>section.footersocial>div>div")
      link_ContactUs = (By.CSS_SELECTOR, "div.pull-left>div>ul>li:nth-child(5)>a")
      hair_care_btn = (By.CSS_SELECTOR, "#categorymenu>nav>ul>li:nth-child(7)>a")
      shampoo_option = (By.CSS_SELECTOR, "li:nth-child(7)>div>ul:nth-child(1)>li:nth-child(2)>a")
      itemBox = (By.CSS_SELECTOR, "div.container-fluid>div>div.block_7>ul>li>a")
      itemFragance = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td.name>a")
      itemShampoo = (By.CSS_SELECTOR, "tbody>tr:nth-child(2)>td.name>a")



class MyAccountPage():

    def __init__(self, driver):
        self.driver = driver

    def verificar_Ingreso_Correcto1(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account1).text

    def verificar_Ingreso_Correcto2(self):
        return self.driver.find_element(*MyAccountPageLocators.text_my_account2).text

    def continue_Account3(self):
        self.driver.find_element(*MyAccountPageLocators.btn_continue_register3).click()

    def verificar_Created_Account_Success(self):
        return self.driver.find_element(*MyAccountPageLocators.text_account_created).text

    def seleccionar_Producto_Makeup(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.makeup_btn))
        hover.perform()
        self.driver.find_element(*MyAccountPageLocators.lips_option).click()


    def seleccionar_Cart_Option(self):
        self.driver.find_element(*MyAccountPageLocators.cart_option).click()

    def seleccionar_Producto_SkinCare(self):
        self.driver.find_element(*MyAccountPageLocators.skincare_btn).click()

    def seleccionar_Logoff(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.welcomeback_btn))
        hover.perform()
        self.driver.find_element(*MyAccountPageLocators.logoff).click()

    def seleccionar_Búsqueda(self, product):
        self.driver.find_element(*MyAccountPageLocators.searchbox).click()
        self.driver.find_element(*MyAccountPageLocators.searchbox).send_keys(product)

    def ejecutar_Búsqueda_Glass(self):
        self.driver.find_element(*MyAccountPageLocators.execute_search).click()


    def ejecutar_Búsqueda_Enter(self, product):
        self.driver.find_element(*MyAccountPageLocators.searchbox).click()
        self.driver.find_element(*MyAccountPageLocators.searchbox).send_keys(product + Keys.RETURN)


    def contar_Footer_Component(self):
        elements = len(self.driver.find_elements(*MyAccountPageLocators.footer))
        return elements

    def mostrar_Footer_Component(self):
        #elements = self.driver.find_elements(*MyAccountPageLocators.footer)
        ele = self.driver.find_elements(*MyAccountPageLocators.footer)
        return ele
        #for ele_foo in ele:
           #print(ele_foo.text)

    def seleccionar_ContactUs_Option(self):
        self.driver.find_element(*MyAccountPageLocators.link_ContactUs).click()


    def seleccionar_Producto_Makeup(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.hair_care_btn))
        hover.perform()
        self.driver.find_element(*MyAccountPageLocators.shampoo_option).click()

    def select_HairCare_Shampoo(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.hair_care_btn))
        hover.perform()
        self.driver.find_element(*MyAccountPageLocators.shampoo_option).click()

    def open_ItemBox (self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*MyAccountPageLocators.itemBox))
        hover.perform()



    def get_TitleFragance(self):
        return self.driver.find_element(*MyAccountPageLocators.itemFragance).text

    def get_TitleShampoo(self):
        return self.driver.find_element(*MyAccountPageLocators.itemShampoo).text
