import time
from selenium.webdriver.common.by import By


#обратите внимание, чтобы в директориях на уровни выше не было файла conftest.py, если в иерархии окажется этот файл, то интерпретатор будет работать неверно
#если не запускается с командой из шаблона урока, то попробуйте использовать полный путь к файлу, пример:
#pytest --language=ru C:\Users\1\Desktop\36_10\test_items.py

def test_cart_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    addtocart = browser.find_elements(By.CSS_SELECTOR, ".add-to-basket > button.btn-primary")
    assert len(addtocart) > 0, 'button add to cart not found'