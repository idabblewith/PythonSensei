from days.day_051.files.helpers import *


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        self.chrome_options = Options()
        self.chrome_options.page_load_strategy = "eager"
        self.driver = webdriver.Chrome(
            options=self.chrome_options
        )  # executable_path=chrome_driver
        self.up = 0
        self.down = 0
        self.promised_up = promised_up
        self.promised_down = promised_down

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        print("Got site")
        time.sleep(1)
        print("Finding go btn")
        time.sleep(4)
        go_btn = self.driver.find_element(
            By.XPATH, "//a[@class='js-start-test test-mode-multi']"
        )
        print("checking...")
        # Click the "Go" button
        go_btn.click()
        time.sleep(50)

        download_element = self.driver.find_element(
            By.CLASS_NAME,
            "result-item-download",
        )
        download_result = download_element.find_element(
            By.CLASS_NAME,
            "result-data-value",
            # By.XPATH, ".//span[@class='result-data-value']"
        )

        # Get the text value of the span
        self.down = float(download_result.text)

        # result-data-value

        upload_element = self.driver.find_element(
            By.CLASS_NAME,
            "result-item-upload",
        )
        print(upload_element)
        upload_result = upload_element.find_element(
            By.CLASS_NAME,
            "result-data-value",
        )
        self.up = float(upload_result.text)

        print("Up: ", self.up)
        print("Down: ", self.down)

    def tweet_about_internet(self):
        load_dotenv()
        X_EMAIL = os.getenv("X_EMAIL")
        X_PASSWORD = os.getenv("X_PASSWORD")
        X_USERNAME = os.getenv("X_USERNAME")
        self.driver.get("https://x.com/i/flow/login")

        time.sleep(5)
        email = self.driver.find_element(By.NAME, "text")
        email.click()
        email.send_keys(X_EMAIL)
        next = self.driver.find_element(By.XPATH, "//span[text()='Next']")
        next.click()
        time.sleep(3)
        try:
            password = self.driver.find_element(By.NAME, "password")
        except Exception as e:
            print(e)
            email = self.driver.find_element(By.NAME, "text")
            email.click()
            email.send_keys(X_USERNAME)
            next = self.driver.find_element(By.XPATH, "//span[text()='Next']")
            next.click()
            time.sleep(3)
            password = self.driver.find_element(By.NAME, "password")

        password.click()
        password.send_keys(X_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promised_down}down/{self.promised_up}up?"
        tweet_area = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div',
        )
        tweet_area.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span',
        )
        tweet_button.click()
        time.sleep(5)

        self.driver.quit()


def day_051():
    title("TWITTER COMPLAINT BOT")

    bot = InternetSpeedTwitterBot(promised_up=20, promised_down=100)

    bot.get_internet_speed()
    # bot.up = 9
    # bot.down = 55

    data = [["Up", bot.promised_up, bot.up], ["Down", bot.promised_down, bot.down]]

    # Define the column headers
    headers = ["", "Promised", "Actual"]

    # Print the table
    print(tabulate.tabulate(data, headers, tablefmt="pretty"))

    if bot.down < bot.promised_down or bot.up < bot.promised_up:
        print("Speed not as advertised.\nBecoming Karen...")
        bot.tweet_about_internet()
    else:
        print("No speed issues.")
