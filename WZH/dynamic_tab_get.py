from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os, time

CHROME_DRIVER_PATH = '/Library/Frameworks/Python.framework/Versions/3.6/chromedriver'


# 下载动态界面并返回子分类链接
def get_dynamic_htmlNavLink(site_url):
    print('开始加载', site_url, '动态页面')
    chrome_options = webdriver.ChromeOptions()
    # ban sandbox
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # use headless
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_options)
    # print('dynamic laod web is', site_url)
    driver.set_page_load_timeout(100)
    # driver.set_script_timeout(100)
    try:
        driver.get(site_url)
    except Exception as e:
        driver.execute_script('window.stop()')  # 超出时间则不加载
        print(e, 'dynamic web load timeout')
    action = ActionChains(driver)
    womwn_nav_tag = driver.find_element_by_css_selector('.z-navicat-header_categoryList')
    nav_tag_list = womwn_nav_tag.find_elements_by_css_selector('li')
    cate_list = []
    for tag in nav_tag_list:
        print(tag.text)
        action.move_to_element(tag).perform()
        time.sleep(5)
        a_tag_list = driver.find_elements_by_css_selector('a.z-navicat-header_subCategoryLink')
        for tag in a_tag_list:
            href = tag.get_attribute('href')
            if href != '':
                print(href)
                cate_list.append(href)
    try:
        driver.quit()
    except:
        pass
    return cate_list


site_url = 'https://www.zalando.de/damen-home/'
get_dynamic_htmlNavLink(site_url)