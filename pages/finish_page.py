# python -m pytest -s -v
#pip list Посмотреть что установлено для python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from utilites.logger import Logger
import time
class finish_page(Base):
   
    def product_cart(self):
        Logger.add_start_step(method='product_cart')
        time.sleep(2)
        self.get_current_url()
        self.assert_url("https://5element.by/cart/")
        self.get_screenshot()
        Logger.add_end_step(url=self.browser.current_url, method='product_cart')
        