from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions() ;
prefs = {"download.default_directory" : "D:\\Stocks-Data\\Uber\\"}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=options)

# driver = webdriver.Chrome()

driver.get("https://finance.yahoo.com/quote/UBER/history?p=UBER")
print(driver.title)

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div').click()

driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/ul[1]/li[2]/button').click()

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()

time.sleep(60)
driver.quit()