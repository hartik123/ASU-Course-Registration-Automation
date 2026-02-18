from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, date
import smtplib
from email.mime.text import MIMEText
from selenium.webdriver.support.ui import Select
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_python(i):
    sender = "hartiksuhagiya10@gmail.com"
    receiver = "hmsuhagi@asu.edu"
    subject = "One course opened | "+str(i)
    message = "One course opened | "+str(i)

    password = os.environ.get('EMAIL_APP_PASSWORD') # Gmail App Password (not account password)
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        print("Successfully sent email")
        smtpObj.quit()
    except Exception as e:
        print(e)

web = webdriver.Chrome()
web.get("https://webapp4.asu.edu/myasu/")
web.maximize_window()
username = os.environ.get('ASU_USERNAME')
password = os.environ.get('ASU_PASSWORD')

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
found_open = 0
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
    
        if found_open == 0:
            WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="win2divSCC_NAV_TAB_row$0"]')))
            shopping_cart = web.find_element(By.XPATH, '//*[@id="win2divSCC_NAV_TAB_row$0"]')
        else:
            WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.ID, 'win9divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0')))
            shopping_cart = web.find_element(By.ID, 'win9divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0')

        shopping_cart.click()

        # time.sleep(5)
        # WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_ENROLL_FL"]')))
        # enroll_button = web.find_element(By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_ENROLL_FL"]')
        # enroll_button.click()

        # time.sleep(5)

        # enroll_confirmation = web.find_element(By.XPATH, '//*[@id="#ICYes"]')
        # enroll_confirmation.click()

        # now = datetime.now()

        # today = date.today()
        # current_time = now.strftime("%H:%M:%S")
        # print("Iteration: ", i, " | Current date and time:", today, "|", current_time)

        time.sleep(5)

        #TRACKING OPEN COURSES
        # tags_containing_open_word = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'ps_box-edit')))
        # number_of_ele = web.find_elements(By.CLASS_NAME, 'ps_box-value')
        # print(tags_containing_open_word[0])
        # print(tags_containing_open_word[5])
        for i in range(6):
            getting_status = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_AVAIL_FL$'+str(i)+'"]')))
            # getting_status = web.find_element(By.XPATH, '//*[@id="DERIVED_SSR_FL_SSR_AVAIL_FL$'+str(i)+'"]')
            print("i-", getting_status.text)
            if "closed" in getting_status.text.lower():
                # send_email_python(i)

                class_number_open = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "DERIVED_SSR_FL_SSR_CLASSNAME_LONG$"+str(i))))
                class_number_open = class_number_open.text
                class_number_open = class_number_open[:5]
                print("class open: ", str(class_number_open))

                # WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ps_box-group psc_layout psa_vtab psc_rowact')))
                # swap_class = web.find_elements(By.CLASS_NAME, 'ps_box-group psc_layout psa_vtab psc_rowact')
                # swap_class = swap_class[7]

                WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.ID, 'SCC_LO_FL_WRK_SCC_VIEW_BTN$7')))
                swap_class = web.find_element(By.ID, 'SCC_LO_FL_WRK_SCC_VIEW_BTN$7')

                swap_class.click()
                
                time.sleep(3)
                # select_class_from_your_schedule = new Select(WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="DERIVED_REGFRM1_DESCR50$4$"]')))

                select_class_remove_from_your_schedule = Select(web.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_DESCR50$4$"]'))
                # select_class_remove_from_your_schedule.select_by_visible_text("CSE 563: Software Requirements and Spec (26502)")

                time.sleep(5)
                hi = web.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_DESCR50$4$"]')
                hi = hi.find_elements_by_xpath(".//*")
                print("The option is: ", hi[0].text)
                
                course_with_me_list = []
                for i in range(3):
                    course_with_me_list.append(hi[i].text)
                
                if "CSE 563: Software Requirements and Spec (26502)" in course_with_me_list:
                    select_class_remove_from_your_schedule.select_by_visible_text("CSE 563: Software Requirements and Spec (26502)")
                elif "CSE 536: Advanced Operating Systems (29392)" in course_with_me_list:
                    select_class_remove_from_your_schedule.select_by_visible_text("CSE 536: Advanced Operating Systems (29392)")
                else:
                    break

                time.sleep(5)
                select_class_get_from_your_schedule = Select(web.find_element(By.XPATH, '//*[@id="DERIVED_REGFRM1_SSR_CLASSNAME_35"]'))
                select_class_get_from_your_schedule.select_by_value("27725")


                time.sleep(5)
                nextButton = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SSR_SWAP_FL_WRK_SSR_PB_SRCH"]')))
                nextButton.click()

                time.sleep(5)
                submitButton = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SSR_ENRL_FL_WRK_SUBMIT_PB"]')))
                submitButton.click()

                time.sleep(5)
                confirmYesButton = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="#ICYes"]')))
                confirmYesButton.click()

                time.sleep(5)
                WebDriverWait(web, 20).until(EC.element_to_be_clickable((By.ID, 'win9divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0')))
                shopping_cart = web.find_element(By.ID, 'win9divSCC_LO_FL_WRK_SCC_GROUP_BOX_1$0')
                shopping_cart.click()

            # DERIVED_REGFRM1_DESCR50$4$
                time.sleep(4)
                found_open = 1



    
    except Exception as e:
        print(e)
        working = 0
        found_open = 0
        time.sleep(5)
    

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