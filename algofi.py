import csv
import pandas as pd
from datetime import datetime

import log,algo
from algofi_amm.v0.asset import Asset
from algofi_amm.v0.client import AlgofiAMMTestnetClient, AlgofiAMMMainnetClient
from algofi_amm.v0.config import PoolType, PoolStatus
from algofi_amm.utils import get_payment_txn, get_params, send_and_wait

assetIDMap=dict(pd.read_csv("asa.csv")[["asset","algofiID"]].values)
client=AlgofiAMMMainnetClient(user_address=algo.account["address"])

def getAsset(asset):return Asset(client,assetIDMap[asset])
def getPool(trgAsset,srcAsset):return client.get_pool(PoolType.CONSTANT_PRODUCT_75BP_FEE,assetIDMap[trgAsset],assetIDMap[srcAsset])
def getPrice(pool,asset):return pool.get_pool_price(assetIDMap[asset])

def swap(pool,srcAmount,srcAsset,trgAmount,trgAsset):
	log.out("Converting {:.6f} {} to {:.6f} {} on algofi".format(
                srcAmount/1000000,
                srcAsset.unit_name,
                trgAmount/1000000,
                trgAsset.unit_name
                ))

	swap_exact_for_txn=pool.get_swap_exact_for_txns(algo.account["address"],srcAsset,srcAmount,int(0.995*trgAmount))
	swap_exact_for_txn.sign_with_private_key(algo.account["address"],algo.account["private_key"])
	result=swap_exact_for_txn.submit(client.algod,wait=True)

	time=datetime.now()
	data=[
		[time,srcAsset.unit_name,"S",srcAmount/1000000],
		[time,trgAsset.unit_name,"B",trgAmount/1000000],
		[time,"ALGO","S",0.004]
		]

	with open("arb.csv","a")as f:csv.writer(f).writerows(data)
	return result


def swap_fake(pool,srcAmount,srcAsset,trgAmount,trgAsset):
	log.out("Converting {:.6f} {} to {:.6f} {} on algofi".format(
		srcAmount/1000000,
		srcAsset.unit_name,
		trgAmount/1000000,
		trgAsset.unit_name
	))

	time=datetime.now()
	data=[
		[time,srcAsset.unit_name,"S",srcAmount/1000000],
		[time,trgAsset.unit_name,"B",trgAmount/1000000],
		[time,"ALGO","S",0.004]
		]

	with open("arb.csv","a")as f:csv.writer(f).writerows(data)
