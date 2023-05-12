from selenium.webdriver.common.by import By


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

    payment_method = (By.CSS_SELECTOR, ".wc_payment_method")

    def get_payment_method(self):
        return self.driver.find_elements(*PaymentPage.payment_method)


