from datetime import datetime
from datetime import timedelta
class Base():
    def __init__(self,browser):
        self.browser = browser

    """Method get current url"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")
        print("---------------")

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = (datetime.utcnow()+ timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot'+ now_date + '.png'
        #browser.save_screenshot("d:\\Python\\avtom_selen_smit\\screen\\" + name_screenshot)
        #browser.save_screenshot(".\\screen\\" + name_screenshot)
        self.browser.save_screenshot(f'./screen/screenshot{now_date}.png')
    
    """Method assert url"""
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value url")