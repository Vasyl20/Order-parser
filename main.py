from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

# Переход на сторінку, яку потрібно перевірити
url = "https://freelancehunt.com/ua/projects/skill/mac-ta-objective/146.html?page=1"
driver.get(url)

# Знаходження елементу з класом "pagination"
pagination = driver.find_element_by_css_selector("div.pagination")

# Знаходження усіх елементів <li> безпосередньо всередині елементу "pagination"
li_elements = pagination.find_elements_by_css_selector("ul.no-padding > li")

# Рахування кількості елементів <li>
li_count = len(li_elements)

# Виведення кількості сторінок
print("Кількість сторінок:", li_count)

# Завершення роботи драйвера
driver.quit()