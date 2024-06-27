import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = input("Enter your email: \n")
password = input("Enter your password: \n")

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='username']"))
)

email_input.send_keys(email)

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))
)

password_input.send_keys(password)

submit_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='organic-div']/form/div[3]/button"))
)

submit_btn.click()

WebDriverWait(driver, 10).until(EC.title_contains("Feed"))

title = driver.title

print(title)

time.sleep(2)

network = driver.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[2]/a")

network.click()

WebDriverWait(driver, 10).until(EC.title_contains("My Network"))

title = driver.title

print(title)

downBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[4]/aside[1]/div[1]/header/div[3]/button[2]")))
downBtn.click()

seeAll = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section[1]/header/a")))
seeAll.click()

WebDriverWait(driver, 10).until(EC.title_contains("Invitation"))

time.sleep(5)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)

accept_buttons = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@aria-label, 'Accept')]"))
)

numberOfButtons = len(accept_buttons)

print("Number of accept buttons found:", numberOfButtons)

for button in accept_buttons:
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button)).click()
        time.sleep(1)
    except Exception as e:
        print(f"Error clicking button: {e}")

driver.quit()

# *[@id="ember1704"]/section/ul/li/div[1]/child::div[@class="invitation-card__action-container pl3"]/child::button[contains(@aria-label, "Accept")]