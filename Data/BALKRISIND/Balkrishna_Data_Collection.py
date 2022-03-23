from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd

def Balkrishna_Data():
    options = webdriver.ChromeOptions() ;
    prefs = {"download.default_directory" : os.path.dirname(os.path.realpath(__file__))}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=options)

    # driver = webdriver.Chrome()

    driver.get("https://finance.yahoo.com/quote/BALKRISIND.NS/history?p=BALKRISIND.NS")
    print(driver.title)

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div').click()

    from datetime import datetime, timedelta
    tom = datetime.now() + timedelta(1)
    tom = tom.strftime('%d-%m-%Y')
    tom = "".join(tom.split('-'))
    driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/div[2]/input').send_keys(tom)

    driver.find_element(By.XPATH, '//*[@id="dropdown-menu"]/div/ul[1]/li[1]/button').click()

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/button').click()

    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a').click()

    time.sleep(30)
    driver.quit()
    
def Balkrish_data_add():
    path1 = os.path.dirname(os.path.realpath(__file__)) + "/BALKRISIND.NS.csv"
    path2 = os.path.dirname(os.path.realpath(__file__)) + "/BALKRISIND.NS (1).csv"
    dataframe1 = pd.read_csv(path1)
    findat1 = dataframe1.tail(1).to_numpy().tolist()
    dataframe2 = pd.read_csv(path2)
    findat2 = dataframe2.tail(1).to_numpy().tolist()
    print(findat1 == findat2)
    if (findat1 != findat2):
        with open(path1, 'a', newline='') as f_object:
            f_object.write(",".join(list(map(str,findat2[0])))+"\n")
        Balkrish_train()
    os.remove(path2)

def Balkrish_train():
    import joblib
    import tensorflow as tf
    from keras.preprocessing.sequence import TimeseriesGenerator
    sc_path = os.path.dirname(os.path.realpath(__file__)) + "/BALKRISIND_scaler.pkl"
    md_path = os.path.dirname(os.path.realpath(__file__)) + "/BALKRISIND_model.h5"
    fil_path = os.path.dirname(os.path.realpath(__file__)) + "/BALKRISIND.NS.csv"
    scaler = joblib.load(sc_path)
    rnn = tf.keras.models.load_model(md_path)
    df = pd.read_csv(fil_path, usecols=["Date", "Open", "Adj Close", "High", "Low"], index_col='Date',parse_dates=True)
    df = df[-2::]
    sc_t = scaler.transform(df)
    gene = TimeseriesGenerator(sc_t, sc_t, 1, batch_size=1)
    rnn.fit(gene, epochs=10)
    rnn.save("BALKRISIND_model.h5")


def balkrish_run():
    Balkrishna_Data()
    Balkrish_data_add()