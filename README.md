# Jobs_Applying
## LinkedIn Job Application Scraper

This project uses Selenium to automate the process of logging into LinkedIn, navigating to the Jobs page, and extracting application links for job postings. The script logs into LinkedIn, navigates to the Jobs page, searches for software engineering positions, and retrieves the application links for each job.

### Features

- Automated login to LinkedIn
- Navigate to the LinkedIn Jobs page
- Click on "Show all" buttons to reveal more job postings
- Extract and print application links, excluding "Easy Apply" jobs
- Analyze job application forms using OpenAI GPT to identify form fields

### Prerequisites

- Python 3.6+
- Google Chrome
- ChromeDriver

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/linkedin-job-scraper.git
    cd linkedin-job-scraper
    ```

2. Install the required Python packages:
    ```bash
    pip install selenium openai
    ```

3. Download and install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your version of Chrome. Ensure the ChromeDriver executable is in your PATH or specify its location in the script.

### Configuration

Create a `config.py` file in the project directory with your LinkedIn credentials and OpenAI API key:
```python
linkedin_username = 'your_email'
linkedin_password = 'your_password'
API_key = 'your_openai_api_key'
```

### Explanation of Updates

- **Features**: Added features to exclude "Easy Apply" jobs and analyze job application forms using OpenAI GPT.
- **Installation**: Added the installation of the `openai` package.
- **Configuration**: Instructions for creating a `config.py` file for sensitive credentials.
- **Usage**: Updated the usage section to reflect the new script name and functionalities.
- **Code Overview**: Detailed the functions added or updated, including the OpenAI GPT integration.
- **Example Output**: Provided a sample output format.

### Usage

Run the script:

```bash
python3 linkedin_job_scraper.py
```
The script will log into LinkedIn, navigate to the Jobs page, and print the application links for software engineering positions.

##### Code Overview
- login_to_linkedin(driver): Logs into LinkedIn using the provided credentials.
- navigate_to_jobs_page(driver): Navigates to the LinkedIn Jobs page.
- get_apply_link(driver): Extracts and prints application links for job postings.

### Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or find bugs.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.


This README.md provides an overview of the project, including installation and usage instructions. Be sure to replace the placeholders with your actual information, such as the repository URL and LinkedIn credentials.
