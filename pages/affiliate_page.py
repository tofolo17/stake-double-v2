from pages.base_page import BasePage
from resources.locators import AffiliatePageLocators


class AffiliatePage(BasePage):
    URL = 'https://arbety.com/?invite=p&code=jefwane'

    def __init__(self, browser):
        super().__init__(browser)
        self.locator = AffiliatePageLocators
