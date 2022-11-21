import os
import time
from playwright.sync_api import Page, Playwright, sync_playwright, expect
import pytest
from POM.login.login_locators import LoginLocators as Locator
from POM.login.login_page import LoginPage
from credencials import *

# password = os.environ['password']

class TestLogin:

    @pytest.mark.parametrize("login, password", [(credencials["ligin_1"], credencials["password"]),
                                                (credencials["ligin_2"], credencials["password"])])
                                                # (credencials["ligin_3"], password)])
    def test_correct_loggining(self, set_up, login:str, password:str) -> None:
        log = LoginPage(set_up)
        log.put_value_in_input(login, password)
        assert log.get_tittle(Locator.PRODUCTS_TITTLE).inner_text() == "PRODUCTS"

    def test_incorrect_loggining_locekd_user(self, set_up) -> None:
        log = LoginPage(set_up)
        log.put_value_in_input(credencials["ligin_4"], credencials["password"])
        assert log.get_tittle(Locator.ERROR_MESSAGE).inner_text() == "Epic sadface: Sorry, this user has been locked " \
                                                                     "out."

    @pytest.mark.parametrize("login, password, message",
                         [("", "bad", "Epic sadface: Username is required"),
                         ("bad", "", "Epic sadface: Password is required"),
                         ("bad", "bad", "Epic sadface: Username and password do not match any user in this service")])
    def test_loggining_incorrect_credencials(self, set_up, login:str, password:str, message:str) -> None:
        log = LoginPage(set_up)
        log.put_value_in_input(login, password)
        assert log.get_tittle(Locator.ERROR_MESSAGE).inner_text() == message

