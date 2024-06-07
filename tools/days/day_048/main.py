# Copyright (c) 2024 Jarid Prince

from days.day_048.files.helpers import *


def init(driver: WebDriver):
    cookie = "https://orteil.dashnet.org/cookieclicker/"
    with open("./tools/days/day_048/files/saves.txt") as newsave:
        save = newsave.read()
    nls("Launching...")
    driver.get(cookie)
    got_it_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cc_btn_accept_all"))
    )
    got_it_button = driver.find_element(By.CLASS_NAME, "cc_btn_accept_all")
    if got_it_button:
        got_it_button.click()
    lang_select_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )
    lang_select_button = driver.find_element(By.ID, "langSelect-EN")
    if lang_select_button:
        lang_select_button.click()
    time.sleep(5)

    options = driver.find_element(By.ID, "prefsButton")
    options.click()
    importsave = driver.find_element(By.LINK_TEXT, "Import save")
    importsave.click()
    textarea = driver.find_element(By.ID, "textareaPrompt")
    pyperclip.copy(save)
    textarea.click()
    textarea.clear()  # Optional: Clear the existing text in the textarea
    textarea.send_keys(Keys.CONTROL, "v")
    # textarea.send_keys(save)
    loadbtn = driver.find_element(By.ID, "promptOption0")
    loadbtn.click()

    time.sleep(2)


def upgrade(driver: WebDriver, buildings: bool, upgrades: bool, products: bool):

    if buildings == True:
        unlocked_store_items = driver.find_elements(
            By.CSS_SELECTOR, "div.product.unlocked.enabled"
        )
        unlocked_store_items_reversed = unlocked_store_items[::-1]
        for item in unlocked_store_items_reversed:
            try:
                item.click()
            except Exception as e:
                # print(e)
                pass

    if upgrades == True:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "div.crate.upgrade.enabled")
        unlocked_upgrades_reversed = upgrades[::-1]
        for upg in unlocked_upgrades_reversed:
            try:
                # ignore revoking elder covenant
                if upg.get_attribute("data-id") != "85":
                    upg.click()
            except Exception as e:
                print(e)
                pass

    if products == True:
        product_upgrades = driver.find_elements(By.CSS_SELECTOR, "div.productButton")
        unlocked_product_upgrades_reversed = product_upgrades[::-1]
        for upg in unlocked_product_upgrades_reversed:
            try:
                upg.click()
                yes_button = driver.find_element(By.ID, "promptOption0")
                yes_button.click()
            except Exception as e:
                # print(e)
                pass


def close_popups(driver: WebDriver):
    close_btns = driver.find_elements(By.CSS_SELECTOR, "div.close")
    # print(close_btns)
    for btn in close_btns:
        try:
            # btn.hover()
            btn.click()
        except Exception as e:
            # print(e)
            pass


def click_specials(driver: WebDriver):
    def try_gold():
        try:
            golden = driver.find_element(By.CLASS_NAME, "shimmer")
            golden.click()
        except:
            try_big_one()

    def try_big_one():
        try:
            bigone = driver.find_element(By.ID, "bigCookie")
            bigone.click()
        except:
            try_gold()

    try_gold()


def savegame(driver):
    try:
        options = driver.find_element(By.ID, "prefsButton")
        options.click()
        time.sleep(1)
        saveg = driver.find_element(By.LINK_TEXT, "Save")
        saveg.click()
        time.sleep(1)
        exs = driver.find_element(By.LINK_TEXT, "Export save")
        exs.click()
        time.sleep(1)
        savedata = driver.find_element(By.ID, "textareaPrompt")
        savefile = savedata.text
        with open("./tools/days/day_048/files/saves.txt", "w+") as savetxt:
            savetxt.write(savefile)
        finish = driver.find_element(By.LINK_TEXT, "All done!")
        finish.click()
        nls("Game saved.")
    except Exception as e:
        print(f"SAVE EXCEPT:\n\n{e}\n\n")
        pass


def reset_timer(INCREMENT: float, start_time: float):
    runtime = time.time()
    elapsed_time_seconds = runtime - start_time
    total_hours = int(elapsed_time_seconds // 3600)
    elapsed_time_seconds -= total_hours * 3600

    total_minutes = int(elapsed_time_seconds // 60)
    elapsed_time_seconds -= total_minutes * 60

    total_seconds = int(elapsed_time_seconds)

    print(datetime.now().time())
    print(
        f"Running for {total_hours} hours, {total_minutes} minutes, and {total_seconds} seconds."
    )
    return time.time() + INCREMENT


def day_048():
    title("GAME PLAYING BOT")
    # ===================
    delay = 10
    INCREMENT = delay  # 60 * 25
    # chrome_driver = "./tools/chromedriver.exe"
    driver = webdriver.Chrome()  # executable_path=chrome_driver
    init(driver=driver)
    # ===================
    start_time = time.time()
    every_ten = time.time() + INCREMENT
    save_interval = time.time() + (INCREMENT * 6)

    #  ==================
    # upgrade(driver=driver)
    go = True

    while go == True:
        # constant click
        click_specials(driver=driver)

        if time.time() > every_ten:
            upgrade(driver=driver, upgrades=True, buildings=True, products=True)
            close_popups(driver=driver)
            every_ten = reset_timer(INCREMENT=INCREMENT, start_time=start_time)

        if time.time() > save_interval:
            savegame(driver=driver)
            close_popups(driver=driver)
            save_interval = reset_timer(
                INCREMENT=(INCREMENT * 6),
                start_time=start_time,
            )
