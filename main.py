import logging
import os
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOGIN_PAGE = "https://ruokaboksi.fi/oma-tili/"
RECIPE_PAGE = "https://ruokaboksi.fi/resepti/?taxonomy=ruokaboksi_recipe_weeks"
RECIPE_BASE_URL = "https://ruokaboksi.fi/resepti/"
USER_EMAIL = os.environ['RB_USERNAME']
USER_PWD = os.environ['RB_PASSWORD']
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler()])
logger = logging.getLogger()


def main():
    driver = getWebdriver()
    rbLogin(driver)
    rbRecipePage(driver)
    rbCrawler(driver)


# Crawls the page for recipe-links.
def rbCrawler(driver):
    recipes = driver.find_elements_by_xpath("//div[@class='recipes']/div[@class='recipe']")
    for recipe in recipes:
        title = recipe.find_element_by_xpath("./div[@class='text']/h4[@class='title']").get_attribute("innerHTML")
        click_action = recipe.get_attribute("onclick")
        url_match = re.findall("https:\/\/ruokaboksi\.fi\/resepti\/([^\/]*)\/", click_action)
        if url_match:
            slug = url_match[0]
            url = f"{RECIPE_BASE_URL}/{slug}"
            print(f"Scraping recipe {title} with url {url}")


def rbRecipePage(driver):
    driver.get(RECIPE_PAGE)


def rbLogin(driver):
    driver.get(LOGIN_PAGE)
    # Enter username.
    username_field = driver.find_element_by_id("username")
    username_field.clear()
    username_field.send_keys(USER_EMAIL)

    # Enter password.
    password_field = driver.find_element_by_id("password")
    password_field.clear()
    password_field.send_keys(USER_PWD)

    # Click login.
    driver.find_element_by_name("login").click()


def getWebdriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    logger.info(f"Created new chrome session with id {driver.session_id} / executor_url {driver.command_executor._url}")
    return driver


if __name__ == "__main__":
    main()
