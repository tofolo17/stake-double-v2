from selenium.webdriver.common.by import By


class AffiliatePageLocators:
    # ID
    LOGIN_FORM = (By.ID, 'email')
    PASSWORD_FORM = (By.ID, 'current-password')

    # CSS
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        '#root > div.modal.modal-ssm > div.modal-wrapper > div > div.modal-body > form > button.button.default.color-primary.medium'
    )
    LOGIN_FORM_BUTTON = (
        By.CSS_SELECTOR,
        '#root > div.modal.modal-ssm > div.modal-wrapper > div > div.modal-body > form > button.button.text.color-primary.medium'
    )


class GamePageLocators:
    # NAME
    EXTERNAL_IFRAME = (By.NAME, 'external-game')

    # CSS
    INTERNAL_IFRAME = (By.CSS_SELECTOR, 'div.games-container > iframe')
    BALANCE_VALUE = (By.CSS_SELECTOR, '[data-role="balance-label-value"]')

    CHIPS = (By.CSS_SELECTOR, '[data-role="chip-stack"]')

    
    COLUMN_2ND = (By.CSS_SELECTOR, '[data-bet-spot-id="2nd12"]')
    COLUMN_3RD = (By.CSS_SELECTOR, '[data-bet-spot-id="3rd12"]')