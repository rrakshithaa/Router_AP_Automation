import pytest
from page_ap.login import Login
from page_ap.ap_config import APAutomation
from selenium import webdriver

driver = webdriver.Chrome()
password = "admin"


class TestLinksysAP:
    @pytest.mark.usefixture(scope="class")
    def setup(self):
        self.password = password
        self.driver = driver



    def test_open_browser(self):
        login_page = Login(password, driver)
        login_page.open_browser()
        login_page.login_ap()
        login_page.wireless_mode()

    def test_edit_ssid_pass_2g(self):
        ap_automate = APAutomation(password, driver)
        # self.test_open_browser()
        ap_automate.edit_ssid_pass_2g()
        ap_automate.network_mode_2g("Mixed")
        ap_automate.security_mode_2g("WPA2/WPA Mixed Personal")
        ap_automate.channel_2g("Auto")
        ap_automate.channel_width_2g("Auto")


    def test_edit_ssid_pass_5g(self):
        ap_automate = APAutomation(password, driver)
        # self.test_open_browser()
        ap_automate.edit_ssid_pass_5g()
        ap_automate.network_mode_5g("Mixed")
        ap_automate.security_mode_5g("WPA2/WPA Mixed Personal")
        ap_automate.channel_5g("Auto")
        ap_automate.channel_width_5g("Auto")


    def apply_changes(self):
        ap_automate = APAutomation(password, driver)
        ap_automate.apply_changes()

