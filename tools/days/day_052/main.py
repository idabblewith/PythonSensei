from days.day_052.files.helpers import *


class InstaFollower:

    def __init__(self, username: str, password: str, similar_account: str):
        # Optional - Keep browser open (helps diagnose issues during a crash)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.username = username
        self.password = password
        self.similar_account = similar_account

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(1)
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(self.username)
        time.sleep(0.5)
        passw = self.driver.find_element(By.NAME, "password")
        passw.send_keys(self.password)
        time.sleep(0.5)
        passw.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_following(self):
        self.driver.get(f"https://www.instagram.com/{self.similar_account}/following/")
        time.sleep(2.5)
        try:
            # Wait until the followers button is clickable
            followers_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[href$='/epicgames/following/']")
                )
            )
            followers_button.click()
            print("Clicked on the followers button.")
        except Exception as e:
            print("An error occurred:", e)
        time.sleep(5.5)

    def follow(self):
        try:
            # Wait for the modal to appear
            modal_xpath = "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]"
            modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, modal_xpath))
            )

            last_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", modal
            )
            while True:
                # Scroll down the modal
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight", modal
                )
                time.sleep(2)  # Allow time for new elements to load

                new_height = self.driver.execute_script(
                    "return arguments[0].scrollHeight", modal
                )
                if new_height == last_height:
                    break
                last_height = new_height

            follow_buttons_css = "button._acan._acap._acas._aj1-._ap30"
            buttons = self.driver.find_elements(By.CSS_SELECTOR, follow_buttons_css)

            print(f"Found {len(buttons)} buttons.")
        except Exception as e:
            print("An error occurred:", e)

        for button in buttons:
            if button.text == "Follow":
                try:
                    ActionChains(self.driver).move_to_element(button).perform()
                    button.click()
                    time.sleep(1.1)
                except ElementClickInterceptedException as e:
                    print(e)
                except Exception as e:
                    print(e)
            else:
                print("btn text: ", button.text)
        print("\nDONE!\n")


def day_052():
    title("INSTAGRAM BOT")
    load_dotenv()
    SIMILAR_INSTAGRAM_ACCOUNT = os.getenv("SIMILAR_INSTAGRAM_ACCOUNT")
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    bot = InstaFollower(
        username=INSTAGRAM_USERNAME,
        password=INSTAGRAM_PASSWORD,
        similar_account=SIMILAR_INSTAGRAM_ACCOUNT,
    )
    bot.login()
    bot.find_following()
    bot.follow()
