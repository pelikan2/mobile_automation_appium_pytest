from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


DEFAULT_TIMEOUT = 30


def first_steps_to_dashboard(driver):
    confirm_button = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.Button[@resource-id="com.pelicantravel.pelipecky:id/button_confirm"]')))
    confirm_button.click()
    notifications = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
    notifications.click()
    for _ in range(4):
        continue_button = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                             '//android.widget.Button[@resource-id="com.pelicantravel.pelipecky:id/continueButton"]')))
        continue_button.click()


def check_element(driver, xpath):
    return WebDriverWait(driver, DEFAULT_TIMEOUT).until(ec.visibility_of_element_located((By.XPATH, xpath)))


def change_region(driver):

    WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH,
                                                                      '//android.widget.TextView[@text="#pelipecky.sk"]')))
    region_change = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH,
                                                                                             '//android.widget.ScrollView/android.view.View[1]')))
    region_change.click()
    region_change = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH,
                                                                      '//android.widget.TextView[@text="#pelipecky.cz"]')))
    region_change.click()
    region_change = WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH,
                                                                                            '//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')))
    region_change.click()


def find_flight_ticket(driver):
    flight_button = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                             '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/navigation_bar_item_small_label_view" and @text="Flights"]')))
    flight_button.click()
    permission = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                          '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')))
    permission.click()
    flight_from = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/labelTextView" and @text="Flight from"]')))
    flight_from.click()
    flight_from = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '//android.widget.EditText[@resource-id="com.pelicantravel.pelipecky:id/searchEditText"]')))
    flight_from.send_keys("Vienna")
    flight_from = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                           '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/titleTextView" and @text="Vienna Intl Arpt"]')))
    flight_from.click()
    done_button = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.ID,
                                                                                           'com.pelicantravel.pelipecky:id/doneButton')))
    done_button.click()
    flight_to = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/labelTextView" and @text="Flight to"]')))
    flight_to.click()
    flight_to = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.EditText[@resource-id="com.pelicantravel.pelipecky:id/searchEditText"]')))
    flight_to.send_keys("Palermo")
    flight_to = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/titleTextView"]')))
    flight_to.click()
    done_button = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.ID,
                                                                                           'com.pelicantravel.pelipecky:id/doneButton')))
    done_button.click()
    oneway = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                      '//android.widget.CompoundButton[@resource-id="com.pelicantravel.pelipecky:id/oneWay"]')))
    oneway.click()
    departure = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                         '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/titleTextView" and @text="Departure"]')))
    departure.click()
    calendar = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                        '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/calendarDayTextView" and @text="30"]')))
    calendar.click()
    find_flights = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                            '//android.widget.Button[@resource-id="com.pelicantravel.pelipecky:id/searchSubmit"]')))
    find_flights.click()


def check_value(driver):
    check_price = WebDriverWait(driver, 30).until(ec.visibility_of_element_located((By.XPATH,
                                                                                      '//android.widget.TextView[@resource-id="com.pelicantravel.pelipecky:id/priceTextView"]')))
    price = check_price.get_attribute('text')
    return price[-2:]