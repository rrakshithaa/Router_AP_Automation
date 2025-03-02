import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    logger.info("🚀 Launching Chrome WebDriver...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
    logger.info("🛑 WebDriver closed.")


