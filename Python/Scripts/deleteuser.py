#!/usr/bin/env python

import sys
import os
import time
import datetime

def panduan(stt1,stt2):
        reader=open('/etc/passwd')
        line=reader.readline()
        while line!='' and line!=None :
                string=line.split(':',1)[0]
                comm=string
                if stt1==comm :
                        aa=stt1
                        break
                elif stt2==comm :
                        aa=stt2
                        break
                else :
                        line=reader.readline()
        return line

stt1=sys.argv[2]
stt2=sys.argv[2].replace('.','')
b=panduan(stt1,stt2)
aa=b.split(':',1)[0]
d=time.strftime('%Y-%m-%d',time.localtime(time.time()))
now=datetime.datetime.now()


if aa==stt1  or aa==stt2 :
        print(aa)
        bb=b.split(':',7)[5].split('/',2)[1]
        os.system('echo /%s/%s:%s:%s:%s >>/home5/helena.zheng/python/lizhi/resignemploynees.txt' %(bb,aa,sys.argv[1],d,now.strftime('%j')))
else :
        print "The account does not exist"
