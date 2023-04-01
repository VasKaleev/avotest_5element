# python -m pytest -s -v -p no:warnings .\tests\test_buy_product.py
# pip list - Посмотреть что установлено для python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from base.base_class import Base
from win32api import GetSystemMetrics
from selenium.webdriver import ActionChains
import time
class Main_page(Base):

    #Locators
    menu_main = "//a[@href='/catalog/11-noutbuki-i-kompyutery']"
    menu_noutbuki = "//a[@href='/catalog/1383-noutbuki']"
    tovar_s_vitriny = "(//div[@class='inp-box__text filter-label'])[2]"
    checkbox_filter_tov_v_rassr = "//div[text()='Товары в рассрочку']"
    filter_uchebn = "//a[@href='https://5element.by/catalog/1383-noutbuki/diagonal-ekrana=11-6,13-3,13-4,13-5,13-9,14-0,14-1,15-6;installment=1']"
    button_sort = "//span[@class='ic-sort']"
    sort_reiting = "//div[text()='По рейтингу']"
    vid = "//button[@class='btn btn--index btn--square']"
    naz_prod_1 = "(//a[@class='c-text'])[1]"
    value_price_prod_1 = "(//div[@class='c-price'])[1]"
    cart = "(//button[@class='btn c-cart ec-add-to-cart'])[1]"
    cart_nazv_prod_1 = "(//a[@class='c-text'])[1]"
    cart_price_prod_1 = "//div[@class='m-price']"
    click_cart_pereyti = "//a[@href='/cart/']"
  
    #Getters
    def get_select_menu_main(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_main)))
    def get_select_menu_noutbuki(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.menu_noutbuki)))
    def get_select_tovar_s_vitriny(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.tovar_s_vitriny)))
    def get_checkbox_filter_tov_v_rassr(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_filter_tov_v_rassr)))
    def get_filter_uchebn(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.filter_uchebn)))
    def get_button_sort(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.button_sort)))
    def get_sort_reiting(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.sort_reiting)))
    def get_button_sort(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.button_sort)))
    def get_button_sort_po_reitingy(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.sort_reiting)))
    def get_vid(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.vid)))
    def get_naz_prod_1(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.naz_prod_1)))
    def get_value_price_prod_1(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.value_price_prod_1)))
    def get_cart(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_cart_nazv_prod_1(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart_nazv_prod_1)))
    def get_cart_price_prod_1(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.cart_price_prod_1)))
    def get_click_cart_pereyti(self):
        return WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable((By.XPATH, self.click_cart_pereyti)))
    
    #Actions
    def click_select_menu_main(self):
        self.get_select_menu_main().click()
        print("Click menu_main")
    def click_select_menu_noutbuki(self):
        self.get_select_menu_noutbuki().click()
        print("Click menu_noutbuki")
        time.sleep(3)
    def click_select_tovar_s_vitriny(self):
        self.get_select_tovar_s_vitriny().click()
        print("Нажали checkbox Товар c витрины")
        time.sleep(3)
    def click_chekbox_filter_tov_v_rassr(self):
        self.get_checkbox_filter_tov_v_rassr().click()
        print("Click chekbox filter tovar v rassrochku")
        time.sleep(2)
    def click_filter_uchebn(self):
        self.get_filter_uchebn().click()
        print("Click filter uchebn")
        time.sleep(3)      
    def click_button_sort(self):
        self.get_button_sort().click()
        print("Нажали кнопку сортировка")
        time.sleep(2)
    def click_sort_reiting(self):
        self.get_sort_reiting().click()
        print("Нажали кнопку сортировка по рейтингу")
        time.sleep(2)
    def click_vid(self):
        self.get_vid().click()
        print("Click vid") 
        print("Monitor Height =", GetSystemMetrics(1))
        SCROLL_PAUSE_TIME = 1
        self.browser.execute_script("window.scrollTo(0, window.scrollY + 500)")
        print("Click chekbox filter tovar v rassrochku down")
    def click_naz_prod_1(self):
        nazv_product_1 = self.get_naz_prod_1().text
        print("Название товара перед добавлением в корзину: ", nazv_product_1)
        time.sleep(2)
    def click_value_price_prod_1(self):
        value_price_product_1 = self.get_value_price_prod_1().text
        #value_price_prod_1 = value_price_product_1.replace(" ","")
        #value_price_prod_1 = float(value_price_prod_1)
        print("Цена товара перед добавлением в корзину: ", float(value_price_product_1.replace(" ","")))
        time.sleep(2)
    def click_cart(self):
        self.get_cart().click()
        print("Нажали кнопку добавить в корзину")
        print("---------------")
        time.sleep(2)

    #Проверка после добавления товара в козину
    #Проверяем название товара после добавления в корзину     
    def click_cart_nazv_prod_1(self):
        time.sleep(2)
        cart_product_1 = self.get_cart_nazv_prod_1().text
        print("Название товара в корзине: ", self.get_naz_prod_1().text)
        assert cart_product_1 == self.get_naz_prod_1().text
        print("INFO Название товара на сайте и в корзине совпадают")                    
        time.sleep(2)
    #Проверяем цену товара после добавления в корзину    
    def click_cart_price_prod_1(self):
        time.sleep(2)
        #Цена товара после добавления в корзину cart_price_prod1
        cart_price_prod1 = self.get_cart_price_prod_1().text
        sum_prod1 = float(cart_price_prod1.replace(" ",""))
        print("Цена товара в корзине: ", sum_prod1)
        #Цена товара до добавления в корзину 
        price_do = self.get_value_price_prod_1().text
        price_dof = float(price_do.replace(" ",""))
        print("Цена товара до добавления в корзину: ", price_dof)
        assert sum_prod1 == price_dof
        print("Цена на сайте и после добавления в корзину совпадает")                   
        time.sleep(2)
    def clickp_cart_pereyti(self):
        self.get_click_cart_pereyti().click()
        print("Нажали кнопку Перейти в корзину")
        time.sleep(2)

          
    #Methods
    def select_menu_main(self):
        self.get_current_url()
        self.click_select_menu_main()
        self.click_select_menu_noutbuki()
        self.click_select_tovar_s_vitriny()
        self.click_chekbox_filter_tov_v_rassr()
        self.click_filter_uchebn()
        self.click_button_sort()
        self.click_sort_reiting()
        self.click_vid()
        self.click_naz_prod_1()
        self.click_value_price_prod_1()
        self.click_cart()
        self.click_cart_nazv_prod_1()
        self.click_cart_price_prod_1()
        self.clickp_cart_pereyti()

    


    