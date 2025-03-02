import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




class Login:
    def __init__(self, password, driver):
        # super().__init__(driver, password)
        self.password = password
        self.driver = driver


    def open_browser(self):
        router_ip = f"http://ip_link/"
        self.driver.get(router_ip)
        logger.info("Open Browser")

    def login_ap(self):
        password_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "adminPass")))
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)
        logger.info("Login Successfully!!!")
        time.sleep(5)

    def wireless_mode(self):
        wireless = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//li[2]/ul/li[3]")))
        wireless.click()
        logger.info("clicked on wireless sucessfully")
        time.sleep(5)
