import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import logging
class add_Card():

    def __init__(self, driver):
        self.driver = driver
        self.woman = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
        self.clickonitem = "//div[@class='right-block']//a[@class='product-name'][contains(text(),'Blouse')]"
        self.additemtocard = "//span[contains(text(),'Add to cart')]"
        self.proceedtocheckout = "//span[contains(text(),'Proceed to checkout')]"
        self.proceedtocheckoutt = "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]"
        self.enteremail = "//input[@id='email']"
        self.enterpassword= "//input[@id='passwd']"
        self.login = "//span[contains(text(),'Sign in')]"
        self.enterfirstname = "//input[@id='firstname']"
        self.enterlastname = "//input[@id='lastname']"
        self.entercompanyname = "//input[@id='company']"
        self.enteraddress = "//input[@id='address1']"
        self.entercity = "//input[@id='city']"
        self.clickenterstate = "//select[@id='id_state']"
        self.enterzip = "//input[@id='postcode']"
        self.entercountry = "//select[@id='id_country']"
        self.enterphone = "//input[@id='phone']"
        self.entermobilephone = "//input[@id='phone_mobile']"
        self.savebilling = "//span[contains(text(),'Save')]"
        self.continuecheckoutaddress= "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
        self.checkmarkclick = "//input[@id='cgv']"
        self.continuecheckoutcarier="//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]"
        self.paybybank = "//a[@class='bankwire']//span[contains(text(),'(order processing will be longer)')]"
        self.confirmall = "//span[contains(text(),'I confirm my order')]"

    def women(self):
        self.driver.find_element_by_xpath(self.woman).click()
    def click_on_item(self):
        self.driver.find_element_by_xpath(self.clickonitem).click()
    def add_item_to_card(self):
        self.driver.find_element_by_xpath(self.additemtocard).click()
    def proceed_to_check_out(self):
        self.driver.find_element_by_xpath(self.proceedtocheckout).click()
    def proceed_to_check_outt(self):
        self.driver.find_element_by_xpath(self.proceedtocheckoutt).click()
    def enteremail(self):
        self.driver.find_element_by_xpath(self.enteremail).send_keys("exzigen@hotmail.com")
    def enterpassword(self):
        self.driver.find_element_by_xpath(self.enterpassword).send_keys("adik99")
    def clicklogin(self):
        self.driver.find_element_by_xpath(self.login).click()
    def enter_firstname (self):
        self.driver.find_element_by_xpath(self.enterfirstname).send_keys("Eddie")
    def enter_lastname (self):
        self.driver.find_element_by_xpath(self.enterlastname).send_keys("Ali")
    def enter_companyname(self):
        self.driver.find_element_by_xpath(self.entercompanyname).send_keys("tf")
    def enter_address(self):
        self.driver.find_element_by_xpath(self.enteraddress).send_keys("65 Martin")
    def enter_city(self):
        self.driver.find_element_by_xpath(self.entercity).send_keys("NewCity")
    def click_enter_state(self):
        self.driver.find_element_by_xpath(self.clickenterstate).send_keys("Alamaba")
    def enter_zip(self):
        self.driver.find_element_by_xpath(self.enterzip).send_keys("45678")
    def enter_country(self):
        self.driver.find_element_by_xpath(self.entercountry).send_keys("United States")
    def enter_phone(self):
        self.driver.find_element_by_xpath(self.enterphone).send_keys("4169099898")
    def enter_mobile_phone(self):
        self.driver.find_element_by_xpath(self.entermobilephone).send_keys("4169099797")
    def save_billing(self):
        self.driver.find_element_by_xpath(self.savebilling).click()
    def continue_checkout_address(self):
        self.driver.find_element_by_xpath(self.continuecheckoutaddress).click()
    def checkmark(self):
            self.driver.find_element_by_xpath(self.checkmarkclick).click()
    def continue_checkout_carier(self):
        self.driver.find_element_by_xpath(self.continuecheckoutcarier).click()
    def payby(self):
        self.driver.find_element_by_xpath(self.paybybank).click()
    def confirm(self):
        self.driver.find_element_by_xpath(self.confirmall).click()




