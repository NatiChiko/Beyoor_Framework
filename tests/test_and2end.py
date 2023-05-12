import logging
from time import sleep
from selenium.webdriver.common.by import By
from BaseClass import BaseClass
from pageObjects.billlingPage import BillingPage
from pageObjects.checkouPage import CheckOutPage
from pageObjects.homePage import HomePage
from pageObjects.paymentPage import PaymentPage
from pageObjects.shopPage import ShopPage


class TestEndToEnd(BaseClass):
    def test_end2end(self):
        home_page = HomePage(self.driver)
        home_page.get_shop_button().click()
        shop_page = ShopPage(self.driver)
        shop_page.get_list_of_elements()

        for item in shop_page.get_list_of_elements():
            item.click()
            if item == shop_page.get_list_of_elements()[2]:
                break

        shop_page.get_view_cart().click()
        checkout_page = CheckOutPage(self.driver)
        checkout_page.get_coupon_code().send_keys("Tojtech QA1 2023 Automation 10%")
        checkout_page.get_apply_button().click()
        text = "Coupon code applied successfully."
        assert text == checkout_page.get_coupon_text().text
        self.driver.refresh()
        checkout_page.get_checkout_button().click()
        billing_info = BillingPage(self.driver)
        billing_info.get_first_name().send_keys("Arsen")
        billing_info.get_last_name().send_keys("Wenger")
        billing_info.get_country().click()
        billing_info.get_country_search().send_keys("Uni")
        countries = billing_info.get_countries_list()

        for country in countries:
            if country.text == "United Kingdom (UK)":
                country.click()
                break

        billing_info.get_address().send_keys("Via dell'Amore 14")
        billing_info.get_city().send_keys("Liverpool")
        billing_info.get_postcode().send_keys("PO16 7GZ")
        billing_info.get_shipping_address().click()
        billing_info.get_phone_number().send_keys("(718) 763-1540")
        billing_info.get_email().send_keys("abc@gmail.com")
        # action = ActionChains(driver)
        # action.move_to_element(driver.find_element(By.CSS_SELECTOR,"div[id='order_review']")).perform()
        payment_page = PaymentPage(self.driver)
        logger = BaseClass()
        sleep(5)
        for payment in payment_page.get_payment_method():
            print(payment.text)
            if payment.text == "Cash on delivery":
                payment.click()
                logger.get_logger().info(payment.text)
                break

