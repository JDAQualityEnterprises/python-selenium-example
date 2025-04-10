
import json
import pytest

from framework.driver_factory import DriverFactory
from pathlib import Path

CONFIG_PATH = "config.json"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


@pytest.fixture(scope='session')
def config():
    stat_file = Path(CONFIG_PATH)
    if stat_file.is_file():
        config_file = open(CONFIG_PATH)
        return json.load(config_file)
    return

@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope='session')
def wait_time_setup(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def url_setup(config):
    return config.getini('base_url')


@pytest.fixture()
def setup(request, config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    #if request.session.testsfailed != before_failed:
        # TODO - set screenshot
    driver.quit()