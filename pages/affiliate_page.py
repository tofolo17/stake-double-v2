import os
import time

from pages.base_page import BasePage
from resources.locators import AffiliatePageLocators


class AffiliatePage(BasePage):
    URL = 'https://www.arbety.com/?invite=p&code=jefwane'

    def __init__(self, browser):
        super().__init__(browser)
        self.locator = AffiliatePageLocators

    def open_login_form(self):
        self.click(self.locator.LOGIN_FORM_BUTTON)

    def login(self):
        self.fill(self.locator.LOGIN_FORM, os.getenv('USER'))
        self.fill(self.locator.PASSWORD_FORM, os.getenv('PASSWORD'))
        self.click(self.locator.LOGIN_BUTTON)

        # Get the current URL
        current_url = self.browser.current_url

        # Set a counter
        counter = 0

        # Loop until the URL changes
        while current_url == self.browser.current_url:
            time.sleep(1)

            # Increment the counter
            counter += 1

            # If the counter is greater than 10, prints a failure message
            if counter > 10:
                print('Login failed')
                self.browser.quit()
