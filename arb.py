import argparse
import log,tiny,coingecko

def main():
	trg,src=args.trg,args.src
	trgAsset=tiny.getAsset(trg)
	srcAsset=tiny.getAsset(src)
	pool=tiny.getPool(trgAsset,srcAsset)
	swapAmount=tiny.getSwapAmount()
	
	log.out("Starting arb.py")
	USDPrice=coingecko.getQuote(trg,src)
	log.out("{} per {} USD Price: {}".format(trg,src,USDPrice))
	tinyQuote=tiny.getQuote(pool,srcAsset,swapAmount)
	log.out("{} per {} tinyman: {}".format(trg,src,tinyQuote.price))
	
	if tinyQuote.price>USDPrice:
		log.out("Selling {} ALGO for {} YLDY on tinyman".format(swapAmount/1000000,tinyQuote.amount_out.amount/1000000))		
		log.out("Buying {} ALGO for {} YLDY with USD".format((tinyQuote.amount_out.amount/USDPrice)/1000000,tinyQuote.amount_out.amount/1000000))
		log.out("Returns: {0:.5g}%".format(100*((tinyQuote.amount_out.amount/USDPrice)/swapAmount-1)))
	else:
		tinyQuote=tiny.getQuote(pool,trgAsset,USDPrice*swapAmount)
		log.out("Selling {} ALGO for {} YLDY with USD".format(swapAmount/1000000,USDPrice*swapAmount/1000000))
		log.out("Buying {} ALGO for {} YLDY on tinyman".format(tinyQuote.amount_out.amount/1000000,USDPrice*swapAmount/1000000))
		log.out("Returns: {0:.5g}%".format(100*(tinyQuote.amount_out.amount/swapAmount-1)))
	
if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
