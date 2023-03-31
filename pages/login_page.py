# python -m pytest -s -v
#pip list Посмотреть что установлено для python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from base.base_class import Base
class Login_page(Base):

    url = 'https://5element.by/'

    #Locators
    cooki = "//button[@class='js-cookie-popup-close btn btn--block']"
    vhod = "//span[@class='ic-h-user']"
    user_name = "//input[@name='login']"
    password =  "//input[@type='password']"
    login_button = "//span[text()='Войти']"
    modal_popap = "(//button[@type='button'])[36]"
    main_word = " (//span[text()='Василий'])[2]"

    #Getters
    def get_cooki_button(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.cooki)))
    def get_vhod_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.vhod)))
    def get_user_name(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_modal_popap(self):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, self.modal_popap))) 
    def get_main_word(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))
    
    #Actions
    def click_cooki_button(self):
        self.get_cooki_button().click()
        print("Click cooki_button")
    def click_vhod_button(self):
        self.get_vhod_button().click()
        print("Click vhod_button")    
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")
    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login_button")
    def click_modal_popap(self):
        self.get_modal_popap().click()
        print("Esc modal_popap")

    #Methods
    def authorization(self):
        self.browser.get(self.url)
        self.browser.maximize_window() 
        self.get_current_url()
        self.click_cooki_button()
        self.click_vhod_button()
        self.input_user_name("kaleev.fam@mail.ru")
        self.input_password("Lytghlytgh1")   
        self.click_login_button()
        self.click_modal_popap()
        self.assert_word(self.get_main_word(), "Василий")

      