from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def setup(request):
    options = Options()
    options.add_argument("__start-maximized")
    options.add_argument("__ignore-certificate-errors")
    options.add_experimental_option("detach", True)
    service_obj = Service("C:\\Users\\nchik\\chromedriver_win32 (2)\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=options)
    driver.implicitly_wait(10)  # For certain elements which needs to be appear it will wait until a ten seconds.
    driver.get("http://shopping.beeyor.com")
    request.cls.driver = driver  #cls stands for class
    yield
    driver.quit()


