from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# options = webdriver.ChromeOptions() ;
# prefs = {"download.default_directory" : "<directory_path>;
# prefs = {"download.default_directory" : "D:\Tutorial\down"};
# options.add_experimental_option("prefs",prefs);

driver = webdriver.Chrome()

driver.get("https://finance.yahoo.com/quote/UBER/history?p=UBER")
print(driver.title)

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div').click()

driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/ul[1]/li[2]/button').click()

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()
print("hlo")

time.sleep(15)
driver.quit()
