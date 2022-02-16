import csv,requests
from datetime import datetime

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

def swap_fake(srcAmount,srcAsset,trgAmount,trgAsset):
	log.out("Converting {:.6f} {} to {:.6f} {} on coingecko".format(
		srcAmount/1000000,
		srcAsset,
		trgAmount/1000000,
		trgAsset
		))

	time=datetime.now()
	data=[
		[time,srcAsset,"S",srcAmount/1000000],
		[time,trgAsset,"B",trgAmount/1000000],
		[time,"ALGO","S",0]
		]
	with open("arb.csv","a")as f:csv.writer(f).writerows(data)
