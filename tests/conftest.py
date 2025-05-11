import pytest
from selenium import webdriver

from utilities import Readconfigurations


@pytest.fixture()
def setup_and_teardown(request):
    driver=None
    browser=Readconfigurations.read_config("info","browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver=webdriver.Edge
    else:
        print("provide only chrome or edge in browser key")
    request.cls.driver = driver
    url=Readconfigurations.read_config("info","url")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.quit()
