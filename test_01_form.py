from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_interaction():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 20)

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "first-name"))
    )
    name_field.send_keys("Иван")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "last-name"))
    )
    name_field.send_keys("Петров")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "address"))
    )
    name_field.send_keys("Ленина, 55-3")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "e-mail"))
    )
    name_field.send_keys("test@skypro.com")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "phone"))
    )
    name_field.send_keys("+7985899998787")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "city"))
    )
    name_field.send_keys("Москва")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "country"))
    )
    name_field.send_keys("Россия")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "job-position"))
    )
    name_field.send_keys("QA")

    name_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "company"))
    )
    name_field.send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    submit_button.click()

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    assert "danger" in zip_code_field.get_attribute("class")

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        element = wait.until(
            EC.presence_of_element_located((By.NAME, field_id))
        )
        classes = element.get_attribute("class") or ""
        assert "success" in classes, (
            f"Поле {field_id} не подсвечено зелёным. Классы: {classes}"
        )

    driver.quit()