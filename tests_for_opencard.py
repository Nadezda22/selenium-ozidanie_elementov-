from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.url)
    header_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "top-links")))
    elements = header_links.find_elements(By.TAG_NAME, 'li')
    assert len(elements) == 7
    logo = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "logo")))
    assert logo.text == "Your Store"
    search = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.NAME, "search")))
    assert search.get.atribute("placeholder") == "Search"
    menu = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.ID, "menu")))
    assert "Software" in menu.text
    footer_rights = WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer > div > p")))
    assert "Your Store © 2021" in footer_rights.text


def test_catalog_page(browser):
    browser.get(browser.url + "index.php?route=product/category&path=18")
    name_ctgr = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2")))
    assert "Laptops & Notebooks" == name_ctgr.text
    content = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div:nth-child(7)")))
    elements = content.find_elements(By.CLASS_NAME, 'product-layout')
    assert len(elements) == 5
    sort_filter = browser.find_element(By.CSS_SELECTOR, "#input-sort > option[selected]")
    assert "Default" == sort_filter.text
    add_to_cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")))
    assert add_to_cart_btn.find_element(By.TAG_NAME, "span").text == "ADD TO CART"


def test_product_card(browser):
    browser.get(browser.url + "index.php?route=product/product&path=18&product_id=47")
    product_tittle = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 h1")))
    assert product_tittle == "HP LP3065"
    product_price = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content .col-sm-4 > .list-unstyled h2")))
    assert product_price.text == "$122.00"
    cart_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    assert cart_btn.is_enabled()
    product_description = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#tab-description")))
    assert "HP LP3065" in product_description.text


def test_log_in_admin_page(browser):
    browser.get(browser.url + "/admin")
    username_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, "input-username")))
    assert username_field.get_attribute("placeholder") == "username"
    password_field = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID, "input-password")))
    assert password_field.get_attribute("placeholder") == "password"
    forgotten_pswd = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Forgotten Password")))
    assert forgotten_pswd == "Forgotten Password"
    login_btn = WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    assert login_btn.text == "Login"
    assert login_btn.is_enabled()


def test_registrator_page(browser):
    browser.get(browser.url + "index.php?route=account/register")
    page_tittle = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > h1")))
    assert page_tittle.text == "Register Account"
    account_links = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".list-group")))
    assert ("Register" in account_links.text) and ("My account" in account_links.text)
    password_fieldset = WebDriverWait(browser, ).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "fieldset:nth-child(2)")))
    password_fields = password_fieldset.find_elements(By.CSS_SELECTOR, "input")
    for i in password_fields:
        assert i.get_attribute("type") == "password"
    continue_btn = WebDriverWait(browser, 2).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='submit']")))
    assert continue_btn.is_enabled()
