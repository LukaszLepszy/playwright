import time

from POM.base_page import BasePage
from POM.login.login_locators import LoginLocators
import pytest
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page


class LoginPage(BasePage):

    def put_value_in_input(self, login, password):
        self.page.locator(LoginLocators.USERNAME_INPUT).is_enabled()
        self.page.locator(LoginLocators.USERNAME_INPUT).fill(login)
        self.page.locator(LoginLocators.PASSWORD_INPUT).is_enabled()
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)
        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    #  input[placeholder='Username']
    def get_tittle(self, locator):
        self.page.locator(locator).is_visible()
        value = self.page.locator(locator).first
        return value

