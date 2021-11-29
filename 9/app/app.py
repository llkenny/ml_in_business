import dill
from flask import Flask, request, jsonify
import os
import pandas as pd

dill._dill._reverse_typemap['ClassType'] = type

app = Flask(__name__)

with open('app/model/pipeline.dill', 'rb') as f:
		model = dill.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    df = pd.DataFrame({"Age": [request.form.get("Age", None)],
                       "Gender": [request.form.get("Gender", None)],
                       "Polyuria": [request.form.get("Polyuria", None)],
                       "Polydipsia": [request.form.get("Polydipsia", None)],
                       "sudden weight loss": [request.form.get("sudden weight loss", None)],
                       "weakness": [request.form.get("weakness", None)],
                       "Polyphagia": [request.form.get("Polyphagia", None)],
                       "Genital thrush": [request.form.get("Genital thrush", None)],
                       "visual blurring": [request.form.get("visual blurring", None)],
                       "Itching": [request.form.get("Itching", None)],
                       "Irritability": [request.form.get("Irritability", None)],
                       "delayed healing": [request.form.get("delayed healing", None)],
                       "partial paresis": [request.form.get("partial paresis", None)],
                       "muscle stiffness": [request.form.get("muscle stiffness", None)],
                       "Alopecia": [request.form.get("Alopecia", None)],
                       "Obesity": [request.form.get("Obesity", None)]})
    
    try:
        predict = model.predict(df)

        proba = model.predict_proba(df)
        proba_json = pd.Series(list(proba)).to_json(orient='values')

        return jsonify({'class':'Positive', 'proba': proba_json}) if predict == 1 else jsonify({'class':'Negative', 'proba': proba_json})
    except AttributeError as e:
        print(str(e))
        return jsonify(str(e)), 400

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)
