import time

from resources.utils import *
from pages.base_page import BasePage
from resources.locators import GamePageLocators
from selenium.webdriver.support import expected_conditions as EC


class GamePage(BasePage):
    URL = 'https://www.arbety.com/games/external/1bdd7868b894471e89bbe046183f932d'

    def __init__(self, browser):
        super().__init__(browser)
        self.locator = GamePageLocators

    def enter_game(self):
        # Entering the game by switching frames
        external_iframe = self.find(self.locator.EXTERNAL_IFRAME)
        self.frame(self.locator.EXTERNAL_IFRAME)

        internal_iframe = self.find(self.locator.INTERNAL_IFRAME)
        self.frame(self.locator.INTERNAL_IFRAME)

        print(f'Frames loaded:\n{external_iframe}\n{internal_iframe}')

        # Checking if balance is displayed
        self.find(self.locator.BALANCE_VALUE)

        print('Element loaded. Inside the game!')

    def bet_strategy(self):
        # Initial bet amount
        first_bet = 2

        # Get the balance
        balance = self.get_money(self.locator.BALANCE_VALUE)

        # Check if the balance is enough
        self.check_balance(balance, first_bet)
        print(f'Initial balance: R${balance}\n')

        # Get the chip_bet, column_2nd and column_3rd
        chip_bet, column_2nd, column_3rd = self.find_structural_elements(
            first_bet)

        # Perform the first bet
        self.perform_bet(chip_bet, column_2nd, column_3rd)

        # Get the initial total bet
        last_bet = self.get_money(self.locator.TOTAL_BET_VALUE)
        print(f'Initial bet amount: R${last_bet}\n')

        # Play loop
        while True:
            # Check for changes in the total bet label
            result = self.get_last_bet_change(last_bet)

            # Wait for the board elements to be clickable
            self.find(self.locator.REPEAT_BUTTON)

            # If the total bet is equal to zero, the bet was lost
            if result == 0:
                balance, current_bet = self.handle_loss(balance, last_bet)
            else:
                balance, current_bet = self.handle_win(
                    balance, last_bet, first_bet, chip_bet, column_2nd, column_3rd
                )

            # Update the last_bet
            last_bet = current_bet

            # Refresh the structural elements <AVOID ERRORS>
            chip_bet, column_2nd, column_3rd = self.find_structural_elements()

    def get_money(self, locator):
        # Get the balance amount and convert it to float
        balance = self.text(locator)
        cleaned_balance = remove_non_utf8_chars(balance)
        money_balance = convert_to_float(cleaned_balance)
        return money_balance

    def find_structural_elements(self, first_bet):
        # Get the chip_bet
        bets = [2, 5, 10, 20, 50, 250]
        self.find(self.locator.CHIPS)
        chips = self.finds(self.locator.CHIPS)
        chip_bet = chips[bets.index(first_bet)]

        # Find the 2nd and 3rd columns
        column_2nd = self.find(self.locator.COLUMN_2ND)
        column_3rd = self.find(self.locator.COLUMN_3RD)

        return chip_bet, column_2nd, column_3rd

    def check_balance(self, balance, amount):
        # Check if the balance is sufficient for the bet
        if balance < amount:
            print('Insufficient balance!')
            self.browser.quit()

    def perform_bet(self, chip_bet, column_2nd, column_3rd):
        # Perform the bet by clicking on the chip and columns

        # Counter
        counter = 0

        # Try to click the chip 5 times due to elements in it's way
        while counter < 5:
            try:
                self.click(chip_bet)
                break
            except Exception:
                counter += 1
                time.sleep(1)
                print('Chip not found. Retrying...')

        self.click(column_2nd)
        self.click(column_3rd)

    def get_last_bet_change(self, last_bet):
        # Check for changes in the total bet label
        while True:
            result = self.get_money(self.locator.TOTAL_BET_VALUE)
            if result != last_bet:
                return result

    def handle_loss(self, balance, last_bet):
        # Handle the loss scenario
        balance -= last_bet
        current_bet = last_bet * 2
        print('Loss!')
        print(f'New balance: R${balance}')
        print(f'New bet amount: R${current_bet}\n')
        self.check_balance(balance, current_bet)
        self.click(self.locator.REPEAT_BUTTON)
        self.click(self.locator.DOUBLE_BUTTON)

        return balance, current_bet

    def handle_win(self, balance, last_bet, first_bet, chip_bet, column_2nd, column_3rd):
        # Handle the win scenario
        balance += last_bet / 2
        current_bet = first_bet
        print('Win!')
        print(f'New balance: R${balance}')
        print(f'New bet amount: R${current_bet}\n')
        self.check_balance(balance, current_bet)
        self.perform_bet(chip_bet, column_2nd, column_3rd)

        return balance, current_bet
