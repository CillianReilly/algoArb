import argparse
import log,algo,tiny,algofi

def main():
	trg,src=args.trg,args.src
	
	tinyTrgAsset=tiny.getAsset(trg)
	tinySrcAsset=tiny.getAsset(src)
	tinyPool=tiny.getPool(tinyTrgAsset,tinySrcAsset)
	
	algofiTrgAsset=algofi.getAsset(trg)
	algofiSrcAsset=algofi.getAsset(src)	
	algofiPool=algofi.getPool(trg,src)

	log.out("Starting arb.py")
	swapAmount=getSwapAmount()

	tinyQuote=tiny.getQuote(tinyPool,tinySrcAsset,swapAmount)
	log.out("{} per {} tinyman: {:.6f}".format(trg,src,tinyQuote.price))

	algofiPrice=algofi.getPrice(algofiPool,trg)
	log.out("{} per {} algofi: {:.6f}".format(trg,src,algofiPrice))

	if tinyQuote.price>algofiPrice:
		testReturn(swapAmount,tinyQuote.amount_out.amount/algofiPrice)
		tiny.swap_fake(tinyPool,tinyQuote)
		algofi.swap_fake(algofiPool,tinyQuote.amount_out.amount,algofiTrgAsset,tinyQuote.amount_out.amount/algofiPrice,algofiSrcAsset)
	else:
		tinyQuote=tiny.getQuote(tinyPool,tinyTrgAsset,algofiPrice*swapAmount)
		testReturn(swapAmount,tinyQuote.amount_out.amount)
		algofi.swap_fake(algofiPool,swapAmount,algofiSrcAsset,swapAmount*algofiPrice,algofiTrgAsset)
		tiny.swap_fake(tinyPool,tinyQuote)
	
def testReturn(initial,returns):
	r=(returns/initial)-1
	log.out("Potential percentage return: {0:.6f}%".format(100*r))
	log.out("Potential ALGO return: {0:.6f}".format((initial*r)/1000000))
	# Fee of 0.004 ALGO per swap per pool
	if not initial*r>8000:
		log.out("Potential returns do not exceed fees")
		exit(0)

def getSwapAmount():
        data=algo.getWalletData(algo.account["address"])
        return algo.getAvailableBalance(data)/2
	
if __name__=="__main__":
	p=argparse.ArgumentParser()
	p.add_argument("trg",help="target")
	p.add_argument("src",help="source")
	args=p.parse_args()

	main()
