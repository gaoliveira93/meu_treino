from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://forum.onipotentes.club/')