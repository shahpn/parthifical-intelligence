from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.wait import WebDriverWait
from twilio.rest import Client
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobar")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument('log-level=2')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

class Lionpath:
    def __init__(self) -> None:
        self.public_psu_link = 'https://public.lionpath.psu.edu/psp/CSPRD/EMPLOYEE/SA/h/?tab=PE_PT_NVT_PUBLIC_HOME'


    def get_semester(self):
        option_text = 'Summer 2023'
        driver.get(self.public_psu_link)
        search = driver.find_element(By.LINK_TEXT, 'Class Search')
        search.click()
        time.sleep(5)
        # find an element after clicking the aboce link
        # dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
        # print(dropdown)
        
        element = driver.find_element(By.XPATH, '//*[@id="CLASS_SRCH_WRK2_STRM$35$"]')
        all_options = element.find_elements(By.TAG_NAME, "option")
        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            # option.click()
        
        driver.quit()
        
        return 'yes'
