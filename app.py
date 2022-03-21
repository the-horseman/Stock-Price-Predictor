from flask import Flask, render_template, request, jsonify
# import tensorflow as tf
import pandas as pd
import numpy as np
import requests
import json

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
        headers = {'x-api-key': "fKQUxQHM0o5rek4MhOLTM85GXHsqJHBv4UKFbLim"}
        response = requests.request("GET", url, headers=headers)
        ex = json.loads(response.text)["finance"]["result"][0]["recommendedSymbols"]
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
        gra_data = pd.read_csv( path, usecols=["Date", gra_tp], parse_dates=True, infer_datetime_format=True)
        ls = gra_data.tail(int(gra_tme)).to_numpy().tolist()
        graph_dic = {"fin_dat": ls}
    return jsonify(graph_dic)


@app.route("/data", methods=["POST"])
def processing():
    dat_dict = {}
    if request.method == "POST":
        data = request.get_json(force=True)
        stock = data["fro"][0]["value"]
        graph = data["fro"][1]["value"]
        time = data["fro"][2]["value"]
        # print(stock, graph, time);
        dir = "Data\\"+stock+"\\"+stock+".csv"
        # predicted values
        pred_arr = pred(dir)
        # predicted values

        # Total data for gragh
        tot_arr = tot_data(dir, graph)
        # Total data for gragh

        # Select required data for graph
        fin_arr = sel_data(tot_arr, time)
        # Select required data for graph

        dat_dict["Pred Data"] = pred_arr
        dat_dict["Graph Data"] = fin_arr

    return jsonify(dat_dict)


def pred(dir):
    n_input = 1
    n_features = 4
    data = pd.read_csv(dir, usecols=["Date", "Open", "Adj Close",
                       "High", "Low"], index_col='Date', parse_dates=True).to_numpy()

    first_eval_batch = data[-n_input:]
    current_batch = first_eval_batch.reshape((1, n_input, n_features))
    current_pred = model.predict(current_batch)[0][0]
    return current_pred


if __name__ == "__main__":
    app.run()
