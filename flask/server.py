from flask import Flask, request, jsonify, Response
import util

app = Flask(__name__)

@app.route("/predict_ontime", methods = ['POST'])
def predict_ontime():
    # order_delivered_carrier_year = 0
    order_delivered_carrier_year = int(request.form['order_delivered_carrier_year'])
    order_delivered_carrier_month = int(request.form['order_delivered_carrier_month'])
    order_delivered_carrier_day = int(request.form['order_delivered_carrier_day'])
    order_delivered_carrier_dayofweek = int(request.form['order_delivered_carrier_dayofweek'])
    order_estimated_hour = float(request.form['order_estimated_hour'])
    product_weight_g_max = float(request.form['product_weight_g_max'])
    product_weight_g_sum = float(request.form['product_weight_g_sum'])
    distance_sum = float(request.form['distance_sum'])
    product_max_cm_sum = float(request.form['product_max_cm_sum'])
    product_volume_cm_max = float(request.form['product_volume_cm_max'])
    product_volume_cm_sum = float(request.form['product_volume_cm_sum'])

    response = jsonify({
        'predict_ontime' : util.get_predict_ontime(order_delivered_carrier_year, order_delivered_carrier_month, order_delivered_carrier_day, order_delivered_carrier_dayofweek, order_estimated_hour, product_weight_g_max, product_weight_g_sum, distance_sum, product_max_cm_sum, product_volume_cm_max, product_volume_cm_sum)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route("/retrain", methods = ['POST'])
def retrain():
    try:
        #X_new_filename??
        X_new_filename = request.form['X_new_path']
        y_new_filename = request.form['y_new_path']

        util.retrain(X_new_filename, y_new_filename)
    except Exception as e:
        return f"{e}"
    return "Retraing model done"

if __name__ == '__main__':
    print("Starting Python Flask Server For Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)


    
    

    





