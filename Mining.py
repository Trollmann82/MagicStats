# Imports libraries required for Python dependencies
import requests
import time
import json
import datetime

# Welcome text
print("")
print("|---------------------------------------|")
print("|  MagicStats v0.0.3 by Matz Trollmann  |")
print("|---------------------------------------|")
print("")

# Blockchain data
blocktimesec = 120
block24h = 86400 / blocktimesec
reward = 10
dailyprod = block24h * reward

# User options
mining = float(input("Input your expected hashrate in MH/s: "))
wallet = str(input("Input your wallet address here: "))

# Static variables
gh = 1000000000
mh = 1000000
kh = 1000
gin = 'Gincoin'

# Code to loop
while True :

    # Gets API data
    url = "https://api.coinmarketcap.com/v2/ticker/2773/"
    ginresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    poolurl = f"http://angrypool.com/api/walletEx?address={wallet}"
    # Calculations from API data from coin block explorer
    ginhash = float(ginresp.text)
    perchash = round(mining * gh / ginhash / 10,5)
    dailycoins = round(dailyprod * perchash / 100, 4)
    # Calculations from API data from Coinmarketcap
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    price = parsed["data"]["quotes"]["USD"]["price"]
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # API data from pool
    poolresponse = requests.get(poolurl)
    data = poolresponse.text
    parsed = json.loads(data)
    total24htext = parsed['total']
    last24h = round(total24htext,4)
    # Prints data to screen on chosen interval
    print(today,'The current hashrate for',gin,'is',round(ginhash / gh,4),'GH/s.')
    print(today,"Your expected hashrate of",mining,"MH/s makes out",perchash,"% of the network.")
    print(today,"Expected daily production is currently",dailycoins,gin,"per day, at an estimated value of",round(price*dailycoins,2),"USD.")
    print(today,"You have mined",last24h,gin,"in the last 24 hours for a total value of",round(price*last24h,2),"USD")
    print(today, "-----     -----     -----     -----     -----     -----     -----     -----     -----     -----")
    time.sleep(300)

