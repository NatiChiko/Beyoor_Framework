from selenium.webdriver.common.by import By


# self.driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]").click()
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop_button = (By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]")

    def get_shop_button(self):  # * means that you call it to treat it as a tupple
        return self.driver.find_element(*HomePage.shop_button)  # because it's class variable, we have to call class itself
