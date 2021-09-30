import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ShampooPageLocators():
    btn_AddCartBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.thumbnail>div.pricetag.jumbotron>a>i")
    lbl_priceBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.thumbnail>div.pricetag.jumbotron>div>div")
    btn_AddCartPantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>a>i")
    lbl_pricePantene = (By.CSS_SELECTOR, "div:nth-child(2)>div.thumbnail>div.pricetag.jumbotron>div>div")
    lbl_titleBulgary = (By.CSS_SELECTOR, "div:nth-child(1)>div.fixed_wrapper>div>a")
    lbl_titlePantene = (By.CSS_SELECTOR, " div:nth-child(2)>div.fixed_wrapper>div>a")

class ShampooPage():

    def __init__(self, driver):
        self.driver = driver



    def add_Fragance(self):
        self.driver.find_element(*ShampooPageLocators.btn_AddCartBulgary).click()

    def get_PriceFragance(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_priceBulgary).text

    def add_Pantene(self):
        self.driver.find_element(*ShampooPageLocators.btn_AddCartPantene).click()

    def get_PricePantene(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_pricePantene).text

    def get_TitleFragance(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_titleBulgary).text

    def get_TitlePantene(self):
        return self.driver.find_element(*ShampooPageLocators.lbl_titlePantene).text



