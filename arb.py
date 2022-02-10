import argparse
import tiny,coingecko

def main():
	trg,src=args.trg,args.src
	trgAsset=tiny.getAsset(trg)
	srcAsset=tiny.getAsset(src)
	pool=tiny.initPool(trgAsset,srcAsset)
	swapAmount=tiny.getSwapAmount()
	
	USDPrice=coingecko.getQuote(trg,src)
	print("{} per {} USD Price: {}".format(trg,src,USDPrice))
	tinyQuote=tiny.getQuote(pool,srcAsset,swapAmount)
	print("{} per {} tinyman: {}".format(trg,src,tinyQuote.price))
	
	if tinyQuote.price>USDPrice:
		print("Selling {} ALGO for {} YLDY on tinyman".format(swapAmount/1000000,tinyQuote.amount_out.amount/1000000))		
		print("Buying {} ALGO for {} YLDY with USD".format((tinyQuote.amount_out.amount/USDPrice)/1000000,tinyQuote.amount_out.amount/1000000))
		print("Returns: {0:.5g}%".format(100*((tinyQuote.amount_out.amount/USDPrice)/swapAmount-1)))
	else:
		tinyQuote=tiny.getQuote(pool,trgAsset,USDPrice*swapAmount)
		print("Selling {} ALGO for {} YLDY on USD".format(swapAmount/1000000,USDPrice*swapAmount/1000000))
		print("Buying {} ALGO for {} YLDY on tinyman".format(tinyQuote.amount_out.amount/1000000,USDPrice*swapAmount/1000000))
		print("Returns: {0:.5g}%".format(100*(tinyQuote.amount_out.amount/swapAmount-1)))
	
	#print("Returns: ")

if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
