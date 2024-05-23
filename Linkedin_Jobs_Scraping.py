import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import linkedin_username, linkedin_password

# Update these variables with your LinkedIn credentials
LINKEDIN_USERNAME = linkedin_username
LINKEDIN_PASSWORD = linkedin_password

# Path to ChromeDriver executable
CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'

def login_to_linkedin(driver):
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)
    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

    username_field.send_keys(LINKEDIN_USERNAME)
    password_field.send_keys(LINKEDIN_PASSWORD)
    sign_in_button.click()

    time.sleep(5)  # Wait for login to complete

def navigate_to_jobs_page(driver):
    driver.get('https://www.linkedin.com/jobs/')
    time.sleep(2)

def click_show_all_button(driver):
    try:
        show_all_button = driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'Show all')]")
        show_all_button[1].click()  # Click the second occurrence
        time.sleep(5)  # Wait for the page to load after clicking
    except Exception as e:
        print(f"Error clicking 'Show all' button: {e}")

def main():
    # Configure Selenium and ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Log in to LinkedIn
        login_to_linkedin(driver)

        # Navigate to the jobs page
        navigate_to_jobs_page(driver)

        # Click the "Show all" button
        click_show_all_button(driver)

        # Keep the browser open
        input("Press any key to close the browser...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
