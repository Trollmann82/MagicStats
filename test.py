import requests
import json
import time
import datetime

# User options
mining = float(input("Input your expected hashrate in MH/s: "))

# Static variables
gh = 1000000000
mh = 1000000
kh = 1000
today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
crsreward = 65
crsdailyprod = crsblock24h * crsreward

while True:
    # Gets data for all coins from Cryptobridge
    cbapi = "https://api.crypto-bridge.org/api/v1/ticker"
    cbresp = requests.get(cbapi)
    cbdata = cbresp.text
    cbparsed = json.loads(cbdata)

    # Gets data for defined coins from CREX24 (address have to be changed to add new coins)
    crexapi = "https://api.crex24.com/CryptoExchangeService/BotPublic/ReturnTicker?request=[NamePairs=BTC_ALPS,BTC_CRS]"
    crexresp = requests.get(crexapi)
    crexdata = crexresp.text
    crexparsed = json.loads(crexdata)

    # Gincoin calculations
    ginnethashresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10, 5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
    ginnethashgh = round(ginnethash / gh, 3)
    gin = str("Gincoin")

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
    crsperchash = round(mining * gh / crsnethash / 10, 5)
    crsdailycoins = round(crsdailyprod * crsperchash / 100, 4)
    crsnethashgh = round(crsnethash / gh, 3)
    crs = str("Alpenschilling")

    # Scrapes Cryptobridge data
    for i in cbparsed:
        if i['id'] == 'GIN_BTC':
            ginprice = (i)['last']
            ginfloat = float(ginprice)
            break
    for i in cbparsed:
        if i['id'] == 'IFX_BTC':
            ifxprice = (i)['last']
            ifxfloat = float(ifxprice)
            break

    # Scrapes CREX24 data
    for i in crexparsed['Tickers']:
        if i['PairName'] == "BTC_ALPS":
            alpsprice = (i)['Last']
            alpsfloat = float(alpsprice)
            break
    for i in crexparsed['Tickers']:
        if i['PairName'] == "BTC_CRS":
            crsprice = (i)['Last']
            crsfloat = float(crsprice)
            break

    # Calculates data for list
    dailygin = round(ginfloat * gindailycoins, 8)
    ginph = round(dailygin / 24, 8)
    dailyifx = round(ifxfloat * ifxdailycoins, 8)
    ifxph = round(dailyifx / 24, 8)
    dailyalps = round(alpsfloat * alpsdailycoins, 8)
    alpsph = round(dailyalps / 24, 8)
    dailycrs = round(crsfloat * crsdailycoins, 8)
    crsph = round(dailycrs / 24, 8)

    # Print a list of the coins every 5 minutes
    print(" ",today)
    print("----------------------------------------------------------------------")
    coinlist = [
        ["Coin Name".ljust(20), "Net Hash (GH)".ljust(13), "Coin Price".ljust(12), "Mined/hour".ljust(12)],
        ["Gincoin".ljust(20), "{:.3f}".format(ginnethashgh).ljust(13), str("%.8f" % ginfloat).ljust(12), str("%.8f" % ginph).ljust(12)],
        ["Infinex".ljust(20), str("%.3f" % ifxnethashgh).ljust(13), str("%.8f" % ifxfloat).ljust(12), str("%.8f" % ifxph).ljust(12)],
        ["Alpenschilling".ljust(20), "{:.3f}".format(alpsnethashgh).ljust(13), str("%.8f" % alpsfloat).ljust(12), str("%.8f" % alpsph).ljust(12)],
        ["Criptoreal".ljust(20), "{:.3f}".format(crsnethashgh).ljust(13), str("%.8f" % crsfloat).ljust(12), str("%.8f" % crsph).ljust(12)],
    ]
    for item in coinlist:
        print("|", item[0], "|",
            item[1], "|",
            item[2], "|",
            item[3], "|")
    print("----------------------------------------------------------------------")
    time.sleep(300)
