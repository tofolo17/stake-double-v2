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
        f1 = self.find(self.locator.EXTERNAL_IFRAME)
        self.frame(self.locator.EXTERNAL_IFRAME)

        f2 = self.find(self.locator.INTERNAL_IFRAME)
        self.frame(self.locator.INTERNAL_IFRAME)

        print(f'Iframe carregado:\n{f1}\n{f2}')

        self.find(self.locator.BALANCE_VALUE)

        print('Elemento carregado. Estamos dentro do jogo!')

    def bet_strategy(self):
        initial_bet = 1

        # Get the balance
        balance = self.get_money(self.locator.BALANCE_VALUE)

        # Check if the balance is enough
        if balance < initial_bet * 2:
            print('Saldo insuficiente!')
            self.browser.quit()
        print(f'Saldo: R${balance}')

        # Get the chip_bet
        bets = [1, 2.5, 5, 10, 25, 125]
        self.find(self.locator.CHIPS)  # Guarantees that the chips are loaded
        chips = self.finds(self.locator.CHIPS)
        chip_bet = chips[bets.index(initial_bet)]

        # Find the 2nd and 3rd columns
        column_2nd = self.find(self.locator.COLUMN_2ND)
        column_3rd = self.find(self.locator.COLUMN_3RD)

        # Bet on the 2nd and 3rd columns
        self.click(chip_bet)
        self.click(column_2nd)
        self.click(column_3rd)

        # Get the total bet
        initial_total_bet = self.get_money(self.locator.TOTAL_BET_VALUE)
        if initial_total_bet != initial_bet * 2:
            print('Algo deu errado!')
            return
        print(f'Aposta inicial: R${initial_total_bet}. Vamos jogar!')

        # Play loop
        while True:
            # Check for changes in the total bet label
            total_bet = self.get_total_bet_change(initial_total_bet)

    def get_money(self, locator):
        balance = self.text(locator)
        cleaned_balance = remove_non_utf8_chars(balance)
        money_balance = convert_to_float(cleaned_balance)
        return money_balance

    def get_total_bet_change(self, total_bet):
        while True:
            new_total_bet = self.get_money(self.locator.TOTAL_BET_VALUE)
            if new_total_bet != total_bet:
                return new_total_bet
