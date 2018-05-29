#!/usr/bin/env python

import sys
import os

def panduan(stt1,stt2):
        reader=open('/etc/passwd')
        line=reader.readline()
        while line!='' and line!=None :
                string=line.split(':',1)[0]
                comm=string
                if stt1==comm :
                        a1=stt1
                        break
                elif stt2==comm :
                        a1=stt2
                        break
                else :
                        line=reader.readline()
        return a1
def chpasswd(aa,site):
        pasdd="SPRD#sciuser"
        os.system('echo %s | /usr/bin/passwd --stdin %s' %(pasdd,aa))
        os.system('echo zlinux2 | /usr/lib64/yp/ypinit -m')
        os.system('service ypserv restart')

def tongbu(site,aa) :
        os.system('echo %s | /usr/lib64/yp/ypinit -m' %(site))
        os.system('service ypserv restart')
        os.system('ssh -l root  /usr/lib64/yp/ypinit -s zlinux1.spreadtrum.com')
        os.system('ssh -l root zlinux2 service ypserv restart')
        os.system('ssh -l root %s /usr/lib/yp/ypinit -s zlinux1.spreadtrum.com' %(site))
        os.system('ssh -l root %s service ypserv restart' %(site))

stt1=sys.argv[1]
stt2=sys.argv[1].replace('.','')
site=sys.argv[2]
aa=panduan(stt1,stt2)

print "Please input username and sitename"
if aa==stt1 or aa==stt2 :
        chpasswd(aa,site)
        tongbu(site,aa)
else :
        print "The account does not exist"

print panduan(stt1,stt2)
