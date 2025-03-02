import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class APAutomation:

    def __init__(self, password, driver):
        self.password = password
        self.driver = driver


    def edit_ssid_pass_2g(self):
        time.sleep(5)
        edit = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "edit-wireless-24")))
        edit.click()
        ssid = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "w-ssid-24")))
        ssid.clear()
        ssid.send_keys("SSID")
        time.sleep(5)
        password_2g = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "w-personal-pass-24")))
        password_2g.clear()
        password_2g.send_keys("Qwerty123")

    def edit_ssid_pass_5g(self):
        time.sleep(5)
        edit = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "edit-wireless-50")))
        edit.click()
        ssid = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "w-ssid-50")))
        ssid.clear()
        ssid.send_keys("Linksys_5g")
        time.sleep(5)
        password_2g = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "w-personal-pass-50")))
        password_2g.clear()
        password_2g.send_keys("Asdf3210")

    def network_mode_2g(self, net_mode):

        try:

            dropdown_netmode_2g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-network-mode-24")))
            dropdown_2g = Select(dropdown_netmode_2g)
            logger.info("Available option:")
            for option in dropdown_2g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Network mode: ")
            dropdown_2g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def security_mode_2g(self, net_mode):

        try:
            dropdown_securitymode_2g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-security-24")))
            dropdown_2g = Select(dropdown_securitymode_2g)
            logger.info("Available option:")
            for option in dropdown_2g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Security mode: ")
            dropdown_2g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def channel_width_2g(self, net_mode):

        try:
            dropdown_channel_width_2g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-channel-width-24")))
            dropdown_5g = Select(dropdown_channel_width_2g)
            logger.info("Available Channel width option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Channel Width mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def channel_2g(self, net_mode):

        try:
            dropdown_channel_2g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-channel-24")))
            dropdown_5g = Select(dropdown_channel_2g)
            logger.info("Available Channel option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select channel mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def network_mode_5g(self, net_mode):

        try:
            dropdown_netmode_5g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-network-mode-50")))
            dropdown_5g = Select(dropdown_netmode_5g)
            logger.info("Available option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select network mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def security_mode_5g(self, net_mode):

        try:
            dropdown_securitymode_5g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-security-50")))
            dropdown_5g = Select(dropdown_securitymode_5g)
            logger.info("Available option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Security mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")


    def channel_width_5g(self, net_mode):

        try:
            dropdown_channel_width_5g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-channel-width-50")))
            dropdown_5g = Select(dropdown_channel_width_5g)
            logger.info("Available option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Channel Width mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")

    def channel_5g(self, net_mode):

        try:
            dropdown_channel_5g = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "w-channel-50")))
            dropdown_5g = Select(dropdown_channel_5g)
            logger.info("Available option:")
            for option in dropdown_5g.options:
                logger.info(option.text)
            # net_mode = input(
            #     "Select Channel mode: ")
            dropdown_5g.select_by_visible_text(net_mode)
            logger.info(f"Sucessfully selected the mode: {net_mode}")
        except Exception as e:
            logger.error(f"Network mode selecting error: {e}")


    def apply_changes(self):
        apply_changes = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//article[@id='wireless-applet']/footer/button")))
        apply_changes.click()
        confirm_changes = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='wireless-disconnect-warning']/div[3]/button[2]")))
        confirm_changes.click()
        confirm_applied_changes = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "confirm")))
        confirm_applied_changes.click()


# if __name__ == '__main__':
#     browser_action = APAutomation(self.password, self.driver)
#
#     password = 'admin'
#     login_cred = r"C:\Users\PycharmProjects\PycharmTest\Router_AP_Automation\base_drivers\credentials.json"
    # APAutomation.edit_ssid_pass_2g(setup('request'))

#     try:
#         with open(login_cred, "r") as file:
#             login_data = json.load(file)
#             network_config = login_data.get("network_config", {})
#             password = network_config.get("password", "")
#
#     except json.JSONDecodeError as e:
#         logger.error(f"Error, failed to open json file {e}")
#
#     login_browser = Login(password, driver)
#     browser_action = APAutomation(password, driver)
#
#     try:
#         login_browser.open_browser()
#         login_browser.login_ap()
#         browser_action.wireless_mode()
#         print("wireless main click...")
#
#         select_netmode = input("Select Network mode: 2g, 5g: \n")
#         if select_netmode == "2g":
#             browser_action.edit_ssid_pass_2g()
#             browser_action.network_mode_2g()
#             browser_action.security_mode_2g()
#             browser_action.channel_width_2g()
#             browser_action.channel_2g()
#             time.sleep(5)
#         else:
#             browser_action.edit_ssid_pass_5g()
#             browser_action.network_mode_5g()
#             browser_action.security_mode_5g()
#             browser_action.channel_width_5g()
#             browser_action.channel_5g()
#             time.sleep(5)
#
#         browser_action.apply_changes()
#
#     except Exception as e:
#         logger.error(f"Browser error: {e}")

