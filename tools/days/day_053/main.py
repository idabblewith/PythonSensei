from days.day_053.files.helpers import *


def day_053():
    title("THREADED AUTOMATED REAL ESTATE")
    ZILLOW_CLONE_SITE = "https://appbrewery.github.io/Zillow-Clone/"

    def scrape_data():
        res = requests.get(ZILLOW_CLONE_SITE)
        zillow_data = res.text
        soup = BeautifulSoup(zillow_data, "html.parser")
        return soup

    def structure_data(html_soup: BeautifulSoup) -> List[Dict[str, str]]:
        data_structures = []
        property_list_element = html_soup.find(
            name="ul", class_="List-c11n-8-84-3-photo-cards"
        )
        properties = property_list_element.find_all(
            class_="StyledPropertyCardDataWrapper"
        )
        for property in properties:
            link_element = property.find("a")
            if link_element:
                link_href = link_element.get("href", "")
                address_element = link_element.find("address")
                address = (
                    address_element.get_text(strip=True) if address_element else "N/A"
                )

                price_element = property.find(class_="PropertyCardWrapper")
                price = (
                    price_element.get_text(strip=True)[:6].strip("+")
                    if price_element
                    else "N/A"
                )

                data = {
                    "address": address,
                    "price": price,
                    "link": link_href,
                }
                data_structures.append(data)

        return data_structures

    def fill_form(property_data, form_url):
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(form_url)
            time.sleep(2)
            address_input = driver.find_element(
                By.XPATH,
                value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )
            price_input = driver.find_element(
                By.XPATH,
                value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )
            link_input = driver.find_element(
                By.XPATH,
                value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )

            address_input.send_keys(property_data["address"])
            price_input.send_keys(property_data["price"])
            link_input.send_keys(property_data["link"])

            submit_element = driver.find_element(
                By.XPATH,
                value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span",
            )
            submit_element.click()
        finally:
            driver.quit()

    def enter_data(data_structures: List[Dict[str, str]]):
        load_dotenv()
        form_url = os.getenv("ZILLOW_GOOGLE_FORM")
        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            future_to_property = {
                executor.submit(fill_form, property_data, form_url): property_data
                for property_data in data_structures
            }
            for future in futures.as_completed(future_to_property):
                try:
                    future.result()  # This will raise any exceptions that occurred during form submission
                except Exception as e:
                    print(f"An error occurred: {e}")

    site_html = scrape_data()
    data_structures = structure_data(site_html)
    enter_data(data_structures)
