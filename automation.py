from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
chrome_browser.implicitly_wait(4000)
chrome_browser.find_element_by_id('at-cv-lightbox-close').click()

assert 'Show Message' in chrome_browser.page_source

string = 'I am a SOFTWARE ENGINEER'
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys(string)

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert string == output_message.text

user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)

chrome_browser.close()
