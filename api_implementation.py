import json
import requests


url = 'http://127.0.0.1:8000/diabetes_prediction'
# url ='https://heroku-diabetes-predict.herokuapp.com/diabetes_prediction'

input_data_for_model = {
    
    # 'pregnancies' : 5,
    # 'Glucose' : 166,
    # 'BloodPressure' : 72,
    # 'SkinThickness' : 19,
    # 'Insulin' : 175,
    # 'BMI' : 25.8,
    # 'DiabetesPedigreeFunction' : 0.587,
    # 'Age' : 51

    'pregnancies' : 1,
    'Glucose' : 89,
    'BloodPressure' : 66,
    'SkinThickness' : 23,
    'Insulin' : 94,
    'BMI' : 28.1,
    'DiabetesPedigreeFunction' : 0.167,
    'Age' : 21
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

