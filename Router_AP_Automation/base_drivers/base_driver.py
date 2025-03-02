import time


class BaseDriver:
    def __init__(self, driver, password):
        self.driver = driver
        self.password = password
