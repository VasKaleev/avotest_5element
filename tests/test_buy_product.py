#python -m pytest -s -v  -p no:warnings .\tests\test_buy_product.py
# python -m pytest -s -v  -p no:warnings .\tests\test_buy_product.py::test_buy_product_1
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.finish_page import finish_page
import time
import warnings

#@pytest.mark.run(order=3)
def test_buy_product_1(set_up, set_group):
    options = Options()
    options.add_argument("--disable-notifications")
    #Запуск браузера Chrome
    def runChromeDriverManager():
        return webdriver.Chrome(ChromeDriverManager().install(),options=options)
        #return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser = runChromeDriverManager()  

    print("Start test 1")
    login = Login_page(browser)
    login.authorization()

    mp = Main_page(browser)
    mp.select_menu_main()
    f = finish_page(browser)
    f.product_cart()
    time.sleep(5)
    browser.quit()
    
    print("Finish test 1")
    time.sleep(3)
    browser.quit()

