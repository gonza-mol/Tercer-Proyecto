import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style
from selenium.webdriver.common.keys import Keys


class ContactUsPageLocators():
    label_ContactUsTitle = (By.CSS_SELECTOR, "#ContactUsFrm>h3")
    text_FirstName = (By.CSS_SELECTOR, "#ContactUsFrm_first_name")
    text_Email = (By.ID, "ContactUsFrm_email")
    text_Enquiry = (By.ID, "ContactUsFrm_enquiry")
    btn_SubmitForm = (By.CSS_SELECTOR, "div.col-md-6.col-sm-6>button")
    label_Enquiry_Ok = (By.CSS_SELECTOR, "p:nth-child(3)")


class ContactUsPage():

    def __init__(self, driver):
        self.driver = driver

    def verificar_ContactUs_Form(self):
        return self.driver.find_element(*ContactUsPageLocators.label_ContactUsTitle).text

    def fill_FirstName(self, name):
        self.driver.find_element(*ContactUsPageLocators.text_FirstName).click()
        self.driver.find_element(*ContactUsPageLocators.text_FirstName).send_keys(name)

    def fill_Email(self, email):
        self.driver.find_element(*ContactUsPageLocators.text_Email).click()
        self.driver.find_element(*ContactUsPageLocators.text_Email).send_keys(email)

    def fill_Enquiry(self, message):
        self.driver.find_element(*ContactUsPageLocators.text_Enquiry).click()
        self.driver.find_element(*ContactUsPageLocators.text_Enquiry).send_keys(message)

    def sendForm(self):
        self.driver.find_element(*ContactUsPageLocators.btn_SubmitForm).click()

    def Verify_Enquiry_Success(self):
        return self.driver.find_element(*ContactUsPageLocators.label_Enquiry_Ok).text
