# Imports libraries required for Python dependencies
import requests
import time
import json
import datetime
import os

# Welcome text
os.system('clear')
print("")
print("|-------------------------------------------|")
print("|    MagicStats v0.2.0 by Matz Trollmann    |")
print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
print("|  Github: https://github.com/Trollmann82/  |")
print("|-------------------------------------------|")
print("")

# Blockchain data
blocktimesec = 120
block24h = 86400 / blocktimesec
reward = 10
dailyprod = block24h * reward

# User options
mining = float(input("Input your expected hashrate in MH/s: "))
wallet = str(input("Input your wallet address here: "))

# Pool choice menu
print("1 = Angrypool\n"
    "2 = Bsod\n"
    "3 = solo mining")
poolchoice = int(input("Choose pool: "))
if poolchoice == 1:
    pool = f"http://angrypool.com/api/walletEx?address="
    poolname = str("mining on Angrypool")
if poolchoice == 2:
    pool = f"http://api.bsod.pw/api/walletEx?address="
    poolname = str("mining on Bsod")
if poolchoice == 3:
    pool = str("")
    poolname = str("solo mining")
# Screen choice menu
print("1 = Clear screen on every update (good for tidy information)\n"
    "2 = Rolling data (good for being able to see historical data)")
screenchoice = int(input("Choose behaviour: "))
# Choosing fiat currency
print("1 = USD\n"
      "2 = EUR\n"
      "3 = SEK")
fiatchoice = int(input("Choose fiat currency: "))
if fiatchoice == 1:
    fiatcurr = str("USD")
if fiatchoice == 2:
    fiatcurr = str("EUR")
if fiatchoice == 3:
    fiatcurr = str("SEK")

# Static variables
gh = 1000000000
mh = 1000000
kh = 1000
gin = 'Gincoin'

os.system('clear')
# Code to loop
while True :

    # Gets API data
    fiatapi = f"https://free.currencyconverterapi.com/api/v5/convert?q=USD_{fiatcurr}&compact=ultra"
    cryptoapi = "https://api.coinmarketcap.com/v2/ticker/2773/"
    ginresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    poolurl = f"{pool}{wallet}"
    # Calculations from API data from coin block explorer
    ginhash = float(ginresp.text)
    perchash = round(mining * gh / ginhash / 10,5)
    dailycoins = round(dailyprod * perchash / 100, 4)
    # Calculations for fiat currency API data
    fiatresponse = requests.get(fiatapi)
    fiatdata = fiatresponse.text
    fiatparsed = json.loads(fiatdata)
    fiat = fiatparsed[f"USD_{fiatcurr}"]
    # Calculations from API data from Coinmarketcap
    response = requests.get(cryptoapi)
    data = response.text
    parsed = json.loads(data)
    price = parsed["data"]["quotes"]["USD"]["price"]
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # API data from pool
    if poolchoice == 1 or poolchoice == 2:
        poolresponse = requests.get(poolurl)
        data = poolresponse.text
        parsed = json.loads(data)
        total24htext = parsed['total']
        last24h = round(total24htext,4)
    time.sleep(5)
    if screenchoice == 1:
        os.system('clear')
    # Prints data to screen every 5 minutes
    print("")
    print("|-------------------------------------------|")
    print("|    MagicStats v0.2.0 by Matz Trollmann    |")
    print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
    print("|  Github: https://github.com/Trollmann82/  |")
    print("|-------------------------------------------|")
    print("")
    print(today)
    print("You are currently ",poolname," on the address ", wallet,".",sep='')
    print("The current hashrate for",gin,"is",round(ginhash / gh,4),"GH/s.")
    print("Your expected hashrate of",mining,"MH/s makes out",perchash,"% of the network.")
    print("Expected daily production is currently ", dailycoins," ",gin," per day, at an estimated value of ", round(price*dailycoins*fiat,2)," ",fiatcurr,".",sep='')
    if poolchoice == 1 or poolchoice == 2:
        print("You have mined",last24h,gin,"in the last 24 hours for a total value of",round(price*last24h*fiat,2),fiatcurr)
    if poolchoice == 3:
        dailyblocks = round(dailycoins / reward, 3)
        print("You will mine an estimated",dailyblocks,"blocks per day, or recieve a block every",round(24 / dailyblocks,2),"hours.")

    time.sleep(295)

