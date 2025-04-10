from selenium import webdriver
from framework.webdriver_listener import WebDriverListener
from framework.webdriver_extension import WebDriverExtension


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtension:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument("no-sandbox")
            options.add_argument("disable-dev-shm-usage")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = WebDriverExtension(
                webdriver.Chrome(options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtension(
                webdriver.Firefox(options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "edge":
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtension(
                webdriver.Edge(options=options),
                WebDriverListener(), config
            )
            return driver
        raise Exception("Provide valid driver name")