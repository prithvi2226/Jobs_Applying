import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from config import linkedin_username, linkedin_password

# LinkedIn credentials
LINKEDIN_USERNAME = linkedin_username
LINKEDIN_PASSWORD = linkedin_password

# Path to ChromeDriver executable
CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'

def login_to_linkedin(driver):
    driver.get('https://www.linkedin.com/login')
    time.sleep(2)
    driver.find_element(By.ID, 'username').send_keys(LINKEDIN_USERNAME)
    driver.find_element(By.ID, 'password').send_keys(LINKEDIN_PASSWORD)
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
    time.sleep(5)

def navigate_to_jobs_page(driver):
    driver.get('https://www.linkedin.com/jobs/')
    time.sleep(2)

def click_show_all_button(driver):
    try:
        driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'Show all')]")[1].click()
        time.sleep(5)
    except Exception as e:
        print(f"Error clicking 'Show all' button: {e}")

def get_apply_links(driver):
    apply_links = []
    jobs = driver.find_elements(By.CLASS_NAME, 'job-card-container')

    for job in jobs:
        try:
            job.click()
            time.sleep(2)

            # Check for "Easy Apply" button
            button_text_elements = driver.find_elements(By.CSS_SELECTOR, '.jobs-apply-button--top-card .artdeco-button__text')
            for element in button_text_elements:
                if element.text.strip() == "Easy Apply":
                    break
            else:
                # If "Easy Apply" button not found, proceed to get the "Apply" link
                apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
                if "Apply" in apply_button.text:
                    apply_button.click()
                    time.sleep(2)

                    # Handle the new tab or window
                    original_window = driver.current_window_handle
                    for window_handle in driver.window_handles:
                        if window_handle != original_window:
                            driver.switch_to.window(window_handle)
                            break

                    # Get the current URL in the new tab/window
                    apply_links.append(driver.current_url)

                    # Close the new tab/window and switch back to the original
                    driver.close()
                    driver.switch_to.window(original_window)
                    time.sleep(2)
        except Exception as e:
            print(f"Error: {e}")
    return apply_links

def save_links_to_json(links, filename='apply_links.json'):
    with open(filename, 'w') as f:
        json.dump(links, f, indent=4)

def main():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=chrome_options)

    try:
        login_to_linkedin(driver)
        navigate_to_jobs_page(driver)
        click_show_all_button(driver)
        apply_links = get_apply_links(driver)
        save_links_to_json(apply_links)
        print(f"Apply links saved to apply_links.json")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
