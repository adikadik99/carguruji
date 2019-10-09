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
class Sign_In():

    def __init__(self, driver):
        self.driver = driver
        self.click="//a[@class='login']"
        self.enteremail = "//input[@id='email']"
        self.enterpassword = "//input[@id='passwd']"
        self.click_signin = "//form[@id='login_form']//span[1]"
        self.myadres = "//span[contains(text(),'My addresses')]"
        self.deleteadres = "//span[contains(text(),'Delete')]"

    def login(self):
        self.driver.find_element_by_xpath(self.click).click()
    def enter_email(self):
        self.driver.find_element_by_xpath(self.enteremail).send_keys("exzigen@hotmail.com")
    def enter_passw(self):
        self.driver.find_element_by_xpath(self.enterpassword).clear()
        self.driver.find_element_by_xpath(self.enterpassword).send_keys("adik99")
    def clicksignin(self):
        self.driver.find_element_by_xpath(self.click_signin).click()
    def my_adres_1(self):
        self.driver.find_element_by_xpath(self.myadres).click()
    def delete_myaddress(self):
        self.driver.find_element_by_xpath(self.deleteadres).click()
