import requests


response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
# print(response.json)

complete_details = response.json()

for i in range(len(complete_details)):
    print(i)