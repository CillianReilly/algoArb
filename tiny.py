import csv
import pandas as pd
from datetime import datetime

import log,algo
from tinyman.v1.client import TinymanMainnetClient

assetIDMap=dict(pd.read_csv("asa.csv")[["asset","tinymanID"]].values)
client=TinymanMainnetClient(user_address=algo.account["address"])

def getAsset(asset):return client.fetch_asset(assetIDMap[asset])
def getPool(trgAsset,srcAsset):return client.fetch_pool(trgAsset,srcAsset)
def getQuote(pool,asset,amount):return pool.fetch_fixed_input_swap_quote(asset(amount),slippage=0.01)

def swap(pool,quote):
	log.out("Converting {:.6f} {} to {:.6f} {} on tinyman".format(
                quote.amount_in.amount/1000000,
		quote.amount_in.asset.name,
                quote.amount_out.amount/1000000,
		quote.amount_out.asset.name
                ))
	transaction_group=pool.prepare_swap_transactions_from_quote(quote)
	transaction_group.sign_with_private_key(algo.account["address"],algo.account["private_key"])
	result=client.submit(transaction_group,wait=True)

	time=datetime.now()
	data=[
		[time,quote.amount_in.asset.unit_name,"S",quote.amount_in.amount/1000000],
		[time,quote.amount_out.asset.unit_name,"B",quote.amount_out.amount/1000000],
		[time,"ALGO","S",0.004]
		]

	with open("arb.csv","a")as f:csv.writer(f).writerows(data)
	return result


def swap_fake(pool,quote):
	log.out("Converting {:.6f} {} to {:.6f} {} on tinyman".format(
		quote.amount_in.amount/1000000,
                quote.amount_in.asset.unit_name,
                quote.amount_out.amount/1000000,
                quote.amount_out.asset.unit_name
		))

	time=datetime.now()
	data=[
		[time,quote.amount_in.asset.unit_name,"S",quote.amount_in.amount/1000000],
		[time,quote.amount_out.asset.unit_name,"B",quote.amount_out.amount/1000000],
		[time,"ALGO","S",0.004]
		]
	with open("arb.csv","a")as f:csv.writer(f).writerows(data)		
