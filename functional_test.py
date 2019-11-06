from selenium import webdriver
# webDriver 地址
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

browser.get('http://127.0.0.1:8000')
assert 'Django' in browser.title
