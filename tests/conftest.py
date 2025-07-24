import pytest
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from selene import Browser
from selene.core.configuration import Config as SeleneConfig
from attachment import attach
from selene import Browser, Config



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from attachment import attach

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
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser = Browser(
        SeleneConfig(
            driver=driver,
            hold_driver_at_exit=True
        )
    )

    yield browser

    attach.add_screenshot(browser)
    #attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()