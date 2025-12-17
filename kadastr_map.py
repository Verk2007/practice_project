import time

from selenium import webdriver

from pages.utils import (click_root_element,
                         go_to_page_of_kadastr_map,
                         set_kadaster_number,
                         set_type_land_plots)


link = "https://rosreestr.gov.ru/"

browser = webdriver.Chrome()
browser.get(link)
try:
    go_to_page_of_kadastr_map(browser)
    set_type_land_plots(browser)
    set_kadaster_number(browser, '68:29:0202003:728')
    click_root_element(browser)



finally:
    time.sleep(10)
    browser.quit()


