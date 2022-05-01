# stalno radi , exit key
import requests
import json
a = 1
crypto = ['BTC', 'ETH']
stocks = ['IBM', ]
forex = []  # mozda ak mi bude dosadno
# kopirano, prikupljanje podataka

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + \
    crypto[0] + '&to_currency=USD&apikey=63Z0YWDRRE4A42JS'
r = requests.get(url)
data = r.json()
print(data)

while True:

    opt = int(input('1) crypto \n2) stocks\n99) exit'))

    if opt == 1:
        # crypto info
        oda = int(input('1)Bitcoin (BTC) \n2)Ether (ETH)\n'))
        i = oda - 1
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + \
            crypto[i] + '&to_currency=USD&apikey=63Z0YWDRRE4A42JS'
        r = requests.get(url)
        data = r.json()
        print(data)
    elif opt == 2:
        # stock info
        oda = int(input('1)IBM \n2)\n'))
        i = oda - 1
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + \
            stocks[i] + '&apikey=63Z0YWDRRE4A42JS'
        r = requests.get(url)
        data = r.json()
        print(data)
    elif opt == 99:
        break
