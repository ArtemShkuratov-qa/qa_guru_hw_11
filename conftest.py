import pytest

from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach
from dotenv import load_dotenv
import os

DEFAULT_BROWSER_VERSION = "128.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_pass = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv('SELENOID_URL')

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()