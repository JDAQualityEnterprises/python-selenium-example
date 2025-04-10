from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactsPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

        self.heading = self.driver.find_element(By.XPATH, "//h1")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )