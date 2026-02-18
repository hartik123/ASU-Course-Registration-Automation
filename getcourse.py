from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, date
import os
from dotenv import load_dotenv

load_dotenv()

web = webdriver.Chrome()
web.get("https://webapp4.asu.edu/myasu/")
web.maximize_window()
username = 'hmsuhagi'
password = '******'

time.sleep(2)
username_page = web.find_element(By.ID,'username')
username_page.send_keys(username)

password_page = web.find_element(By.XPATH, '//*[@id="password"]')
password_page.send_keys(password)

sign_in_button_page = web.find_element(By.CLASS_NAME, "btn-submit")
sign_in_button_page.click()

time.sleep(10)


duo_security_iframe = web.find_element(By.XPATH, "/html/body/div/div/main/div/form/div/iframe")
web.switch_to.frame(duo_security_iframe)

wait_for_send_duo_push_button = WebDriverWait(web, 5)
wait_for_send_duo_push_button.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button")))

send_duo_push_button = web.find_element(By.XPATH, "/html/body/div/div/div[1]/div/form/div[1]/fieldset/div[1]/button")
remember_me = web.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div/label/input')
remember_me.click()
time.sleep(2)
send_duo_push_button.click()

web.switch_to.default_content()

wait_for_search_button_job_portal = WebDriverWait(web, 10)
wait_for_search_button_job_portal.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

time.sleep(10)

web.execute_script('window.open()')
web.switch_to.window(web.window_handles[-1])
web.get("https://webapp4.asu.edu/myasu/")

time.sleep(10)

time.sleep(5)

web.execute_script('window.open()')
web.switch_to.window(web.window_handles[-1])
web.get('https://webapp4.asu.edu/myasu/?action=addclass&strm=2234')

time.sleep(5)

handle = web.window_handles
print("Handle: ", handle)
print("Current web: ", web.current_window_handle)

WebDriverWait(web, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SSR_DUMMY_RECV1$0_row_1"]')))
spring2024 = web.find_element(By.XPATH, '//*[@id="SSR_DUMMY_RECV1$0_row_1"]')
spring2024.click()

time.sleep(5)

working = 1
for i in range(100000):
    
    try:
        if working == 0:
            web.close()
            time.sleep(2)
            web.switch_to.window(web.window_handles[-1])
            web.execute_script('window.open()')
            web.switch_to.window(web.window_handles[-1])
            web.get('https://webapp4.asu.edu/myasu/?action=addclass&strm=2234')
            handle = web.window_handles
            print("Handle: ", handle)
            print("Current web: ", web.current_window_handle)
            time.sleep(5)

            WebDriverWait(web, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SSR_DUMMY_RECV1$0_row_1"]')))
            spring2024 = web.find_element(By.XPATH, '//*[@id="SSR_DUMMY_RECV1$0_row_1"]')
            spring2024.click()
            time.sleep(5)
            working = 1
    
        WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="win2divSCC_NAV_TAB_row$0"]')))
        shopping_cart = web.find_element(By.XPATH, '//*[@id="win2divSCC_NAV_TAB_row$0"]')
        shopping_cart.click()

        time.sleep(5)
        WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_ENROLL_FL"]')))
        enroll_button = web.find_element(By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_ENROLL_FL"]')
        enroll_button.click()

        time.sleep(5)

        enroll_confirmation = web.find_element(By.XPATH, '//*[@id="#ICYes"]')
        enroll_confirmation.click()

        now = datetime.now()

        today = date.today()
        current_time = now.strftime("%H:%M:%S")
        print("Iteration: ", i, " | Current date and time:", today, "|", current_time)

        time.sleep(5)
    
    except Exception as e:
        print(e)
        working = 0
        time.sleep(20)
    

time.sleep(200)








# web = webdriver.Chrome()
# web.get("https://www.youtube.com/")

# web.switch_to.new_window('tab')
# web.get("https://www.geeksforgeeks.org/shamirs-secret-sharing-algorithm-cryptography/")
# web.close()

# web.switch_to.window(web.window_handles[-1])
# web.switch_to.new_window('tab')
# web.get("https://www.youtube.com/")

# # web.close()
# # web.switch_to.window(web.window_handles[-1])
# web.close()
# web.switch_to.window(web.window_handles[-1])
# web.close()

# time.sleep(10)