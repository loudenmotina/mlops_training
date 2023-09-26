from flask import Flask, jsonify, request
# import requests
from pickle import dump, load
from logzero import logger, logfile
from datetime import datetime
logfile("app.log", maxBytes=1e6, backupCount=3)
#!/usr/bin/env python
import snowflake.connector

# Gets the version
conn = snowflake.connector.connect(
    user='louden',
    password='Besingi1',
    account='recfctj-jlb68777',
    warehouse=config["snowflake_WAREHOUSE"],
    database=config["snowflake_DATABASE"],
    schema=config["snowflake_SCHEMA"]
    )

conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")
conn.cursor().execute("USE DATABASE testdb_mg")
conn.cursor().execute("USE SCHEMA testdb_mg.testschema_mg")
conn.cursor().execute(
    "CREATE OR REPLACE TABLE "
    "mlops_table(id interger, date string,predictions interger,actual interger)")

cur = conn.cursor()
cur.execute("select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.CUSTOMER limit 10")
# load the model
model = load(open('model.pkl', 'rb'))

app = Flask(__name__)
logger.info("Flask app started")
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
        values_list = [list(input_data.values())]
        prediction_result = model.predict(values_list)
        if prediction_result[0] == 0:
            prediction_result = "not likely to purchase"
        elif prediction_result[0] == 1:
            prediction_result = "highly likely to purchase"
        current_dateTime = datetime.now()
        formatted_datetime = current_dateTime.strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f'A request was made at {formatted_datetime} with INPUT DATA {input_data}  and the response was {prediction_result}')
        return jsonify({"predictions": prediction_result}), 200

    except Exception as e:
        logger.info(f'A request was made at {formatted_datetime} with INPUT DATA {input_data}  and the response was {prediction_result}')
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)


