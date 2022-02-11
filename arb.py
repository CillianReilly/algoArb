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
		tiny.swap_fake(tinyQuote)
		coingecko.swap_fake(tinyQuote.amount_out.amount,"Yieldy",tinyQuote.amount_out.amount/USDPrice,"Algo")
		log.out("Returns: {0:.5g}%".format(100*((tinyQuote.amount_out.amount/USDPrice)/swapAmount-1)))
	else:
		tinyQuote=tiny.getQuote(pool,trgAsset,USDPrice*swapAmount)
		coingecko.swap_fake(swapAmount,"Algo",swapAmount*USDPrice,"Yieldly")
		tiny.swap_fake(tinyQuote)
		log.out("Returns: {0:.5g}%".format(100*(tinyQuote.amount_out.amount/swapAmount-1)))
	
if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
