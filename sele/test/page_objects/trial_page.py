from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_element import Cast
from .base_page import BasePage
from .locator import Locator

class WikiPage(BasePage):

    url = 'https://en.wikipedia.org/wiki/West_with_the_Night'

    @property
    def talkButton(self):
        locator = Locator(by=By.ID, value='ca-talk')
        return BaseElement(self.driver, locator)

class IMDbPage(BasePage):

    url = 'https://www.imdb.com/title/tt0097165/'

    @property
    def cast(self):
        locator = Locator(by=By.CLASS_NAME, value='cast_list')
        return Cast(self.driver, locator)

class AmazonPage(BasePage):
    url = 'https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&'

    @property
    def emailInput(self):
        locator = Locator(by=By.ID, value='ap_email')
        return BaseElement(self.driver,locator)
    
    @property
    def contiButton(self):
        locator = Locator(by=By.ID, value='continue')
        return BaseElement(self.driver,locator)
    
    @property
    def pwdInput(self):
        locator = Locator(by=By.ID, value='ap_password')
        return BaseElement(self.driver,locator)

    @property
    def signInButton(self):
        locator = Locator(by=By.ID, value='signInSubmit')
        return BaseElement(self.driver,locator)