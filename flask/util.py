import pickle
import joblib
import json
import numpy as py
import pandas as pd

__columns = None
__model = None

def get_predict_ontime(order_delivered_carrier_year, order_delivered_carrier_month, order_delivered_carrier_day, order_delivered_carrier_dayofweek, order_estimated_hour, product_weight_g_max, product_weight_g_sum, distance_sum, product_max_cm_sum, product_volume_cm_max, product_volume_cm_sum):
    new_sample = [[order_delivered_carrier_year, order_delivered_carrier_month, order_delivered_carrier_day, order_delivered_carrier_dayofweek, order_estimated_hour, product_weight_g_max, product_weight_g_sum, distance_sum, product_max_cm_sum, product_volume_cm_max, product_volume_cm_sum]]
    x = pd.DataFrame(new_sample)
    # x.columns = __columns

    predict = str(__model.predict(x)[0])
    if predict == "0":
        result = "Delay"
    else:
        result = "Ontime"
    return result

def retrain(X_new_filename, y_new_filename):

    '''
        X_new_filename, y_new_filename: csv file
    '''

    # X_new_filename = 'X_val.csv'
    # y_new_filename = 'y_val.csv'

    X_new = pd.read_csv(X_new_filename).values[:,1:]
    y_new = pd.read_csv(y_new_filename).values[:,1:].reshape(-1)

    print("Retraining model...start")
    global __model
    if __model is None:
        with open("flask/OntimePredictmodel.sav", "rb") as f:
            __model = joblib.load(f)

    __model.fit(X_new, y_new)

    pickle.dump(__model, open('./OntimePredictmodel_temp.pkl', 'wb'))
    joblib.dump(__model, open('./OntimePredictmodel_temp.sav', 'wb'))

    print("Retraining model...done")

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __model
    if __model is None:
        with open("./OntimePredictmodel.sav", "rb") as f:
            __model = joblib.load(f)
        print("Loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()