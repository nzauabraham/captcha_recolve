from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

profile = webdriver.FirefoxProfile()
# profile.add_extension(r'/app/buster_captcha_solver-2.0.1.xpi')
profile.add_extension(r'./buster_captcha_solver-2.0.1.xpi')

# set Firefox options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')

# driver = webdriver.Firefox(firefox_profile=profile, options=options)

driver = webdriver.Firefox()

# navigate to the page
driver.get("https://www.google.com/recaptcha/api2/demo")

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))

# click the checkbox
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
# switch back to main page
driver.switch_to.default_content()

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
    (By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']")))
# find the Search button and click it
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]"))).click()

WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "/html/body/div/div/div[8]/div[2]/div[1]/div[1]/div[4]//button"))).click()

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/form/fieldset/ul/li[6]/input"))).click()

# click the checkbox
submit_button = driver.find_element(By.ID, "recaptcha-demo-submit")
submit_button.click()

print("<=== FINISHED ====>")
# close the webdriver instance
driver.quit()
