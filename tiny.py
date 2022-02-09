from tinyman.v1.client import TinymanMainnetClient
from cfg import account

assetIDMap={"ALGO":0,"YLDY":226701642}
client=TinymanMainnetClient(user_address=account["address"])

def getAsset(asset):return client.fetch_asset(assetIDMap[asset])
def initPool(trgAsset,srcAsset):return client.fetch_pool(trgAsset,srcAsset)
def getQuote(pool,asset,amount):return pool.fetch_fixed_input_swap_quote(asset(amount),slippage=0.01)

def swap(quote):
	transaction_group=pool.prepare_swap_transactions_from_quote(quote)
	transaction_group.sign_with_private_key(account["address"],account["private_key"])
	result=client.submit(transaction_group,wait=True)
