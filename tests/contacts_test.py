import pytest
from pages.home_page import HomePage
from pages.contacts_page import ContactsPage

@pytest.mark.usefixtures("setup")
class TestContactsPage:
    def test_contact_page_has_title(self) -> None:
        home_page = HomePage(self.driver)

        home_page.click_contact_link.click()

        contacts_page = ContactsPage(self.driver)

        assert(contacts_page.heading.text, "Contact")