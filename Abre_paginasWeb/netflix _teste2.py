from selenium import webdriver

driver = webdriver.iexplorer()
driver.get("https://www.netflix.com/Login")
while True:
    element = driver.find_element_by_css_selector("ui-text-input[name = 'email']")
    driver.execute_script("arguments[0].setAttribute('value','test1')", element)
    element2 = driver.find_element_by_css_selector("ui-text-input[name = 'password']")
    driver.execute_script("arguments[0].setAttribute('value','test1')", element2)
    driver.refresh()