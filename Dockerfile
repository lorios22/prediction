FROM python:3.10
#nunca se deberia usar latest porque siempre deberia tener una version y trazabilidad en mi projecto 
RUN apt-get update

#le dice al build que siempre va a trabajar con este folder
#del workdir ejecuta toda la aplicacion
WORKDIR /app

COPY app.py app.py
COPY predictor.py predictor.py
COPY requirements.txt requirements.txt
COPY iris_model.pkl iris_model.pkl 

RUN pip install -r requirements.txt
#para hacer que se ejecuten la aplicacion 
CMD python app.p