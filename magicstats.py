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
print("|  MagicStats v0.2.2.6.2 by Matz Trollmann  |")
print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
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

# Coin choice menu
#print("1 = Gincoin\n"
#      "2 = ")

# Screen choice menu
print("1 = Clear screen on every update (good for tidy information)\n"
    "2 = Rolling data (good for being able to see historical data)")
screenchoice = int(input("Choose behaviour: "))

# Choosing fiat currency
print("1 = USD\n"
      "2 = EUR\n"
      "3 = GBP\n"
      "4 = SEK\n"
      "5 = NOK\n"
      "6 = Manual input option")
fiatchoice = int(input("Choose fiat currency: "))
if fiatchoice == 1:
    fiatcurr = str("USD")
if fiatchoice == 2:
    fiatcurr = str("EUR")
if fiatchoice == 3:
    fiatcurr = str("GBP")
if fiatchoice == 4:
    fiatcurr = str("SEK")
if fiatchoice == 5:
    fiatcurr = str("NOK")
if fiatchoice == 6:
    fiatcurr = str(input("Type a correct international currency abbreviation (USD, EUR, GBP etc) in capital letters: "))

# Static variables
gh = 1000000000
mh = 1000000
kh = 1000
gin = 'Gincoin'

os.system('clear')
# Code to loop
while True :

    # Gets API data for fiat currency and sets pool address
    fiatapi = f"https://free.currencyconverterapi.com/api/v5/convert?q=USD_{fiatcurr}&compact=ultra"
    poolurl = f"{pool}{wallet}"
    # Gets API data for Gincoin
    cryptoapi = "https://api.crypto-bridge.org/api/v1/ticker"
    cryptoresp = requests.get(cryptoapi)
    coindata = cryptoresp.text
    coinparsed = json.loads(coindata)
    for i in coinparsed:
        if i['id'] == 'GIN_BTC':
            cryptoprice = (i)['last']
            cryptofloat = float(cryptoprice)
            break


    nethashresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")

    # Calculations from API data from coin block explorer
    nethash = float(nethashresp.text)
    perchash = round(mining * gh / nethash / 10,5)
    dailycoins = round(dailyprod * perchash / 100, 4)
    # Calculations for fiat currency API data
    fiatresponse = requests.get(fiatapi)
    fiatdata = fiatresponse.text
    fiatparsed = json.loads(fiatdata)
    fiat = fiatparsed[f"USD_{fiatcurr}"]
    # Calculations from API data from Coinmarketcap
    cmcresponse = requests.get("https://api.coinmarketcap.com/v2/ticker/2773")
    data = cmcresponse.text
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
    #Average blocks per day
    dailyblocks = float(round(dailycoins / reward, 4))
    avghours = str(datetime.timedelta(seconds=round(86400 / dailyblocks)))
    # BTC value calculation
    dailycrypto = round(cryptofloat * dailycoins, 8)
    cryptolast24h = round(cryptofloat*last24h,8)
    cryptoph = round(dailycrypto / 24,8)
    cryptolast24hph = round(cryptolast24h / 24,8)
    dailyfiat = round(price * dailycoins * fiat, 2)
    fiatlast24h = round(price * last24h * fiat, 2)
    #Pause to update data
    time.sleep(5)
    if screenchoice == 1:
        os.system('clear')
    # Prints data to screen every 5 minutes
    print("")
    print("|-------------------------------------------|")
    print("|  MagicStats v0.2.2.6.5 by Matz Trollmann  |")
    print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
    print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
    print("|  Github: https://github.com/Trollmann82/  |")
    print("|-------------------------------------------|")
    print("")
    print(today)
    print("You are currently ",poolname," on the address ", wallet,".",sep='')
    print("The current hashrate for",gin,"is",round(nethash / gh,4),"GH/s.")
    print("Your expected hashrate of",mining,"MH/s makes out",perchash,"% of the network.")
    print("Expected daily production is currently ", dailycoins," ",gin," per day, at an estimated value of ",dailyfiat," ",fiatcurr," or ",dailycrypto," Bitcoin. ","(",cryptoph," BTC/h.)",sep='')
    print("Your hashrate will yield an estimated", dailyblocks, "blocks per day, or create a block every", avghours)
    if poolchoice == 1 or poolchoice == 2:
        print("You have mined ",last24h," ",gin," in the last 24 hours for a total value of ",fiatlast24h," ",fiatcurr," or ",cryptolast24h," Bitcoin. ","(",cryptolast24hph," BTC/h.)",sep='')
    time.sleep(295)

