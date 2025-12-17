import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def set_kadaster_number(browser, kadaster_number):
    

    m_slider = browser.find_element(By.TAG_NAME, 'm-sidebar')
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', m_slider)
    
    input_shadow_root = shadow_root.find_element(By.ID, 'header').find_element(By.TAG_NAME, 'm-search-field')
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', input_shadow_root)
    shadow_root.find_element(By.CSS_SELECTOR, 'form input').click()
    time.sleep(5)
    shadow_root.find_element(By.CSS_SELECTOR, 'form input').send_keys(kadaster_number)
    shadow_root.find_element(By.CSS_SELECTOR, 'form input').send_keys(Keys.ENTER)
    time.sleep(5)


def go_to_page_of_kadastr_map(browser):
    browser.find_element(By.ID, 'details-button').click()
    time.sleep(2)
    browser.execute_script('window.scroll(0, 600)')
    time.sleep(2)
    browser.find_element(By.ID, 'proceed-link').click()
    time.sleep(2)
    karta =  browser.find_element(By.CLASS_NAME, 'citySelectInput')
    karta.clear()
    karta.send_keys('Тамбовская область')
    time.sleep(2)
    # browser.find_element(By.ID, '436').click()
    browser.find_element(By.CLASS_NAME, "citySelectOk").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[text()='Публичная кадастровая карта']").click()
    time.sleep(2)
    browser.find_element(By.ID, 'details-button').click()
    time.sleep(2)
    browser.execute_script('window.scroll(0, 600)')
    time.sleep(2)
    browser.find_element(By.ID, 'proceed-link').click()
    time.sleep(10)


def set_type_land_plots(browser):
    plot_shadow_root1 = find_root_element(browser)
    shadow_button = plot_shadow_root1.find_element(By.CSS_SELECTOR, '.folder m-button')
    plot_shadow_root = browser.execute_script('return arguments[0].shadowRoot', shadow_button)
    time.sleep(5)
    plot_shadow_root.find_element(By.CSS_SELECTOR, 'button').click()

    plot_shadow_root1 = find_root_element(browser)
    shadow_check_box = plot_shadow_root1.find_elements(By.CSS_SELECTOR, 'm-layers-tree-layer')[0]
    check_box = browser.execute_script('return arguments[0].shadowRoot', shadow_check_box)
    shadow_button1 = check_box.find_element(By.CSS_SELECTOR, '.layer m-checkbox')

    shadow_button2 = browser.execute_script('return arguments[0].shadowRoot', shadow_button1)
    check_box1 = shadow_button2.find_element(By.CSS_SELECTOR, 'm-typography')
    time.sleep(5)
    content_shadow_root1 = browser.execute_script('return arguments[0].shadowRoot', check_box1)
    content_shadow_root1.find_element(By.CSS_SELECTOR, 'span').click()




def find_root_element(browser):
    m_slider_content = browser.find_element(By.TAG_NAME, 'm-sidebar')
    main_shadow_root = browser.execute_script('return arguments[0].shadowRoot', m_slider_content)

    first_shadow_root = main_shadow_root.find_element(By.CLASS_NAME, 'content').find_element(By.CSS_SELECTOR, 'layers-tree-ui')
    content_shadow_root = browser.execute_script('return arguments[0].shadowRoot', first_shadow_root)
    defoult_shadow_root = content_shadow_root.find_element(By.ID, 'default-layers-tree')

    template = defoult_shadow_root.find_element(By.CLASS_NAME, 'template')
    second_shadow_root = template.find_element(By.CLASS_NAME, 'layers').find_elements(By.CSS_SELECTOR, 'm-layers-tree-folder')[2]
    plot_shadow_root1 = browser.execute_script('return arguments[0].shadowRoot', second_shadow_root)

    return plot_shadow_root1


def click_root_element(browser):
    m_slider_click = browser.find_element(By.TAG_NAME, 'm-sidebar')
    click_shadow_root = browser.execute_script('return arguments[0].shadowRoot', m_slider_click)

    objects_shadow_root = click_shadow_root.find_element(By.CLASS_NAME, 'content').find_element(By.CSS_SELECTOR, 'm-found-objects')
    accordion_shadow_root = browser.execute_script('return arguments[0].shadowRoot', objects_shadow_root)
    accordion = accordion_shadow_root.find_element(By.CSS_SELECTOR, 'm-accordion')

    click_element = browser.execute_script('return arguments[0].shadowRoot', accordion)
    click_element.find_element(By.CSS_SELECTOR, 'button').click()
