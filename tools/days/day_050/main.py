from days.day_050.files.helpers import *


def day_050():
    title("TINDER SWIPE BOT")
    load_dotenv()
    TINDER_EMAIL = os.getenv("TINDER_EMAIL")
    TINDER_PASSWORD = os.getenv("TINDER_PASSWORD")

    # chrome_path = "./tools/chromedriver.exe"
    capabilities = DesiredCapabilities().CHROME
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")

    prefs = {
        "profile.default_content_setting_values": {
            "notifications": 1,
            "geolocation": 1,
        },
        "profile.managed_default_content_settings": {"geolocation": 1},
    }

    chrome_options.add_experimental_option("prefs", prefs)
    capabilities.update(chrome_options.to_capabilities())
    # chrome_options.binary_location = (
    #     "D:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    # )
    driver = webdriver.Chrome(options=chrome_options)  # executable_path=chrome_path,
    url = "https://tinder.com/"
    driver.get(url)

    time.sleep(1)
    login_button = driver.find_element(By.XPATH, '//div[text()="Log in"]')
    login_button.click()
    time.sleep(2)
    # # FB
    # facebook_login_btn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, '//div[text()="Login with Facebook"]')
    #     )
    # )
    # facebook_login_btn = driver.find_element(
    #     By.XPATH, '//div[text()="Login with Facebook"]'
    # )
    # facebook_login_btn.click()

    # facebook_signin_window = driver.window_handles[1]
    # driver.switch_to.window(facebook_signin_window)
    # time.sleep(3)
    # email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
    # email_input.send_keys(TINDER_EMAIL)
    # time.sleep(1)
    # try:
    #     password_input = driver.find_element(By.XPATH, '//input[@name="pass"]')
    #     password_input.click()
    #     password_input.send_keys(TINDER_PASSWORD)
    #     time.sleep(1)
    #     password_input.send_keys(Keys.ENTER)
    #     time.sleep(2)
    #     base_window = driver.window_handles[0]
    #     driver.switch_to.window(base_window)
    # except Exception as e:
    #     print(e)

    # GOOGLE
    # google_login_btn = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "container"))
    # )
    google_iframe = driver.find_element(
        By.XPATH,
        '//iframe[@title="Sign in with Google Button"]',
        # By.XPATH, '//div[text()="Continue with Google"]'
    )

    # Switch to the iframe
    driver.switch_to.frame(google_iframe)

    # Now you can interact with elements inside the iframe
    google_login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="Continue with Google"]'))
    )
    google_login_btn.click()

    # Switch back to the default content if needed
    driver.switch_to.default_content()

    # google_login_btn = google_iframe.find_element(
    #     By.XPATH, '//span[text()="Continue with Google"]'
    # )
    # google_login_btn.click()

    # google_login_btn = driver.find_element(
    #     By.XPATH, "/html/body/div/div/div[2]/span[1]"
    # )

    google_signin_window = driver.window_handles[1]
    driver.switch_to.window(google_signin_window)
    time.sleep(3)
    email_input = driver.find_element(By.XPATH, '//input[@type="email"]')
    email_input.send_keys(TINDER_EMAIL)
    next_btn = driver.find_element(By.XPATH, '//span[text()="Next"]')
    next_btn.click()
    time.sleep(1)
    try:
        password_input = driver.find_element(By.XPATH, '//input[@type="pass"]')
        password_input.click()
        password_input.send_keys(TINDER_PASSWORD)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)
        base_window = driver.window_handles[0]
        driver.switch_to.window(base_window)
    except Exception as e:
        print(e)

    try:
        time.sleep(3)
        allow_loc = driver.find_element(By.XPATH, '//button[@data-testid="allow"]')
        allow_loc.click()
        time.sleep(1)
        allow_loc = driver.find_element(By.XPATH, '//button[@data-testid="allow"]')
        allow_loc.click()
    except Exception as e:
        print(e)

    try:
        spans = driver.find_elements(By.XPATH, '//span[@class="Pos(r) Z(1)"]')
        for span in spans:
            if (
                span.text == "I accept"
                or span.text == "I ACCEPT"
                or span.text == "I Accept"
            ):
                time.sleep(1)
                btn = span.find_element(By.XPATH, "..")
                btn.click()
                time.sleep(3)
                break
    except Exception as e2:
        print(e2)

    time.sleep(2)

    while True:
        try:
            time.sleep(2)
            body = driver.find_element(By.CSS_SELECTOR, "body")
            body.send_keys(Keys.RIGHT)
            time.sleep(1)
            try:
                modal = driver.find_element(
                    By.XPATH,
                    '//div[@class="Bdrs(8px) Ov(h) Ta(c) Bgc(#fff) M(10px) W(100%) Miw(300px) W(400px)--ml Mah(100%)--xs Ovy(s)--xs Ovs(touch)--xs Ovsby(n)--xs"]',
                )
                if modal:
                    driver.close()
                    nls(f"{bcolors.FAIL}No more likes. Quitting...{bcolors.ENDC}")
                    break
            except:
                pass
        except:
            nls(e)
            pass
