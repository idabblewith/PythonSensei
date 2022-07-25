from days.day_049.files.helpers import *


def day_049():
	title("AUTOMATED JOB SAVER")
	with open("./tools/secrets/linkedin_email.secret") as email:
		link_email = email.read()
	with open("./tools/secrets/linkedin_password.secret") as password:
		link_password = password.read()
	with open("./tools/secrets/linked_search.secret") as search:
		search_query = search.read()
	chrome_driver = "./tools/chromedriver.exe"
	driver = webdriver.Chrome(executable_path=chrome_driver)
	nls("Code altered to save, instead of apply.")
	nls("Launching...")
	nls("Press CTRL C to exit...")
	driver.get(search_query)
	login_btn = driver.find_element_by_class_name("nav__button-secondary")
	login_btn.click()
	time.sleep(1)
	email_input = driver.find_element_by_id("username")
	email_input.click()
	email_input.send_keys(link_email)
	password_input = driver.find_element_by_id("password")
	password_input.click()
	password_input.send_keys(link_password)
	sign_in_btn = driver.find_element_by_css_selector("button.btn__primary--large")
	sign_in_btn.click()

	time.sleep(3)

	left_column = driver.find_element_by_class_name("jobs-search__left-rail")
	left_column.click()
	html = driver.find_element_by_tag_name("html")
	html.send_keys(Keys.END)
	time.sleep(3)
	html.send_keys(Keys.HOME)

	all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
	print(len(all_jobs))
	for job in all_jobs:
		job.click()
		time.sleep(2)
		try:
			save_job_btn = driver.find_element_by_css_selector("button.jobs-save-button")
			save_job_btn.click()
			time.sleep(2)
			close = driver.find_element_by_css_selector(".artdeco-toast-item__dismiss.artdeco-button.ember-view")
			close.click()
		except NoSuchElementException:
			nls("No application button, skipped.")
			continue
	
	while True:
		pass

