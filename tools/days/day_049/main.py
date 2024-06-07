from days.day_049.files.helpers import *


def day_049():
    title("AUTOMATED JOB SAVER")
    load_dotenv()
    LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
    LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
    LINKEDIN_SEARCH_QUERY = os.getenv(
        "LINKEDIN_SEARCH_QUERY"
    )  # spaces between words are %20

    # chrome_driver = "./tools/chromedriver.exe"
    driver = webdriver.Chrome()  # executable_path=chrome_driver
    nls("Code altered to save, instead of apply.")
    nls("Launching...")
    nls("Press CTRL C to exit...")
    driver.get("https://www.linkedin.com")
    login_btn = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    login_btn.click()
    time.sleep(1)
    email_input = driver.find_element(By.ID, "username")
    email_input.click()
    email_input.send_keys(LINKEDIN_EMAIL)
    password_input = driver.find_element(By.ID, "password")
    password_input.click()
    password_input.send_keys(LINKEDIN_PASSWORD)
    sign_in_btn = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large")
    sign_in_btn.click()

    time.sleep(10)

    driver.get(
        f"https://www.linkedin.com/jobs/search/?currentJobId=3940975882&keywords={LINKEDIN_SEARCH_QUERY}&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true"
    )
    time.sleep(2)

    # left_column = driver.find_element(By.CLASS_NAME, "jobs-search__left-rail")
    # left_column = driver.find_element(By.CLASS_NAME, "jobs-search-results-list")
    left_column = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")

    left_column.click()
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(3)
    html.send_keys(Keys.HOME)

    all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    print(len(all_jobs))
    for job in all_jobs:
        job.click()
        time.sleep(2)
        try:
            save_job_btn = driver.find_element(
                By.CSS_SELECTOR, "button.jobs-save-button"
            )
            save_job_btn.click()
            time.sleep(2)
            close = driver.find_element(
                By.CSS_SELECTOR,
                ".artdeco-toast-item__dismiss.artdeco-button.ember-view",
            )
            close.click()
        except NoSuchElementException:
            nls("No application button, skipped.")
            continue

    while True:
        pass
