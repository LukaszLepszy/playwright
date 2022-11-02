import playwright
import pytest
from playwright.sync_api import Playwright

@pytest.fixture()
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(10000)

    yield page
    page.close()