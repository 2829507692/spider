from selenium import webdriver
# browser=webdriver.Chrome()
# browser.get('http://www.baidu.com')
# s=browser.page_source
# print(s)
# browser.quit()
#######################################
#chrome浏览器无头模式
options=webdriver.ChromeOptions()
options.add_argument('--headless')
chrome=webdriver.Chrome(chrome_options=options)
#######################################
chrome.get('http://www.baidu.com')
html=chrome.page_source
print(html)
chrome.quit()
