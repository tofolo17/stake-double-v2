import time
import pages.game_page as GP
import pages.affiliate_page as AP

from selenium import webdriver
from dotenv import load_dotenv
from config import env_settings
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


load_dotenv(env_settings("DESENVOLVIMENTO"))


# Main function
def main():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()

    # Load the affiliate page
    affiliate_page = AP.AffiliatePage(driver)
    affiliate_page.load()

    # Open the login form
    affiliate_page.open_login_form()

    # Login to the main page
    affiliate_page.login()

    # Load the game page
    game_page = GP.GamePage(driver)
    game_page.load()

    # Enter game
    game_page.enter_game()

    # Bet strategy
    game_page.bet_strategy()

    # Sleeps for 5 seconds
    time.sleep(30)

    # Close the browser
    driver.quit()


if __name__ == '__main__':
    main()
