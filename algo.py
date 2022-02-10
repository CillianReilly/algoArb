import requests
from cfg import account

assetIDMap={"ALGO":0,"YLDY":226701642}

## Run a node and query the chain from there
endpoint="https://algoindexer.algoexplorerapi.io/v2"

def getWalletData(address):
	r=requests.get(endpoint+"/accounts/"+address)
	return r.json()["account"]

# Minimum algo balance is 0.1+0.1*number of assets
def getMinBalance(data):return 1000000*(0.1+0.1*len(data["assets"]))
def getAvailableBalance(data):return getALGOBalance(data)-getMinBalance(data)

def getALGOBalance(data):return data["amount-without-pending-rewards"]
def getAssetBalance(data,asset):
	assetID=assetIDMap[asset]
	asset=[i for i in data["assets"]if i["asset-id"]==assetID][0]
	return asset["amount"]

data=getWalletData(account["address"])
