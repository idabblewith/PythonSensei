# Copyright (c) 2024 Jarid Prince

from days.day_048.files.helpers import *


def day_048():
    title("GAME PLAYING BOT")
    chrome_driver = "./tools/chromedriver.exe"
    delay = 10
    driver = webdriver.Chrome(executable_path=chrome_driver)
    cookie = "https://orteil.dashnet.org/cookieclicker/"
    firstsave = "Mi4wMzF8fDE2MTk5MzQwOTIzNzI7MTYxOTkzNDA5MjM3MjsxNjE5OTU5MTc3ODU1O1JvYm90IE11ZmZpbjtpaGFueXwxMTExMTEwMTEwMDEwMDEwMDEwMTB8MjU4MTkzMTc2OS44Njk5OTE7MzkxNzM2ODM3NjAuODE1OTI2OzI5NTA4OzExOzg5NzMwMTEyNS42MTAzMzg2OzQ1OzA7MDswOzA7MDswOzA7MDswOzExOzA7MDswOzA7MDswOzswOzA7MDswOzA7MDswOy0xOy0xOy0xOy0xOy0xOzA7MDswOzA7NTA7MDswOzA7MDsxNjE5OTQzMTgxNzIxOzA7MDs7NDE7MDswOzQ3MTE3MTkuNDYxNjI1ODA2O3wxMDAsMTAwLDMxMDgxODEwNTUsMCwsMCwxMDA7MTAwLDEwMCw3OTg0ODI5ODgsMCwsMCwxMDA7NzAsNzAsMzgzMzU1MTUxLDAsLDAsNzA7NTAsNTAsNzgyMjQyOTM3LDAsLDAsNTA7NTAsNTAsMjMyNDk4MjA5OSwwLCwwLDUwOzQwLDQwLDc3OTQyODI4NzAsMCwsMCw0MDsyMSwyMSwxMTc0MTUwNzc3MSwwLCwwLDIxOzExLDExLDkyNzg4MjczNzIsMCwsMCwxMTsyLDIsMTUxMDkxNzM1OCwwLCwwLDI7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCwwLCwwLDA7fDExMTExMTExMTExMTAwMTExMTExMTExMTExMTExMTExMTExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMDExMTExMTExMTExMTExMTAxMDEwMDAxMTExMTAxMTAwMDAwMDAwMTEwMDAwMTAxMDExMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTExMTAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMTExMTAwMDAwMDAwMTExMDAwMDAwMDAwMTExMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTExMXwxMTExMTEwMDAwMDAwMDAwMTExMTExMDAwMDAwMDAxMTEwMTExMTAwMTExMTEwMTEwMTEwMTAwMDAwMDAwMDAwMDAwMTEwMDExMDExMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAxMDAwMDEwMDAwMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwfHw%3D%21END%21"
    with open("./tools/days/day_048/files/saves.txt") as newsave:
        save = newsave.read()
    nls("Launcing...")
    driver.get(cookie)
    bigone = driver.find_element_by_id("bigCookie")

    start_time = time.time()
    every_ten = time.time() + 60 * 25

    bigone.click()

    options = driver.find_element_by_id("prefsButton")
    options.click()
    importsave = driver.find_element_by_link_text("Import save")
    importsave.click()
    textarea = driver.find_element_by_id("textareaPrompt")
    textarea.click()
    textarea.send_keys(save)
    loadbtn = driver.find_element_by_id("promptOption0")
    loadbtn.click()
    saveg = driver.find_element_by_link_text("Save")
    exs = driver.find_element_by_link_text("Export save")

    def savegame():
        try:
            saveg.click()
            exs.click()
            savedata = driver.find_element_by_id("textareaPrompt")
            savefile = savedata.text
            with open("./tools/days/day_048/files/saves.txt", "w") as savetxt:
                savetxt.write(savefile)
            finish = driver.find_element_by_link_text("All done!")
            finish.click()
            nls("Game saved.")
        except:
            pass

    go = True
    unlocked_store_items = driver.find_elements_by_css_selector(
        "div[class='product unlocked enabled']"
    )
    upgrades = driver.find_elements_by_css_selector(
        "div[class='crate upgrade enabled']"
    )
    upgradesinv = upgrades[::-1]
    unlocked_store_itemsinv = unlocked_store_items[::-1]
    # try:
    #     for item in unlocked_store_itemsinv:
    #         item.click()
    # except:
    #     pass

    # try:
    #     for upg in upgradesinv:
    #         upg.click()
    # except:
    #     pass

    while go == True:
        try:
            golden = driver.find_element_by_class_name("shimmer")
            golden.click()
        except:
            pass

        try:
            bigone.click()
        except:
            golden.click()

        if time.time() > every_ten:
            saveg = driver.find_element_by_link_text("Save")
            exs = driver.find_element_by_link_text("Export save")

            savegame()
            unlocked_store_items = driver.find_elements_by_css_selector(
                "div[class='product unlocked enabled']"
            )
            upgrades = driver.find_elements_by_css_selector(
                "div[class='crate upgrade enabled']"
            )
            upgradesinv = upgrades[::-1]
            unlocked_store_itemsinv = unlocked_store_items[::-1]
            # try:
            #     for upg in upgradesinv:
            #         upg.click()
            # except:
            #     pass
            try:
                for item in unlocked_store_itemsinv:
                    item.click()
            except:
                pass

            runtime = time.time()
            print(datetime.now().time())
            print(f"running for {((runtime-start_time)/60)/60} hours.")
            every_ten = time.time() + 60 * 25
