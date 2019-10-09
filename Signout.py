class Sign_out():

    def __init__(self, driver):
        self.driver = driver
        self.clicklogout="//a[@class='logout']"


    def logout(self):
        self.driver.find_element_by_xpath(self.clicklogout).click()
