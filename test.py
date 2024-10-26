import requests

host = "med-app-env.eba-kcymnwx2.eu-west-1.elasticbeanstalk.com"
url = f'http://{host}/predict'
applicant = {"age": 25,
             "sex":"male",
             "bmi": 45.54,
             "children":2,
             "smoker":"yes",
             "region":"southeast"}

response = requests.post(url, json=applicant).json()
cost = response.get('predicted_medical_cost')
print(f"The predicted medical cost is {cost} yearly.")
