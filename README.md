## AlgoArb
A project to highlight arbitrage opportunities on decentralised exchanges (DEXes) built on the [Algorand](https://www.algorand.com) network.

Also a chance for me to get some experience interacting with blockchain technologies.

As of now, [tinyman](https://tinyman.org) is the only DEX on Algorand, so currently I just compare ALGO and YLDY to their USD price, obtained from [CoinGecko](https://www.coingecko.com).
```
algoArb $ python3 arb.py YLDY ALGO
2022-02-10 10:26:42.978515 ### OUT ### Starting arb.py
2022-02-10 10:26:44.094388 ### OUT ### YLDY per ALGO USD Price: 91.00295759612189
2022-02-10 10:26:44.411497 ### OUT ### YLDY per ALGO tinyman: 96.02251435743237
2022-02-10 10:26:44.412036 ### OUT ### Selling 9.435357 ALGO for 906.006703 YLDY on tinyman
2022-02-10 10:26:44.412392 ### OUT ### Buying 9.955794041562115 ALGO for 906.006703 YLDY with USD
2022-02-10 10:26:44.412717 ### OUT ### Returns: 5.5158%
```
