import pytest  
from pytest_bdd import scenarios, then, given, when
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from pages.github_page import GitHubPage


scenarios("../features/tc01.feature")

from selenium.webdriver.common.by import By
from protect.new import DriverFactory

# Fixture for WebDriver setup
@pytest.fixture(scope="function")
def setup():
    driver = DriverFactory.create_driver()
    yield driver
    driver.quit()

# Step Definitions

@given("I open the GitHub page")
def open_github_page(setup):
    github_page = GitHubPage(setup)
    github_page.open()

@when('I get the word count for "GitHub"')
def get_word_count(setup):
    github_page = GitHubPage(setup)
    setup.word_count = github_page.get_word_count("GitHub")

@then('I should see "GitHub" appear more than 0 times')
def verify_word_count(setup):
    assert setup.word_count > 0, f"'GitHub' should appear more than 0 times, but it appeared {setup.word_count}"
