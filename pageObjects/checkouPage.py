from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    coupon_code = (By.ID, "coupon_code")
    apply_button = (By.CSS_SELECTOR, "button[name='apply_coupon']")
    coupon_text = (By.CSS_SELECTOR, ".woocommerce-message")
    checkout_button = (By.CLASS_NAME, "checkout-button")

    def get_coupon_code(self):
        return self.driver.find_element(*CheckOutPage.coupon_code)

    def get_apply_button(self):
        return self.driver.find_element(*CheckOutPage.apply_button)

    def get_coupon_text(self):
        return self.driver.find_element(*CheckOutPage.coupon_text)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.checkout_button)
