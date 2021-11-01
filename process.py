import ricartagrawala as ra
import argparse
import time

APP_NAME = "Ra_Test"

def initLogger():
        formatter = logging.Formatter('%(asctime)s %(levelname)s::%(message)s')
        hdlrStd = logging.StreamHandler()
        hdlrStd.setFormatter(formatter)
        logger.addHandler(hdlrStd) 
        logger.setLevel(logging.DEBUG)

def parseArgs():
        parser = argparse.ArgumentParser(prog=APP_NAME, usage='%(prog)s [options]')
        parser.add_argument('--firstprocess_addr','-r', type=str, required = False, default = '127.0.0.1', help='firstprocess address')
        parser.add_argument('--firstprocess_port','-i', type=int, default = None, help='firstprocess port')
        parser.add_argument('--cs_time','-u',type=int,required	= True, help="critical section time [ unit - seconds ]")
        parser.add_argument('--wait_time','-w',type=int,required = True, help="Idle time")
        parser.add_argument('--name','-n',type=str,required =True, help="Unique Node Name")
        parser.add_argument('--addr','-a',type=str,required =False, default = '', help="node address")
        parser.add_argument('--port','-p',type=int,required =False, default = 0, help="node port")
        return parser.parse_args()
 
class RaTest(object):
	def __init__(self,args):
		self.use_time = args.cs_time
		self.wait_time = args.wait_time
		self.name = args.name
		self.sponsor = (args.firstprocess_addr, args.firstprocess_port)
		self.addr = args.addr
		self.port = args.port

	def runTest(self): 
		test = ra.RA(self.name,self.addr,self.port)
		if (self.sponsor[0] != None ) and (self.sponsor[1] !=None):
			print "PROCESS::" + self.name + "::INITIALIZATTION"
			test.init(self.sponsor)

		print "PROCESS::" + self.name + "::READY"
		while(True):
			print "PROCESS::" + self.name + "::IDLE"
			time.sleep(self.wait_time)
			print "PROCESS::" + self.name + "::ACQUIRING_RESOURCE [ CRITICAL SECTION] "
			test.acquire()
                        print "PROCESS:: DATA STRUCTURE INFO @PROCESS::"+self.name
                        print "CURRENT SEQUENCE NUMBER::"+str(test.highest_seq_num)
                        print "CURRENT REPLY COUNT - OUTSTANDING::"+str(test.oustanding_reply_count)
                        print "DEFFERED::"
                        print test.reply_deffered
                        print "AWAITING REPLY::"
                        print test.awaiting_reply

			print "PROCESS::" + self.name + "::USING_RESOURCE [ IN CRITICAL SECTION ]"
			time.sleep(self.use_time)
			print "PROCESS::" + self.name + "::USING_DONE [ CRITICAL SECTION COMPLETED ]"		
			print "PROCESS::" + self.name + "::RELEASING_RESOURCE [ RELEASSING FROM CRITICAL SECTION]"
			test.release()


if __name__ == "__main__":
	test = RaTest(parseArgs())
	test.runTest()
