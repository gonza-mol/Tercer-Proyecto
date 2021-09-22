from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class LandingPageLocators():
    go_Login = (By.CSS_SELECTOR, "#customer_menu_top>li>a")
    label_name = (By.CSS_SELECTOR, "#customer_menu_top>li>a>div")
    label_My_Wish_List = (By.CSS_SELECTOR, "#customer_menu_top>li>ul>li:nth-child(2)>a>i")

class LandingPage():

    def __init__(self, driver):
        self.driver = driver

    def click_Go_Login(self):
        self.driver.find_element(*LandingPageLocators.go_Login).click()

    def verificar_Nombre_Landing_Page(self):
        return self.driver.find_element(*LandingPageLocators.label_name).text

    def Select_My_Wish_List_Option(self):
        hover = ActionChains(self.driver).move_to_element(self.driver.find_element(*LandingPageLocators.label_name))
        hover.perform()
        self.driver.find_element(*LandingPageLocators.label_My_Wish_List).click()


