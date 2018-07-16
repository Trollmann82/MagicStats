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
print("|   MagicStats v0.3.2.2 by Matz Trollmann   |")
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

# Gincoin blockchain data
ginblocktimesec = 120
ginblock24h = 86400 / ginblocktimesec
ginreward = 10
gindailyprod = ginblock24h * ginreward

# Infinex blockchain data
ifxblocktimesec = 90
ifxblock24h = 86400 / ifxblocktimesec
ifxreward = 5
ifxdailyprod = ifxblock24h * ifxreward

# Alpenschilling blockchain data
alpsblocktimesec = 114
alpsblock24h = 86400 / alpsblocktimesec
alpsreward = 65
alpsdailyprod = alpsblock24h * alpsreward

# Criptoreal blockchain data
crsblocktimesec = 114
crsblock24h = 86400 / crsblocktimesec
crsreward = 30
crsdailyprod = crsblock24h * crsreward

# Taler blockchain data
tlrblocktimesec = 300
tlrblock24h = 86400 / tlrblocktimesec
tlrreward = 50
tlrdailyprod = tlrblock24h * tlrreward

# Vertical blockchain data
vtlblocktimesec = 120
vtlblock24h = 86400 / vtlblocktimesec
vtlreward = 24
vtldailyprod = vtlblock24h * vtlreward


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

    # Gets exchange API data for Gincoin
    cbapi = "https://api.crypto-bridge.org/api/v1/ticker"
    cbresp = requests.get(cbapi)
    cbdata = cbresp.text
    cbparsed = json.loads(cbdata)

    for i in cbparsed:
        if i['id'] == 'GIN_BTC':
            cbprice = (i)['last']
            cbfloat = float(cbprice)
            break
    # Gets data for defined coins from CREX24 (address have to be changed to add new coins)
    crexapi = "https://api.crex24.com/CryptoExchangeService/BotPublic/ReturnTicker?request=[NamePairs=BTC_ALPS,BTC_CRS]"
    crexresp = requests.get(crexapi)
    crexdata = crexresp.text
    crexparsed = json.loads(crexdata)

    # Gets Coinstock.me Taler coin data
    csapi = "https://coinstock.me//api/v2/tickers/tlrbtc.json"
    csresp = requests.get(csapi)
    csdata = csresp.text
    csparsed = json.loads(csdata)

    # Gets Graviex coin data
    grvapi = "https://graviex.net//api/v2/tickers.json"
    grvresp = requests.get(grvapi)
    grvdata = grvresp.text
    grvparsed = json.loads(grvdata)

    # Gincoin calculations
    ginnethashresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10, 5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
    ginnethashgh = round(ginnethash / gh, 3)
    gin = str("Gincoin")
    ginbalanceresp = requests.get(f"https://explorer.gincoin.io/ext/getbalance/{wallet}")
    ginbalance = float(ginbalanceresp.text)

    # Infinex Calculations
    ifxnethashresp = requests.get("http://explorer.infinex.info/api/getnetworkhashps")
    ifxnethash = float(ifxnethashresp.text)
    ifxperchash = round(mining * gh / ifxnethash / 10, 5)
    ifxdailycoins = round(ifxdailyprod * ifxperchash / 100, 4)
    ifxnethashgh = round(ifxnethash / gh, 3)
    ifx = str("Infinex")

    # Alpenschilling Calculations
    alpsnethashresp = requests.get("http://explorer.alpenschilling.cash/api/getnetworkhashps")
    alpsnethash = float(alpsnethashresp.text)
    alpsperchash = round(mining * gh / alpsnethash / 10, 5)
    alpsdailycoins = round(alpsdailyprod * alpsperchash / 100, 4)
    alpsnethashgh = round(alpsnethash / gh, 3)
    alps = str("Alpenschilling")

    # Criptoreal Calculations
    crsnethashresp = requests.get("https://criptoreal.info/api/getnetworkhashps")
    crsnethash = float(crsnethashresp.text)
    # ifcrsnethash = crsnethash + (mining * mh)
    crsperchash = round(mining * gh / crsnethash / 10, 5)
    # ifcrsperchash = round(mining * gh / ifcrsnethash / 10,5)
    crsdailycoins = round(crsdailyprod * crsperchash / 100, 4)
    # ifcrsdailycoins = round(crsdailyprod * ifcrsperchash / 100, 4)
    crsnethashgh = round(crsnethash / gh, 3)
    # ifcrsnethashgh = round(ifcrsnethash / gh, 3)
    crs = str("Alpenschilling")

    # Taler Calculations

    #tlrnethashresp = requests.get("http://taler-explorer.online/api/getnetworkhashps")
    #tlrnethash = float(tlrnethashresp.text)
    #tlrperchash = round(mining * gh / tlrnethash / 10, 5)
    #tlrdailycoins = round(tlrdailyprod * tlrperchash / 100, 4)
    #tlrnethashgh = round(tlrnethash / gh, 3)
    #tlr = str("Taler")

    # Vertical Calculations

    vtlnethashresp = requests.get("https://explorer.vertical.ovh/api/getnetworkhashps")
    vtlnethash = float(vtlnethashresp.text)
    vtlperchash = round(mining * gh / vtlnethash / 10, 5)
    vtldailycoins = round(vtldailyprod * vtlperchash / 100, 4)
    vtlnethashgh = round(vtlnethash / gh, 3)
    vtl = str("Vertical")

    # Scrapes Cryptobridge data
    for i in cbparsed:
        if i['id'] == 'GIN_BTC':
            ginprice = (i)['last']
            ginvolumetext = (i)['volume']
            ginvolume = float(ginvolumetext)
            ginfloat = float(ginprice)
            break
    for i in cbparsed:
        if i['id'] == 'IFX_BTC':
            ifxprice = (i)['last']
            ifxvolumetext = (i)['volume']
            ifxvolume = float(ifxvolumetext)
            ifxfloat = float(ifxprice)
            break

    # Scrapes CREX24 data
    for i in crexparsed['Tickers']:
        if i['PairName'] == "BTC_ALPS":
            alpsprice = (i)['Last']
            alpsvolumetext = (i)['BaseVolume']
            alpsvolume = float(alpsvolumetext)
            alpsfloat = float(alpsprice)
            break
    for i in crexparsed['Tickers']:
        if i['PairName'] == "BTC_CRS":
            crsprice = (i)['Last']
            crsvolumetext = (i)['BaseVolume']
            crsvolume = float(crsvolumetext)
            crsfloat = float(crsprice)
            break

    # Scrapes Coinstock.me data
        #for i in csparsed:
            #tlrprice = (i)['last']
            #tlrfloat = float(tlrprice)
            #break
    tlrprice = float(csparsed["ticker"]["last"])
    tlrvolume = float(csparsed["ticker"]["volbtc"])
    vtlprice = float(grvparsed["vtlbtc"]["ticker"]["last"])
    vtlvolume = float(grvparsed["vtlbtc"]["ticker"]["volbtc"])

    # Calculates data for list
    dailygin = round(ginfloat * gindailycoins, 8)
    ginph = round(dailygin / 24, 8)
    dailyifx = round(ifxfloat * ifxdailycoins, 8)
    ifxph = round(dailyifx / 24, 8)
    dailyalps = round(alpsfloat * alpsdailycoins, 8)
    alpsph = round(dailyalps / 24, 8)
    dailycrs = round(crsfloat * crsdailycoins, 8)
    # ifdailycrs = round(crsfloat * ifcrsdailycoins, 8)
    crsph = round(dailycrs / 24, 8)
    # ifcrsph = round(ifdailycrs / 24, 8)
    #dailytlr = round(tlrprice * tlrdailycoins, 8)
    #tlrph = round(dailytlr / 24, 8)
    dailyvtl = round(vtlprice * vtldailycoins, 8)
    vtlph = round(dailyvtl / 24, 8)


    nethashresp = ginnethashresp

    # Calculations from API data from coin block explorer
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10,5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
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
        cryptolast24h = round(cbfloat * last24h, 8)
        cryptolast24hph = round(cryptolast24h / 24, 8)
        fiatlast24h = round(price * last24h * fiat, 2)
    #Average blocks per day
    gindailyblocks = float(round(gindailycoins / ginreward, 4))
    avghours = str(datetime.timedelta(seconds=round(86400 / gindailyblocks)))
    # BTC value calculation
    gindailycrypto = round(cbfloat * gindailycoins, 8)
    cryptoph = round(gindailycrypto / 24,8)
    dailyfiat = round(price * gindailycoins * fiat, 2)

    # Wallet Balance

    ginbtcwalletvalue = ginbalance * ginfloat
    ginfiatwalletvalue = round(price * ginbalance * fiat, 2)
    # Pause to update data
    time.sleep(5)
    if screenchoice == 1:
        os.system('clear')
    # Prints data to screen every 5 minutes
    print("")
    print("|-------------------------------------------|")
    print("|   MagicStats v0.3.2.1 by Matz Trollmann   |")
    print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
    print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
    print("|  Github: https://github.com/Trollmann82/  |")
    print("|-------------------------------------------|")
    print("")
    print(today)
    print("You are currently ",poolname," on the address ", wallet,".",sep='')
    print("The current hashrate for",gin,"is",round(ginnethash / gh,4),"GH/s.")
    print("Your expected hashrate of",mining,"MH/s makes out",ginperchash,"% of the network.")
    print("Expected daily production is currently ", gindailycoins," ",gin," per day, at an estimated value of ",dailyfiat," ",fiatcurr," or ",gindailycrypto," Bitcoin. ","(",cryptoph," BTC/h.)",sep='')
    print("Your hashrate will yield an estimated", gindailyblocks, "blocks per day, or create a block every", avghours)
    if poolchoice == 1 or poolchoice == 2:
        print("You have mined ",last24h," ",gin," in the last 24 hours for a total value of ",fiatlast24h," ",fiatcurr," or ",cryptolast24h," Bitcoin. ","(",cryptolast24hph," BTC/h.)",sep='')
    print("You have", ("%.8f" % ginbalance), gin, "in your wallet at an estimated value of", ("%.8f" % ginbtcwalletvalue), "Bitcoin or", ("%.2f" % ginfiatwalletvalue),fiatcurr,".")
    print("------------------------------------------------------------------------------------------------------")
    coinlist = [
        ["Coin Name".ljust(20), "Net Hash (GH)".ljust(13), "Coin Price".ljust(12), "24h BTC Volume".ljust(14),
         "Coins/day".ljust(12),"BTC/hour".ljust(12),],
        ["Gincoin".ljust(20), "{:.3f}".format(ginnethashgh).ljust(13), str("%.8f" % ginfloat).ljust(12),
         str("%.8f" % ginvolume).ljust(14), str(gindailycoins).ljust(12), str("%.8f" % ginph).ljust(12)],
        ["Infinex".ljust(20), str("%.3f" % ifxnethashgh).ljust(13), str("%.8f" % ifxfloat).ljust(12),
         str("%.8f" % ifxvolume).ljust(14), str(ifxdailycoins).ljust(12), str("%.8f" % ifxph).ljust(12)],
        ["Alpenschilling".ljust(20), "{:.3f}".format(alpsnethashgh).ljust(13), str("%.8f" % alpsfloat).ljust(12),
         str("%.8f" % alpsvolume).ljust(14), str(alpsdailycoins).ljust(12), str("%.8f" % alpsph).ljust(12)],
        ["Criptoreal".ljust(20), "{:.3f}".format(crsnethashgh).ljust(13), str("%.8f" % crsfloat).ljust(12),
         str("%.8f" % crsvolume).ljust(14), str(crsdailycoins).ljust(12), str("%.8f" % crsph).ljust(12)],
        #["Taler".ljust(20), "{:.3f}".format(tlrnethashgh).ljust(13), str("%.8f" % tlrprice).ljust(12),
         #str("%.8f" % tlrvolume).ljust(14), str(tlrdailycoins).ljust(12), str("%.8f" % tlrph).ljust(12)],
        ["Vertical".ljust(20), "{:.3f}".format(vtlnethashgh).ljust(13), str("%.8f" % vtlprice).ljust(12),
         str("%.8f" % vtlvolume).ljust(14), str(vtldailycoins).ljust(12), str("%.8f" % vtlph).ljust(12)],
    ]
    coinlist.sort(key=lambda item: item[5], reverse=True)
    for item in coinlist:
        print("|", item[0], "|",
              item[1], "|",
              item[2], "|",
              item[3], "|",
              item[4], "|",
              item[5], "|",)
    print("------------------------------------------------------------------------------------------------------")
    time.sleep(295)
