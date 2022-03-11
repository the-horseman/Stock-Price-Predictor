from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/data", methods = ["POST"])
def processing():
    dat_dict = {}
    if request.method == "POST":
        data = request.get_json(force=True)
        stock = data["fro"][0]["value"]
        graph = data["fro"][1]["value"]
        time = data["fro"][2]["value"]

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
    data = pd.read_csv(dir, usecols=["Date", "Open", "Adj Close", "High", "Low"], index_col='Date',parse_dates=True).to_numpy()
    
    first_eval_batch = data[-n_input:]
    current_batch = first_eval_batch.reshape((1, n_input, n_features))
    current_pred = model.predict(current_batch)[0][0]
    return current_pred



def tot_data(stck, grgh):
    data = pd.read_csv(dir, usecols=["Date", "Open", "Adj Close", "High", "Low"], index_col='Date',parse_dates=True)
    return stck

def sel_data(tot_arr, tme):
    return tot_arr

if __name__ == "__main__":
    app.run()
