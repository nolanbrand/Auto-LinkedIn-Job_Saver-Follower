from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

EMAIL = "Your LinkedIn email address"
PASSWORD = "Your LinkedIn Password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.linkedin.com/jobs/search/")

sign_in_1 = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_1.click()

username = driver.find_element(By.ID, value="username")
username.send_keys(EMAIL)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

sign_in_2 = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_2.click()

time.sleep(12)

job_input = driver.find_element(By.CSS_SELECTOR, value='div input')

# print(job_search_inputs)
job_input.send_keys("Python Developer")

search_button = driver.find_element(By.XPATH, value='//*[@id="global-nav-search"]/div/div[2]/button[1]')
search_button.click()

chat_button = driver.find_elements(By.CSS_SELECTOR, value='.msg-overlay-bubble-header button')
chat_button[3].click()
time.sleep(4)

jobs_list = driver.find_elements(By.XPATH, value='//*[@id="main"]/div/div[2]/div[1]/div/ul/li')
action = ActionChains(driver)

for job_index in range(0, len(jobs_list)):
    try:
        driver.execute_script("arguments[0].scrollIntoView();", jobs_list[job_index])
        jobs_list[job_index].click()
        time.sleep(1)
        save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button')
        driver.execute_script("arguments[0].scrollIntoView();", save_button)
        time.sleep(1)
        save_button.click()
        time.sleep(1)
        follow_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/section/section/div[1]/div[1]/button')
        driver.execute_script("arguments[0].scrollIntoView();", follow_button)
        time.sleep(1)
        try:
            follow_button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            pass
    except IndexError:
        pass
