from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd

def Reliance_Data():
    options = webdriver.ChromeOptions() ;
    prefs = {"download.default_directory" : os.path.dirname(os.path.realpath(__file__))}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=options)

    # driver = webdriver.Chrome()

    driver.get("https://finance.yahoo.com/quote/RELIANCE.NS/history?p=RELIANCE.NS")
    print(driver.title)

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div').click()

    driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/ul[1]/li[1]/button').click()

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()

    time.sleep(30)
    driver.quit()
    
def Rel_data_add():
    path1 = "RELIANCE.NS.csv"
    path2 = "RELIANCE.NS (1).csv"
    dataframe1 = pd.read_csv(path1)
    findat1 = dataframe1.tail(1).to_numpy().tolist()
    dataframe2 = pd.read_csv(path2)
    findat2 = dataframe2.tail(1).to_numpy().tolist()
    print(findat1 == findat2)
    if (findat1 != findat2):
        with open(path1, 'a', newline='') as f_object:
            f_object.write(",".join(list(map(str,findat2[0])))+"\n")

    os.remove(path2)

def Rel_run():
    Reliance_Data()
    Rel_data_add()