from selenium.webdriver.common.by import By


class BillingPage:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@id='billing_first_name']")
    last_name = (By.XPATH, "//input[@id='billing_last_name']")
    country = (By.CSS_SELECTOR, "#select2-billing_country-container")
    country_search = (By.CSS_SELECTOR, "input[role='combobox']")
    countries_list = (By.CSS_SELECTOR, ".select2-results__option")
    address = (By.CSS_SELECTOR, "#billing_address_1")
    city = (By.CSS_SELECTOR, "#billing_city")
    postcode = (By.CSS_SELECTOR, "#billing_postcode")
    shipping_address = (By.CSS_SELECTOR, "#ship-to-different-address-checkbox")
    phone_number = (By.CSS_SELECTOR, "#billing_phone")
    email = (By.CSS_SELECTOR, "#billing_email")


    def get_first_name(self):
        return self.driver.find_element(*BillingPage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*BillingPage.last_name)

    def get_country(self):
        return self.driver.find_element(*BillingPage.country)

    def get_country_search(self):
        return self.driver.find_element(*BillingPage.country_search)

    def get_countries_list(self):
        return self.driver.find_elements(*BillingPage.countries_list)

    def get_address(self):
        return self.driver.find_element(*BillingPage.address)

    def get_city(self):
        return self.driver.find_element(*BillingPage.city)

    def get_postcode(self):
        return self.driver.find_element(*BillingPage.postcode)

    def get_shipping_address(self):
        return self.driver.find_element(*BillingPage.shipping_address)

    def get_phone_number(self):
        return self.driver.find_element(*BillingPage.phone_number)

    def get_email(self):
        return self.driver.find_element(*BillingPage.email)






