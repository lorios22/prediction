import pickle
def predict(data):
    #Load model
    with open("iris_model.pkl","rb") as f:
        model = pickle.load(f)
    result =  model.predict(data)
    return list(result)