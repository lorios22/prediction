#primero estan las librerias instaladas en python
import logging

#segundo las que debo instalar
from flask import Flask, render_template, request
import pandas as pd

#tercero los modulos que traigo 
import predictor  # type: ignore

#API QUE NOS PERMITA IDENTIFICAR EL TIPO DE FLOR
app = Flask(__name__)

def read_data(request_file):
    data = pd.read_csv(request_file)
    return data.iloc[4,:].values()

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        #Make predictions
        if 'file' in request.files:
            #Info es para un usuario que no conoce el sistema
            app.logger.info("No file")
            return "No file loaded"
        #En python los diccionarios tienen una funcion que se llama get, si no existe retorna un none, no revienta
        request_file = request.files.get('file')
        
        if request_file.filename == "":
            return "No file selected"
        data= read_data(request_file=request_file)
        result = predictor.predict(data=data)
        return result
    return render_template("upload_data.html")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True, use_reloader=False)
    

