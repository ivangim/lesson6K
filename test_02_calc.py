from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50) 
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.maximize_window()

        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

 
        button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()
        
        button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()

        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        
        actual_result = driver.find_element(By.CLASS_NAME, "screen").text
        
        assert actual_result == "15", f"{actual_result}"
        
    except Exception as e:
        driver.save_screenshot("calc_error.png")
        raise
        
    finally:
        driver.save_screenshot("calc_result.png")
        driver.quit()