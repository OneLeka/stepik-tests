import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector('button.btn-add-to-basket')
