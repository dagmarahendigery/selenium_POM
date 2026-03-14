from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class Locators:
    CREATE_ACCOUNT_EMAIL = (By.id, "email_create")


class AuthenticationPage(BasePage):
    """
    Authentication Page
    """
    def enter_create_account_email(self, email):
        """
        Enter email for new user registration
        :param email:
        :return:
        """

        self.driver.find_element(*Locators.CREATE_ACCOUNT_EMAIL).send_keys(email)