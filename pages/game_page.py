import os

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
        first_bet = int(os.getenv('MONEY'))

        # Get the balance
        balance = self.get_money(self.locator.BALANCE_VALUE)

        # Check if there's a bet in progress
        if self.get_money(self.locator.TOTAL_BET_VALUE) != 0:
            print('There is a bet in progress. Please wait for it to finish.')
            self.browser.quit()

        # Check if the balance is enough
        self.check_balance(balance, first_bet)
        print(f'Initial balance: R${balance}')

        # Get the chip_bet, column_2nd and column_3rd
        chip_bet, column_2nd, column_3rd = self.find_structural_elements(
            first_bet
        )

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

            # Update the balance after the result
            balance = self.get_money(self.locator.BALANCE_VALUE)

            # Print the result
            print(f'Due to last round, our balance was: R${balance}')

            # If the total bet is equal to zero, the bet was lost
            if result == 0:
                current_bet = self.handle_loss(balance, last_bet)
            else:
                current_bet = self.handle_win(
                    balance, first_bet, chip_bet, column_2nd, column_3rd
                )

            # Print our new trial
            print(
                f"To the next round, we'll bet R${current_bet}. That leaves us with R${balance - current_bet} in our balance. Good luck!\n"
            )

            # Update the last_bet
            last_bet = current_bet

            # Refresh the structural elements - <AVOID ERRORS>
            chip_bet, column_2nd, column_3rd = self.find_structural_elements(
                first_bet
            )

    def get_money(self, locator):
        # Get the balance amount and convert it to float
        money = self.text(locator)
        cleaned_money = remove_non_utf8_chars(money)
        float_money = convert_to_float(cleaned_money)
        return float_money

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
        self.force_click(chip_bet, 10)
        self.force_click(column_2nd, 10)
        self.force_click(column_3rd, 10)

    def get_last_bet_change(self, last_bet):
        # Check for changes in the total bet label
        while True:
            result = self.get_money(self.locator.TOTAL_BET_VALUE)
            if result != last_bet:
                return result

    def handle_loss(self, balance, last_bet):
        '''
        PROBLEMAS AO DUPLICAR A APOSTA! Se passa de rodada, ele perde o botão de duplicar.
        Encontrar verificador de aposta encerrada.
        '''
        # Handle the loss scenario
        current_bet = last_bet * 2
        print('Loss!')

        # Check if the balance is enough
        self.check_balance(balance, current_bet)
        print("Balance OK. We're good to go!")

        # Repeat and double the bet
        self.force_click(self.locator.REPEAT_BUTTON, 10)
        self.force_click(self.locator.DOUBLE_BUTTON, 10)

        return current_bet

    def handle_win(self, balance, first_bet, chip_bet, column_2nd, column_3rd):
        # Handle the win scenario
        current_bet = first_bet
        print('Win!')

        # Check if the balance is enough
        self.check_balance(balance, current_bet)
        print("Balance OK. We're good to go!")

        # Perform the bet
        self.perform_bet(chip_bet, column_2nd, column_3rd)

        return current_bet
