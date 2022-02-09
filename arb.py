import argparse
import tiny,coingecko

def main():
	trg,src=args.trg,args.src
	trgAsset=tiny.getAsset(trg)
	srcAsset=tiny.getAsset(src)
	pool=tiny.initPool(trgAsset,srcAsset)

	USDPrice=coingecko.getQuote(trg,src)
	print("{} per {} USD Price: {}".format(trg,src,USDPrice))
	tinyQuote=tiny.getQuote(pool,srcAsset,1000000)
	print("{} per {} tinyman: {}".format(trg,src,tinyQuote.price))

	if tinyQuote.price<USDPrice:
		print("Buy {trg} on USD with {src}, sell {trg} on tinyman for {src}. Returns: {0:.5g}%".format(100*(USDPrice/tinyQuote.price-1),trg=trg,src=src))
	else:
		print("Buy {trg} on tinyman with {src}, sell {trg} on USD for {src}. Returns: {0:.5g}%".format(100*(tinyQuote.price/USDPrice-1),trg=trg,src=src))


if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
