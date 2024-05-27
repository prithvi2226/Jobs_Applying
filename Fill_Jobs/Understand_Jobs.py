from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import openai
import sys
import os
import textwrap

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import the config module
from config import API_key

CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'


def get_page_source(url):
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
        html_content = driver.page_source
    finally:
        driver.quit()
    
    return html_content

# Example usage
job_application_url = 'https://careers.spglobal.com/jobs/301340?lang=en-us&utm_source=linkedin'
html_content = get_page_source(job_application_url)


# OpenAI API key
openai.api_key = API_key

def analyze_form(html_content):
    # Split HTML content into smaller chunks
    wrapped_text = textwrap.wrap(html_content, width=2000)  # Adjust width as necessary
    responses = []

    for idx, chunk in enumerate(wrapped_text[:10]):
        print(f"Processing chunk {idx + 1}/{min(len(wrapped_text), 10)}...")
        prompt = f"Analyze the following HTML content and identify the form fields for a job application. Specify the field names and the type of data to enter:\n\n{chunk}"
        try:
            chat_completion = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ]
            )
            responses.append(chat_completion.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error processing chunk {idx + 1}: {e}")
            continue  # Skip to the next chunk in case of an error

    return "\n".join(responses)

# Example usage
form_analysis = analyze_form(html_content)
print(form_analysis)
