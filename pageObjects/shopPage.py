from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    list_of_items = (By.XPATH, "//a[text()='Add to cart']")
    view_cart = (By.XPATH, "(//a[@title='View cart'])[1]")

    def get_list_of_elements(self):  # this is getter, caller
        return  self.driver.find_elements(*ShopPage.list_of_items)


    def get_view_cart(self):
        return self.driver.find_element(*ShopPage.view_cart)