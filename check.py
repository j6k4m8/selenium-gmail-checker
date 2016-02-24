from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings

driver = webdriver.Chrome()
# driver.set_window_size(1120, 550)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

print("Loading login page...")
driver.get("https://accounts.google.com/ServiceLogin?service=mail#identifier")
usernametext = driver.find_element_by_name('Email')
usernametext.send_keys(settings.USERNAME)
driver.find_element_by_name('signIn').click()
passwordtext = driver.find_element_by_name('Passwd') \
                     .send_keys([settings.PASSWORD, Keys.RETURN])
print("Signed in. Going to accounts page...")
wait.until(EC.element_to_be_clickable((By.ID,':29')))
driver.get("https://mail.google.com/mail/u/0/#settings/accounts")
links = driver.find_elements_by_xpath("//*[contains(text(), 'Check mail now')]")
print("Clicking links...")
for l in links:
    try:
        l.click()
    except:
        pass
links = driver.find_elements_by_xpath("//*[contains(text(), 'Check mail now')]")
for l in links:
    try:
        l.click()
    except:
        pass
print("Done.")
driver.close()
