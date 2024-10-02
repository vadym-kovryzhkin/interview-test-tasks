import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = ""
    # yield driver
    driver.close()

