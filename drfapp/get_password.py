import requests
url = "http://127.0.0.1:8000/api/token/"
data = {'username': 'admin', 'password': 'admin'}
response = requests.post(url, data=data)
print("Status Code:", response.status_code)
print("Response Content:", response.text)