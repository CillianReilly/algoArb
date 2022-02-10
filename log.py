from datetime import datetime

def message(lvl,msg):
	print(" ### ".join([str(datetime.now()),lvl,msg]))

def createLogger(lvl):
	def logger(msg):return message(lvl,msg)
	return logger

out=createLogger("OUT")
dbg=createLogger("DBG")
err=createLogger("ERR")
