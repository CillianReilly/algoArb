import requests
import log

IDMap={"ALGO":"algorand","YLDY":"yieldly"}
endpoint="https://api.coingecko.com/api/v3/simple/price"

def getPrice(symbols):
	ids=",".join([IDMap[i]for i in symbols])
	r=requests.get(endpoint+"?ids="+ids+"&vs_currencies=USD")
	prices=[r.json()[i]["usd"]for i in ids.split(",")]
	return dict(zip(symbols,prices))

def getQuote(trg,src):
	price=getPrice([trg,src])
	return price[src]/price[trg]

def swap_fake(trgAmount,trgAsset,srcAmount,srcAsset):
	log.out("Converting {} {} to {} {} on coingecko".format(
		trgAmount/1000000,
		trgAsset,
		srcAmount/1000000,
		srcAsset
		))	
