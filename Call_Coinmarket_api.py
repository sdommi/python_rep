import requests
import json

##API Key=""

apiURL =  'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    "start":1,
    "limit":100,
    "convert":"USD",
    "CMC_PRO_API_KEY":"USER YOUR OWN API"
}
try:
    response = requests.get(apiURL,params=parameters)
    if response.status_code==200:
        print("Successfully Connected to the server")
    print(response)
except Exception as e:
    print(e)
else:
    data = json.loads(response.text)
    with open('coinsdata.json','w') as fw:
        j_dump =json.dumps(data,indent=4)
        fw.write(json.dumps(data,indent=4))
