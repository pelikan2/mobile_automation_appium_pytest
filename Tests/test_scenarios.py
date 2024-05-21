import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Utils.configuration import appium_driver
from Utils.support_functions import (first_steps_to_dashboard, check_element, change_region, find_flight_ticket,
                                     check_value)


@allure.feature("flight_ticket")
@allure.severity(allure.severity_level.BLOCKER)
def test_find_tickets(appium_driver):

    first_steps_to_dashboard(appium_driver)
    find_flight_ticket(appium_driver)
    flight_ticket = check_element(appium_driver, '//android.widget.TextView[@text="Vienna Intl Arpt → Punta Raisi Arpt"]')
    assert flight_ticket.is_displayed(), "Element is not displayed"


@allure.feature("settings")
@allure.severity(allure.severity_level.NORMAL)
def test_app_settings_change_region(appium_driver):
    first_steps_to_dashboard(appium_driver)
    profile = WebDriverWait(appium_driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/navigation_bar_item_small_label_view" and @text="Profile"]')))
    profile.click()
    preferences = WebDriverWait(appium_driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                                '//android.widget.TextView[@text="Application preferences"]')))
    preferences.click()
    change_region(appium_driver)
    back = WebDriverWait(appium_driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '//android.widget.Button')))
    back.click()
    find_flight_ticket(appium_driver)
    flight_detail = WebDriverWait(appium_driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '(//android.widget.ImageView[@resource-id="com.pelicantravel.pelipecky:id/arrowImageView"])[1]')))
    flight_detail.click()
    assert check_value(appium_driver) == 'Kč'
