import logging

logger  = logging.getLogger('foo')

class BasePage:
    URL: str
    BaseUrl : str

    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.open()