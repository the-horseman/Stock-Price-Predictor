from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import pandas as pd
import numpy as np
import requests
import json
import joblib

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/view", methods=["POST"])
def also_view():
    view_dic = {"ans": []}
    if request.method == "POST":
        data = request.get_json(force=True)
        stock = data["viewed"]
        url = "https://yfapi.net/v6/finance/recommendationsbysymbol/"
        url = url + stock
        headers = {'x-api-key': "I0mOisEOsz3aCSJKF5hPUaTawLEZ4Uhv8uP8qtZn"}
        response = requests.request("GET", url, headers=headers)
        ex = json.loads(response.text)[
            "finance"]["result"][0]["recommendedSymbols"]
        for i in ex:
            ex1 = i["symbol"]
            ex2 = round(i["score"]*100, 2)
            view_dic["ans"].append([ex1, ex2])
    return jsonify(view_dic)


@app.route("/graph", methods=["POST"])
def graph_data():
    graph_dic = {}
    if request.method == "POST":
        data = request.get_json(force=True)
        gra_st = data["sto"]
        gra_tp = data["gra"]
        gra_tme = data["tme"]
        path = "Data/"
        path = path + gra_st[:-3:] + "/" + gra_st + ".csv"
        gra_data = pd.read_csv(
            path, usecols=["Date", gra_tp], parse_dates=True, infer_datetime_format=True)
        ls = gra_data.tail(int(gra_tme)).to_numpy().tolist()
        graph_dic = {"fin_dat": ls}
    return jsonify(graph_dic)


@app.route("/pred", methods=["POST"])
def processing():
    n_input = 1
    n_features = 4
    pred_dict = {}
    if request.method == "POST":
        data = request.get_json(force=True)
        st = data["sto"]
        print(st)
        dat_path = "Data/" + st[:-3:] + "/" + st + ".csv"
        df = pd.read_csv(dat_path, usecols=[
                         "Date", "Open", "Adj Close", "High", "Low"], index_col='Date', parse_dates=True)
        df = df.iloc[-1::]
        sc_path = "Data/" + st[:-3:] + "/" + st[:-3:] + "_scaler.pkl"
        md_path = "Data/" + st[:-3:] + "/" + st[:-3:] + "_model.h5"
        scaler = joblib.load(sc_path)
        sc_train = scaler.transform(df)
        rnn = tf.keras.models.load_model(md_path)
        fin_dat = sc_train[-n_input:]
        cur_batch = fin_dat.reshape((1, n_input, n_features))
        current_pred = rnn.predict(cur_batch)[0]
        fin_pred = scaler.inverse_transform(current_pred)[0]
        pred_dict["Open"] = str(fin_pred[0])
        pred_dict["High"] = str(fin_pred[1])
        pred_dict["Low"] = str(fin_pred[2])
        pred_dict["Close"] = str(fin_pred[3])
    return jsonify(pred_dict)


if __name__ == "__main__":
    app.run()
