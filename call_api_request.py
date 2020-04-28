import requests
import json

##Your API key: 607a95068f26a75cfe077e4c

##https://prime.exchangerate-api.com/v5/607a95068f26a75cfe077e4c/latest/USD

apiURL = 'https://prime.exchangerate-api.com/v5/607a95068f26a75cfe077e4c/latest/USD'
try:
    response = requests.get(apiURL)
    if (response.status_code == 200):
        print("Successfully conected to the server")
except Exception as e:
    print(e)
else:
    #currencyData = response.text
    #json_text = json.loads(currencyData)
    #json_bump=json.dumps(json_text,indent=2)
    #print(json_bump)
    jsondata = response.json()
    print(jsondata['conversion_rates'])
    """{'USD': 1, 'AED': 3.672, 'ARS': 66.4054, 'AUD': 1.5516, 'BGN': 1.8024,
    # 'BRL': 5.616, 'BSD': 1.0, 'CAD': 1.4056, 'CHF': 0.9741, 'CLP': 858.4989, 'CNY'
    ': 7.0854, '
    COP
    ': 4095.0, '
    CZK
    ': 25.0958, '
    DKK
    ': 6.8814, '
    DOP
    ': 54.8787, '
    EGP
    ': 15.7644, '
    EUR
    ': 0.9232, '
    FJD
    ': 2.266, '
    GBP
    ': 0.8053, '
    GTQ
    ': 7.7119, '
    HKD
    ': 7.7503, '
    HRK
    ': 6.9596, '
    HUF
    ': 327.2015, '
    IDR
    ': 15208.6498, '
    ILS
    ': 3.5122, '
    INR
    ': 76.215, '
    ISK
    ': 146.385, '
    JPY
    ': 107.2198, '
    KRW
    ': 1225.6659, '
    KZT
    ': 429.975, '
    MXN
    ': 24.8916, '
    MYR
    ': 4.3566, '
    NOK
    ': 10.5625, '
    NZD
    ': 1.6543, '
    PAB
    ': 1.0, '
    PEN
    ': 3.3968, '
    PHP
    ': 50.7348, '
    PKR
    ': 158.9556, '
    PLN
    ': 4.1791, '
    PYG
    ': 6615.0, '
    RON
    ': 4.4619, 'RUB': 74.3653, '
    SAR
    ': 3.7556, '
    SEK
    ': 10.0255, '
    SGD
    ': 1.4196, '
    THB
    ': 32.462, '
    TRY
    ': 6.9833, '
    TWD
    ': 30.0535, '
    UAH
    ': 27.0418, '
    UYU
    ': 43.608, '
    ZAR
    ': 18.8552}"""

    print("FInd the best currency Converter Ever")
    user_currency = input("Please Enter the ci=urrency that you would like to use :",).upper()
    user_amount =  input("Please Enter the amount to convert into USD :")
    amount_in_usd = jsondata['conversion_rates'][user_currency] * int(user_amount)
    print("The Total amount is :",amount_in_usd)
