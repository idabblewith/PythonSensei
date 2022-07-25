from days.day_050.files.helpers import *

def day_050():
	title("TINDER SWIPE BOT")
	with open("./tools/secrets/tinder_email.secret") as e:
		email = e.read()
	with open("./tools/secrets/tinder_password.secret") as p:
		password = p.read()

	chrome_path = "./tools/chromedriver.exe"
	capabilities = DesiredCapabilities().CHROME
	chrome_options = Options()
	chrome_options.add_argument("--incognito")
	chrome_options.add_argument("--disable-infobars")
	chrome_options.add_argument("start-maximized")
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument("--disable-popup-blocking")

	prefs = {
		'profile.default_content_setting_values':
		{
			'notifications': 1,
			'geolocation': 1
		},

		'profile.managed_default_content_settings':
		{
			'geolocation': 1
		},
	}

	chrome_options.add_experimental_option('prefs', prefs)
	capabilities.update(chrome_options.to_capabilities())
	chrome_options.binary_location = "D:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
	driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
	url = 'https://tinder.com/'
	driver.get(url)

	time.sleep(1)
	login_button = driver.find_element_by_link_text("LOG IN")
	login_button.click()
	time.sleep(0.5)
	facebook_login = driver.find_element(By.XPATH, '//span[text()="Log in with Facebook"]')
	facebook_login_btn = facebook_login.find_element_by_xpath('..')
	time.sleep(2)
	facebook_login_btn.click()

	facebook_signin_window = driver.window_handles[1]
	driver.switch_to.window(facebook_signin_window)
	time.sleep(3)
	email_input = driver.find_element_by_xpath('//input[@name="email"]')
	email_input.send_keys(email)
	time.sleep(0.5)
	try:
		password_input = driver.find_element_by_xpath('//input[@name="pass"]')
		password_input.click()
		password_input.send_keys(password)
		time.sleep(1)
		password_input.send_keys(Keys.ENTER)
		time.sleep(2)
		base_window = driver.window_handles[0]
		driver.switch_to.window(base_window)
	except Exception as e:
		print(e)

	try:
		time.sleep(3)
		allow_loc = driver.find_element_by_xpath('//button[@data-testid="allow"]')
		allow_loc.click()
		time.sleep(0.5)
		allow_loc = driver.find_element_by_xpath('//button[@data-testid="allow"]')
		allow_loc.click()
	except Exception as e:
		print(e)

	try:
		spans = driver.find_elements_by_xpath('//span[@class="Pos(r) Z(1)"]')
		for span in spans:
			if span.text == "I accept" or span.text == "I ACCEPT" or span.text == "I Accept":
				time.sleep(1)
				btn = span.find_element_by_xpath('..')
				btn.click()
				time.sleep(3)
				break
	except Exception as e2:
		print(e2)

	time.sleep(2)

	while True:
		try:
			time.sleep(2)
			body = driver.find_element_by_css_selector('body')
			body.send_keys(Keys.RIGHT)
			time.sleep(1)
			try:
				modal = driver.find_element_by_xpath('//div[@class="Bdrs(8px) Ov(h) Ta(c) Bgc(#fff) M(10px) W(100%) Miw(300px) W(400px)--ml Mah(100%)--xs Ovy(s)--xs Ovs(touch)--xs Ovsby(n)--xs"]')
				if modal:
					driver.close()
					nls(f"{bcolors.FAIL}No more likes. Quitting...{bcolors.ENDC}")
					break
			except:
				pass
		except:
			nls(e)
			pass
