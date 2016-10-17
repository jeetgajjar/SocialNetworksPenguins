from selenium import webdriver
# import png

driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('http://10minutemail.com')
driver.save_screenshot('tenminutemail.png')
