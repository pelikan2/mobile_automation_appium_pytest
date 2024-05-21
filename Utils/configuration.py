import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions


@pytest.fixture(scope='function')
def appium_driver():
    cap: Dict[str, Any] = {
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'Android',
        'appPackage': 'com.pelicantravel.pelipecky',
        'appActivity': 'com.pelican.common.ui.splash.SplashActivity',
        'language': 'en',
        'locale': 'US'
    }

    url = 'http://localhost:4724'

    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

    yield driver

    driver.quit()
    