import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    browser_url = os.getenv('BROWSER_URL')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{browser_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    #attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()