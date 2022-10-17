from requests import Session
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
import os
import requests
import json
import xlsxwriter

# Load Configs (acess env vars with os.getenv())
load_dotenv(override=True)

# Supplemental Functions for Generating Resource URLs
def getIcoUrl (coinId):
    return os.getenv('CMC_COIN_ICO_BASE_URL') + str(coinId) + ".png"

def getCoinInfoUrl (coinSlug):
    return os.getenv('CMC_COIN_INFO_BASE_URL') + str(coinSlug) + "/"

# CoinMarketCap API Handler
reqUrl = os.getenv('API_BASE_URL') + os.getenv('API_PATH_CRYPTO_LIST_LATEST')
reqHead = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('API_KEY')
}
reqParam = {
    'start':'1',
    'limit':'200',
    'convert':'USD',
    'sort': 'market_cap'
}

session = Session()
session.headers.update(reqHead)
response = session.get(reqUrl, params=reqParam)

## Receive Response
data = json.loads(response.text)

## Extract Data
coinData = data["data"]

## Extract Timestamp (yyyy-mm-dd)
coinStatus = data["status"]
coinTimestamp = ((coinStatus["timestamp"]).split("T"))[0]


## Process Data Into Multidimentional Array
coinArray = []

for coin in coinData:
    coinStr = [coin["name"],coin["symbol"],getIcoUrl(coin["id"]),getCoinInfoUrl(coin["slug"])]
    coinArray.append(coinStr)

# XLSX Writer
workbook = xlsxwriter.Workbook(('cmc_report_'+coinTimestamp+".xlsx"))
worksheet = workbook.add_worksheet(name=coinTimestamp)
worksheet.set_default_row(50)

## Write Coin Array to XLSX
for row, coins in enumerate(coinArray, start=0):
    for col, coin in enumerate(coins,start=0):
        if (col == 2):
            ### Images are resized to 50px by 50px
            imageObj = Image.open(BytesIO(requests.get(coin).content))
            imageObjResized = imageObj.resize((50,50))
            imageData = BytesIO()
            imageObjResized.save(imageData, format="PNG", optimize=True)
            worksheet.insert_image(row,col,coin,{'image_data': imageData})
        else:
            worksheet.write(row,col,coin)

workbook.close()


