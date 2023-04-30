import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobar")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
options.add_argument('log-level=2')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


class Bulletin:
    def __init__(self) -> None:
        pass

    def _get_classes(self, input):
        matches = re.findall(r'(CMPSC|IST)\s?(\d{3})(w?)', input, re.IGNORECASE)

        if matches:
            course_names = [match[0].upper() + ' ' + match[1] + match[2] for match in matches]
            course_links = 'https://bulletins.psu.edu/search/?search=' + course_names[0].replace(' ', '+') + '&psusearchname=%2Fsearch%2F&caturl=%2Fundergraduate'
              
            for course_name in course_names:
                course = course_name.replace(' ', '')

            driver.get(course_links)

            element = driver.find_element(By.XPATH, f"""//*[@id='cb-{course}']/div[2]/p""")

            class_name = driver.find_element(By.XPATH, f"""//*[@id="fssearchresults"]/div[2]/h2""")
            
            
            # print(element.text)

            course_links += f'\n\n{element.text}'

            # driver.quit()

            return class_name.text, course_links
        else:
            return("No course names found.")

    def _search_history(self, input):
        link = 'https://www.google.com/search?q=' + input.replace(' ', '+') + '+psu'
        return link

    def _search_location(self):
        link = 'Check out the campus map: https://www.abington.psu.edu/map'
        return link

    def _search_professor(self, input):
        match = re.search(r'(?i)Professor\s(\w+)', input)

        if match:
                professor_name = match.group(1)
                link = 'https://www.abington.psu.edu/directory/results?keys=' + professor_name  +'&type=All'
                # return(link)

                driver.get(link)

                name = driver.find_element(By.XPATH, f"""//*[@id="main-layout"]/div/section/div/div/div/div[2]/div/table/tbody/tr/td[1]""")
                email = driver.find_element(By.XPATH, f"""//*[@id="main-layout"]/div/section/div/div/div/div[2]/div/table/tbody/tr/td[2]""")
                roles = driver.find_elements(By.XPATH, f"//div[contains(@class, 'paragraph paragraph--type--person-role paragraph--view-mode--default')]")
                office = driver.find_element(By.XPATH, f"""//*[@id="main-layout"]/div/section/div/div/div/div[2]/div/table/tbody/tr/td[4]""")
            
                role = ""

                if len(roles) == 1:
                    role = roles[0].text
                elif len(roles) > 1:
                    for inner_div in roles:
                        role += inner_div.text + ' | '

                    role = role[:-3]
                
                     
                a_tag = driver.find_element(By.XPATH, f"""//*[@id="main-layout"]/div/section/div/div/div/div[2]/div/table/tbody/tr/td[1]/a""")
                link = a_tag.get_attribute('href')

                name = name.text
                email = email.text
                office = office.text

                
                if name == "":
                    name = 'None'
                if email == "":
                    email = 'None'
                if role == "":
                    role = 'None'
                if office == "":
                    office = 'None'

                # driver.quit()

                return f"Below is the following information for {name}:\n\tEmail: {email}\n\tRole(s): {role}\n\tOffice Location: {office}\n\nOr use the following link to get more information: {link}"

        else:
                return(f"Professor not found.")