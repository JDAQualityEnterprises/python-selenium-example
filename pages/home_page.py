
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from models.HomeLinks import HomeLinks


class HomePage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)

        self.open()

        displayed_list = self.driver.find_element(By.XPATH, "//nav[contains(@style, 'visible')]/ul")

        self.home_link = displayed_list.find_element(By.XPATH, f"./li[contains(.,'{'Home'}')]")
        self.contact_link = displayed_list.find_element(By.XPATH, f"./li[contains(.,'{'Contact'}')]")
        self.aboutus_link = displayed_list.find_element(By.XPATH, f"./li[contains(.,'{'About Us'}')]")
        self.clients_link = displayed_list.find_element(By.XPATH, f"./li[contains(.,'{'Clients'}')]")

        self.click_contact_link = displayed_list.find_element(By.XPATH, f"./li[contains(.,'{'Contact'}')]//a")

        self.email_links = driver.find_elements(By.XPATH, f"//a[contains(.,'{HomeLinks.Email}')]")
