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
print("|    MagicStats v0.5.2 by Matz Trollmann    |")
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

# MCT+ blockchain data
mctblocktimesec = 60
mctblock24h = 86400 / mctblocktimesec
mctreward = 25
mctdailyprod = mctblock24h * mctreward

# Manocoin blockchain data
manoblocktimesec = 120
manoblock24h = 86400 / manoblocktimesec
manoreward = 5
manodailyprod = manoblock24h * manoreward

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
print("1 = Respawn\n"
    "2 = Angrypool\n"
    "3 = Bsod\n"
    "4 = solo mining")
poolchoice = int(input("Choose pool: "))
if poolchoice == 1:
    pool = f"https://pool.respawn.rocks/api/walletEx?address="
    poolname = str("mining on Respawn Rocks")
if poolchoice == 2:
    pool = f"http://angrypool.com/api/walletEx?address="
    poolname = str("mining on Angrypool")
if poolchoice == 3:
    pool = f"http://api.bsod.pw/api/walletEx?address="
    poolname = str("mining on Bsod")
if poolchoice == 4:
    pool = str("")
    poolname = str("solo mining")

# Coin choice menu
print("1 = Gincoin\n"
      "2 = Manocoin")
coinchoice = int(input("Choose coin: "))
if coinchoice == 1:
    coinname = "Gincoin"
if coinchoice == 2:
    coinname = "Manocoin"


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
            cbginprice = (i)['last']
            cbginfloat = float(cbginprice)
            break

    for i in cbparsed:
        if i['id'] == 'MANO_BTC':
            cbmanoprice = (i)['last']
            cbmanofloat = float(cbmanoprice)
            break

    for i in cbparsed:
        if i['id'] == 'MCT_BTC':
            cbmctprice = (i)['last']
            cbmctfloat = float(cbmctprice)
            break

    # Gincoin calculations
    ginnethashresp = requests.get("https://explorer.gincoin.io/api/getnetworkhashps")
    ginnethash = float(ginnethashresp.text)
    ginperchash = round(mining * gh / ginnethash / 10, 5)
    gindailycoins = round(gindailyprod * ginperchash / 100, 4)
    ginnethashgh = round(ginnethash / gh, 3)
    if coinchoice == 1:
        ginbalanceresp = requests.get(f"https://explorer.gincoin.io/ext/getbalance/{wallet}")
        coinbalance = float(ginbalanceresp.text)

    # Manocoin Calculations
    manonethashresp = requests.get("http://explorer.manocoin.org/api/getnetworkhashps")
    manonethash = float(manonethashresp.text)
    manoperchash = round(mining * gh / manonethash / 10, 5)
    manodailycoins = round(manodailyprod * manoperchash / 100, 4)
    manonethashgh = round(manonethash / gh, 3)
    mano = str("Manocoin")
    if coinchoice == 2:
        manobalanceresp = requests.get(f"https://explorer.manocoin.org/ext/getbalance/{wallet}")
        coinbalance = float(manobalanceresp.text)

    # Infinex Calculations
    ifxnethashresp = requests.get("http://explorer.infinex.info/api/getnetworkhashps")
    ifxnethash = float(ifxnethashresp.text)
    ifxperchash = round(mining * gh / ifxnethash / 10, 5)
    ifxdailycoins = round(ifxdailyprod * ifxperchash / 100, 4)
    ifxnethashgh = round(ifxnethash / gh, 3)
    ifx = str("Infinex")

    # MCT+ Calculations
    mctnethashresp = requests.get("http://explorer.mct.plus/api/getnetworkhashps")
    mctnethash = float(mctnethashresp.text)
    mctperchash = round(mining * gh / mctnethash / 10, 5)
    mctdailycoins = round(mctdailyprod * mctperchash / 100, 4)
    mctnethashgh = round(mctnethash / gh, 3)
    mct = str("MCT+")

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
    for i in cbparsed:
        if i['id'] == 'MANO_BTC':
            manoprice = (i)['last']
            manovolumetext = (i)['volume']
            manovolume = float(manovolumetext)
            manofloat = float(manoprice)
            break
    for i in cbparsed:
        if i['id'] == 'MCT_BTC':
            mctprice = (i)['last']
            mctvolumetext = (i)['volume']
            mctvolume = float(mctvolumetext)
            mctfloat = float(mctprice)
            break

    # Calculates data for list
    dailygin = round(ginfloat * gindailycoins, 8)
    ginph = round(dailygin / 24, 8)
    dailyifx = round(ifxfloat * ifxdailycoins, 8)
    ifxph = round(dailyifx / 24, 8)
    dailymano = round(manofloat * manodailycoins, 8)
    manoph = round(dailymano / 24, 8)
    dailymct = round(mctfloat * mctdailycoins, 8)
    mctph = round(dailymct / 24, 8)

    if coinchoice == 1:
        coinnethashresp = ginnethashresp
        coinperchash = ginperchash
        coinnethash = ginnethash
        coindailycoins = gindailycoins
        coindailyprod = gindailyprod
        coinreward = ginreward
        cbcoinfloat = cbginfloat
    if coinchoice == 2:
        coinnethashresp = manonethashresp
        coinperchash = manoperchash
        coinnethash = manonethash
        coindailycoins = manodailycoins
        coindailyprod = manodailyprod
        coinreward = manoreward
        cbcoinfloat = cbmanofloat

    # Calculations from API data from coin block explorer
    coinnethash = float(coinnethashresp.text)
    coinperchash = round(mining * gh / coinnethash / 10,5)
    coindailycoins = round(coindailyprod * coinperchash / 100, 4)
    # Calculations for fiat currency API data
    fiatresponse = requests.get(fiatapi)
    fiatdata = fiatresponse.text
    fiatparsed = json.loads(fiatdata)
    fiat = fiatparsed[f"USD_{fiatcurr}"]

    # Calculations from API data from Coinmarketcap
    if coinchoice == 1:
        cmcresponse = requests.get("https://api.coinmarketcap.com/v2/ticker/2773")
        data = cmcresponse.text
        parsed = json.loads(data)
        price = parsed["data"]["quotes"]["USD"]["price"]

    if coinchoice == 2:
        cmcresponse = requests.get("https://api.coinmarketcap.com/v2/ticker/1")
        data = cmcresponse.text
        parsed = json.loads(data)
        btcprice = parsed["data"]["quotes"]["USD"]["price"]
        price = btcprice * manofloat
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # API data from pool
    if poolchoice == 1 or poolchoice == 2 or poolchoice == 3:
        poolresponse = requests.get(poolurl)
        data = poolresponse.text
        parsed = json.loads(data)
        total24htext = parsed['total']
        last24h = round(total24htext,4)
        if coinchoice == 1:
            cryptolast24h = round(cbginfloat * last24h, 8)
        if coinchoice == 2:
            cryptolast24h = round(cbmanofloat * last24h, 8)
        cryptolast24hph = round(cryptolast24h / 24, 8)
        fiatlast24h = round(price * last24h * fiat, 2)
    #Average blocks per day
    coindailyblocks = float(round(coindailycoins / coinreward, 4))
    avghours = str(datetime.timedelta(seconds=round(86400 / coindailyblocks)))
    # BTC value calculation
    dailycrypto = round(cbcoinfloat * coindailycoins, 8)
    cryptoph = round(dailycrypto / 24,8)
    dailyfiat = round(price * coindailycoins * fiat, 2)

    # Wallet Balance
    if coinchoice == 1:
        coinbtcwalletvalue = coinbalance * ginfloat
        coinfiatwalletvalue = round(price * coinbalance * fiat, 2)
    if coinchoice == 2:
        coinbtcwalletvalue = coinbalance * manofloat
        coinfiatwalletvalue = round(price * coinbalance * fiat, 2)
    # Pause to update data
    time.sleep(5)
    if screenchoice == 1:
        os.system('clear')
    # Prints data to screen every 5 minutes
    print("")
    print("|-------------------------------------------|")
    print("|    MagicStats v0.5.2 by Matz Trollmann    |")
    print("|  BTC: 3PBN9BHxFyjWoXBT1HH4YPDV5UcYBq9YsS  |")
    print("|  GIN: GgpRYX7NchKczJQs4CdE1yKhRSv9U8rL29  |")
    print("|  Github: https://github.com/Trollmann82/  |")
    print("|-------------------------------------------|")
    print("")
    print(today)
    print("You are currently ",poolname," on the address ", wallet,".",sep='')
    print("The current hashrate for",coinname,"is",round(coinnethash / gh,4),"GH/s.")
    print("Your expected hashrate of",mining,"MH/s makes out",coinperchash,"% of the network.")
    print("Expected daily production is currently ", coindailycoins," ",coinname," per day, at an estimated value of ",dailyfiat," ",fiatcurr," or ",dailycrypto," Bitcoin. ","(",cryptoph," BTC/h.)",sep='')
    print("Your hashrate will yield an estimated", coindailyblocks, "blocks per day, or create a block every", avghours)
    if poolchoice == 1 or poolchoice == 2:
        print("You have mined ",last24h," ",coinname," in the last 24 hours for a total value of ",fiatlast24h," ",fiatcurr," or ",cryptolast24h," Bitcoin. ","(",cryptolast24hph," BTC/h.)",sep='')
    print("You have", ("%.8f" % coinbalance), coinname, "in your wallet at an estimated value of", ("%.8f" % coinbtcwalletvalue), "Bitcoin or", ("%.2f" % coinfiatwalletvalue),fiatcurr,".")
    print("------------------------------------------------------------------------------------------------------")
    coinlist = [
        ["Coin Name".ljust(20), "Net Hash (GH)".ljust(13), "Coin Price".ljust(12), "24h BTC Volume".ljust(14),
         "Coins/day".ljust(12),"BTC/hour".ljust(12),],
        ["Gincoin".ljust(20), "{:.3f}".format(ginnethashgh).ljust(13), str("%.8f" % ginfloat).ljust(12),
         str("%.8f" % ginvolume).ljust(14), str(gindailycoins).ljust(12), str("%.8f" % ginph).ljust(12)],
        ["Infinex".ljust(20), str("%.3f" % ifxnethashgh).ljust(13), str("%.8f" % ifxfloat).ljust(12),
         str("%.8f" % ifxvolume).ljust(14), str(ifxdailycoins).ljust(12), str("%.8f" % ifxph).ljust(12)],
  #      ["Alpenschilling".ljust(20), "{:.3f}".format(alpsnethashgh).ljust(13), str("%.8f" % alpsfloat).ljust(12),
   #      str("%.8f" % alpsvolume).ljust(14), str(alpsdailycoins).ljust(12), str("%.8f" % alpsph).ljust(12)],
        #["Criptoreal".ljust(20), "{:.3f}".format(crsnethashgh).ljust(13), str("%.8f" % crsfloat).ljust(12),
         #str("%.8f" % crsvolume).ljust(14), str(crsdailycoins).ljust(12), str("%.8f" % crsph).ljust(12)],
        #["Taler".ljust(20), "{:.3f}".format(tlrnethashgh).ljust(13), str("%.8f" % tlrprice).ljust(12),
         #str("%.8f" % tlrvolume).ljust(14), str(tlrdailycoins).ljust(12), str("%.8f" % tlrph).ljust(12)],
   #     ["Vertical".ljust(20), "{:.3f}".format(vtlnethashgh).ljust(13), str("%.8f" % vtlprice).ljust(12),
    #     str("%.8f" % vtlvolume).ljust(14), str(vtldailycoins).ljust(12), str("%.8f" % vtlph).ljust(12)],
        ["Manocoin".ljust(20), "{:.3f}".format(manonethashgh).ljust(13), str("%.8f" % manofloat).ljust(12),
         str("%.8f" % manovolume).ljust(14), str(manodailycoins).ljust(12), str("%.8f" % manoph).ljust(12)],
        ["MCT+".ljust(20), "{:.3f}".format(mctnethashgh).ljust(13), str("%.8f" % mctfloat).ljust(12),
         str("%.8f" % mctvolume).ljust(14), str(mctdailycoins).ljust(12), str("%.8f" % mctph).ljust(12)],
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
