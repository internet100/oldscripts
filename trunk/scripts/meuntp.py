#!/usr/bin/python2
import os, sys, urllib, time
def gambiarra_ntp():
	try:
		aa = urllib.urlopen("http://monitor.ntp.br/horacerta/s.php?zone=-3").read().strip().split("#")[1]
		if len(aa) and aa.isdigit():
			aaa = time.gmtime(int(aa[:-3])-time.timezone+time.daylight*3600)
			os.system("date %02i%02i%02i%02i%04i.%02i"%(aaa.tm_mon,aaa.tm_mday,aaa.tm_hour,aaa.tm_min,aaa.tm_year,aaa.tm_sec))
	except:
		time.sleep(60)
		gambiarra_ntp()
time.sleep(60)
gambiarra_ntp()
