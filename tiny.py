from tinyman.v1.client import TinymanMainnetClient

assetIDMap={"ALGO":0,"YLDY":226701642}
client=TinymanMainnetClient()

def initPool(trg,src):
        trg=client.fetch_asset(assetIDMap[trg])
        src=client.fetch_asset(assetIDMap[src])
        pool=client.fetch_pool(trg,src)
        return [pool,src]

def getQuote(pool,src):
        quote=pool.fetch_fixed_input_swap_quote(src(1000000),slippage=0.01)
        return quote.price
