from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def calc_value(browser):
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(int(x))
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)


def wait(browser):

    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click()

    calc_value(browser)

    button = browser.find_element_by_id('solve')
    button.click()

    return alert_result(browser)


def alert_result(browser):
    alert = browser.switch_to.alert
    alert_text = alert.text
    result = alert_text.split(' ')[-1]
    return result


def main(func, link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        result = func(browser)
        print(result)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    func, link = wait, 'http://suninjuly.github.io/explicit_wait2.html'
    main(func, link)