import time
import warnings
import json
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Drivers\\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox("C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Drivers\\geckodriver.exe")
    warnings.simplefilter('ignore', ResourceWarning)
    #driver = webdriver.Chrome("C:\\Users\\admin\\PycharmProjects\\SegundoProyecto\\Drivers\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

