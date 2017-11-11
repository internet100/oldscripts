#!/usr/bin/python2
import os, sys, urllib, time
def gambiarra_ntp():
	bb = time.time()
	aa = urllib.urlopen("http://monitor.ntp.br/horacerta/s.php?zone=-3").read().strip().split("#")[1]
	bb = (time.time()-bb)/2
	if len(aa) and aa.isdigit():
		aaa = time.gmtime(int(aa[:-3])-time.timezone+time.daylight*3600+int(bb))
		os.system("date %02i%02i%02i%02i%04i.%02i"%(aaa.tm_mon,aaa.tm_mday,aaa.tm_hour,aaa.tm_min,aaa.tm_year,aaa.tm_sec))
gambiarra_ntp()
