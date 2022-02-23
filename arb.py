import argparse
import log,algo,tiny,coingecko

def main():
	trg,src=args.trg,args.src
	trgAsset=tiny.getAsset(trg)
	srcAsset=tiny.getAsset(src)
	pool=tiny.getPool(trgAsset,srcAsset)
	swapAmount=getSwapAmount()
	
	log.out("Starting arb.py")
	USDPrice=coingecko.getQuote(trg,src)
	log.out("{} per {} USD Price: {:.6f}".format(trg,src,USDPrice))
	tinyQuote=tiny.getQuote(pool,srcAsset,swapAmount)
	log.out("{} per {} tinyman: {:.6f}".format(trg,src,tinyQuote.price))
	
	if tinyQuote.price>USDPrice:
		tiny.swap_fake(pool,tinyQuote)
		coingecko.swap_fake(tinyQuote.amount_out.amount,trg,tinyQuote.amount_out.amount/USDPrice,src)
		logReturn((tinyQuote.amount_out.amount/USDPrice)/swapAmount)
	else:
		tinyQuote=tiny.getQuote(pool,trgAsset,USDPrice*swapAmount)
		coingecko.swap_fake(swapAmount,src,swapAmount*USDPrice,trg)
		tiny.swap_fake(pool,tinyQuote)
		logReturn(tinyQuote.amount_out.amount/swapAmount)
	
def logReturn(input):
	log.out("Returns: {0:.6f}%".format(100*(input-1)))

def getSwapAmount():
        data=algo.getWalletData(algo.account["address"])
        return algo.getAvailableBalance(data)/2

if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
