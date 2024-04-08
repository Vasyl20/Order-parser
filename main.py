from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()  # Припустимо, що ви використовуєте Chrome, можна змінити на інший драйвер
index_num =int(1)
# Переход на сторінку, яку потрібно перевірити
url = "https://freelancehunt.com/ua/projects/skill/parsing-danih/169.html"
driver.get(url)

# Очікування наявності елементів на сторінці
try:
    # Очікування наявності блоку з класом "pagination"
    pagination = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.pagination > ul.no-padding")))
    
    # Знаходження усіх елементів <li> у блоку "pagination"
    a_elements = pagination.find_elements(By.TAG_NAME, "a")
    
    # Рахування кількості елементів <li>
    li_count = len(a_elements)
    
    # Виведення кількості сторінок
    print("Кількість сторінок:", li_count)
        
finally:
    # Завершення роботи драйвера
    driver.quit()

driver2 = webdriver.Chrome()

page=1

while True:


    driver2.get(f"https://freelancehunt.com/ua/projects/skill/parsing-danih/169.html?page={str(page)}")

    WebDriverWait(driver2, 10).until(EC.presence_of_element_located(("xpath", "//tbody//tr")))

    rows = driver2.find_elements("xpath", "//tbody//tr[.//h2 and .//a]")

    if int(page) >= int(li_count-1):
        break
    else:

       for index in range(li_count):
            h2_text = rows[index].find_element("xpath", ".//h2").text
            print(f"{index_num}: {h2_text}")
            index_num += 1     
            
    page += 1
    
driver.quit()