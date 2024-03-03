import time
import pages

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Main function
def main():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()

    # Load the affiliate page
    affiliate_page = pages.AffiliatePage(driver)
    affiliate_page.load()

    # Sleeps for 5 seconds
    time.sleep(5)

    # Close the browser
    driver.quit()


if __name__ == '__main__':
    main()
