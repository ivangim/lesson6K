from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



def test_sauce_demo_store():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 5)
    
    try:
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.save_screenshot("store_0.png")

        username_input = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()
        driver.save_screenshot("store_1.png")

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
        
        wait = WebDriverWait(driver, 10)
        
        backpack_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack_button.click()

        driver.save_screenshot("store_2.png")

        wait.until(EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-backpack"), "Remove"))

        tshirt_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        tshirt_button.click()
        driver.save_screenshot("store_3.png")

        wait.until(EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-bolt-t-shirt"), "Remove"))

        onesie_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        onesie_button.click()
  

        wait.until(EC.text_to_be_present_in_element((By.ID, "remove-sauce-labs-onesie"), "Remove"))

        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_icon.click()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
        driver.save_screenshot("store_4.png")

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        driver.save_screenshot("store_5.png")

        driver.save_screenshot("store_6.png")

        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        
        first_name = driver.find_element(By.ID, "first-name")
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")
        
        first_name.send_keys("Иван")
        last_name.send_keys("Петров")
        postal_code.send_keys("123456")
        driver.save_screenshot("store_7.png")
        
        continue_button.click()

        total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        
        total_text = total_element.text
        total_value = total_text.replace("Total: $", "")

        expected_total = "58.29"
        assert total_value == expected_total

        driver.save_screenshot("store_8.png")
        
    except Exception as e:
        driver.save_screenshot("store_error.png")
        raise
        
    finally:

        driver.quit()