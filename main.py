import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOGIN_PAGE = "https://ruokaboksi.fi/oma-tili/"
USER_EMAIL = "paula.calais@icloud.com"
USER_PWD = "BR4N"
RECIPE_PAGE = "https://ruokaboksi.fi/resepti/?taxonomy=ruokaboksi_recipe_weeks"

def main():
    driver = getWebdriver()
    rbLogin(driver)
    rbRecipePage(driver)
    rbCrawler(driver)


# Crawls the page for recipe-links.
def rbCrawler(driver):
    pass


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
    return driver


if __name__ == "__main__":
    main()
