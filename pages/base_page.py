from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    URL = ''

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 60)

    def find(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def text(self, locator):
        self.wait.until(self.non_null_value(locator))
        return self.find(locator).text

    def load(self):
        self.browser.get(self.URL)
        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'body')))

    def fill(self, locator, value):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(value)

    def frame(self, locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def script(self, script):
        return self.browser.execute_script(script)

    def non_null_value(self, locator):
        def _wait_for_non_null_value(driver):
            try:
                element = driver.find_element(*locator)
                text = element.text.strip()
                return text != ''
            except Exception:
                return False

        return _wait_for_non_null_value
