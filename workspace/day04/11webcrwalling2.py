from selenium import webdriver
import time

browser = webdriver.Chrome("D:/python/driver/chromedriver")
browser.get("http://www.python.org")

menus = browser.find_element_by_css_selector("#top ul.menu li")

pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)

