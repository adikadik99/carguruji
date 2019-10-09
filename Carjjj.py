import HtmlTestRunner
import unittest
from Carguruji.Pages.SignIN import Sign_In
from Carguruji.Pages.addToCard import add_Card
from Carguruji.Driver.Driver import chromedriver
from Carguruji.Pages.Signout import Sign_out
# Reports table for reports has been created
# Screenshot table for screenshots has been created

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = chromedriver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


    def test_addingitems(self):
        driver = self.driver
        driver.get("http://carguruji.com/shop/")
        driver.implicitly_wait(5)
        sign = Sign_In(driver)
        signout = Sign_out(driver)
        addCard = add_Card(driver)

        #logging in, checking with assertequal if log in is successfull, screenshot is saved for confirmation
        sign.login()
        sign.enter_email()
        sign.enter_passw()
        sign.clicksignin()
        driver.implicitly_wait(5)
        self.driver.save_screenshot("/Users/adik/PycharmProjects/selenium/Carguruji/Sceenshots/image.png")
        x = self.driver.title
        print(x)
        self.assertEqual(x, "My account - CarGuruji Shop")
        driver.implicitly_wait(20)
        sign.my_adres_1()
        sign.delete_myaddress()
        driver.switch_to_alert().accept()



        # choosing item,entereing billing info ,checking with assertEqual if order was successfully placed
        addCard.women()
        addCard.click_on_item()
        addCard.add_item_to_card()
        addCard.proceed_to_check_out()
        addCard.proceed_to_check_outt()
        driver.implicitly_wait(6)
        addCard.enter_firstname()
        addCard.enter_lastname()
        addCard.enter_companyname()
        addCard.enter_address()
        addCard.enter_city()
        addCard.click_enter_state()
        addCard.enter_zip()
        addCard.enter_country()
        addCard.enter_phone()
        addCard.enter_mobile_phone()
        addCard.save_billing()
        addCard.continue_checkout_address()
        addCard.checkmark()
        addCard.continue_checkout_carier()
        addCard.payby()
        addCard.confirm()
        self.driver.save_screenshot("/Users/adik/PycharmProjects/selenium/Carguruji/Sceenshots/image2.png")
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Order confirmation - CarGuruji Shop")

        #signing out,saving screenshot,checking with assertEqual if logout was successfull
        signout.logout()
        self.driver.save_screenshot("/Users/adik/PycharmProjects/selenium/Carguruji/Sceenshots/image3.png")
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Login - CarGuruji Shop")




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=(HtmlTestRunner.HTMLTestRunner(output=Reports, verbosity=2)))
