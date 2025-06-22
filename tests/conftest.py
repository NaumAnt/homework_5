import pytest
from selene import browser

@pytest.fixture(scope="session")
def setup_browser():
    # Устанавливаем размер окна браузера
    browser.config.window_width = 1950
    browser.config.window_height = 1250
    yield browser
    browser.quit()

@pytest.fixture
def open_form_browser_chrome(setup_browser):
    setup_browser.open('https://demoqa.com/automation-practice-form')