import pytest
import re
from pages.home_page import HomePage
from pytest_check import check

from models.HomeLinks import HomeLinks

@pytest.mark.usefixtures("setup")
class TestMainPage:
    def test_home_has_title(self) -> None:
        home_page = HomePage(self.driver)

        assert(home_page.driver.title, re.compile("JDA Quality Enterprises Limited"))

    def test_home_has_links(self) -> None:
        home_page = HomePage(self.driver)

        with check:
            assert(home_page.home_link.text, HomeLinks.Home)
        with check:
            assert(home_page.contact_link.text, HomeLinks.Contact)
        with check:
            assert(home_page.aboutus_link.text, HomeLinks.AboutUs)
        with check:
            assert(home_page.clients_link.text, HomeLinks.Clients)
        with check:
            assert(len(home_page.email_links), 1)