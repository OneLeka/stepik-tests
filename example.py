from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import os
import time


def fill_form(browser):
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_elements_by_xpath('//div//button[text()="Submit"]')[0]
    button.click()


def fill_100(browser):
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("123")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


def registration(browser):
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('input[placeholder*="name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[placeholder*="last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[placeholder*="email"]')
    input3.send_keys("whoami@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    print(welcome_text)
    assert "Congratulations! You have successfully registered!" == welcome_text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def click_box(browser):
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(int(x))
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)
    box = browser.find_element_by_id('robotCheckbox')
    box.click()
    flag = browser.find_element_by_id('robotsRule')
    flag.click()
    button = browser.find_element_by_css_selector('button.btn[type="submit"]')
    button.click()


def get_attr(browser):
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(int(x))
    print(y)
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(y)
    box = browser.find_element_by_id('robotCheckbox')
    box.click()
    flag = browser.find_element_by_id('robotsRule')
    flag.click()
    button = browser.find_element_by_css_selector('button.btn[type="submit"]')
    button.click()


def options(browser):
    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = int(x_element.text)
    y = int(y_element.text)
    z = x + y
    print('{} + {} = {}'.format(x, y, z))
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(z))

    button = browser.find_element_by_css_selector('button.btn[type="submit"]')
    button.click()


def scroll(browser):
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))
    check_box = browser.find_element_by_id('robotCheckbox')
    check_box.click()
    # browser.execute_script("window.scrollBy(0, 100);")
    radio_button = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)

    radio_button.click()
    button = browser.find_element_by_tag_name('button')
    button.click()


def add_file(browser):
    fisrt = browser.find_element_by_name('firstname')
    fisrt.send_keys('First')
    second = browser.find_element_by_name('lastname')
    second.send_keys('Second')
    email = browser.find_element_by_name('email')
    email.send_keys('email@mail.ru')

    file_element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'empty.txt')  # добавляем к этому пути имя файла
    file_element.send_keys(file_path)

    button = browser.find_element_by_tag_name('button')
    button.click()


def alert(browser):
    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    # alert_text = alert.text
    alert.accept()

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))

    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    result = alert_text.split(' ')[-1]
    print(result)


    # confirm = browser.switch_to.alert
    # confirm.accept()
    # confirm.dismiss()

    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()


def redirect(browser):
    button = browser.find_element_by_tag_name('button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(y))


    button = browser.find_element_by_tag_name('button')
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    result = alert_text.split(' ')[-1]
    print(result)


def simple(browser):
    time.sleep(1)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text


def main(func, link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        func(browser)

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    # func, link = scroll, 'http://SunInJuly.github.io/execute_script.html'
    # func, link = add_file, 'http://suninjuly.github.io/file_input.html'
    # link = "http://suninjuly.github.io/find_link_text"
    # link = "http://suninjuly.github.io/find_xpath_form"
    # link = 'http://suninjuly.github.io/selects1.html'
    # link = 'http://suninjuly.github.io/math.html'
    # link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/huge_form.html"
    func, link = get_attr,'http://suninjuly.github.io/get_attribute.html'
    # link = 'http://suninjuly.github.io/selects1.html'

    # func, link = alert, 'http://suninjuly.github.io/alert_accept.html'
    #func, link = redirect, 'http://suninjuly.github.io/redirect_accept.html'

    #func, link = simple, 'http://suninjuly.github.io/wait1.html'

    main(func, link)

