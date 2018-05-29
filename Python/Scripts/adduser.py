#!/usr/bin/env python

## This script is used to creat account of android. You need to enter the account's name group and comment, like this python crearaccount.py zhangsan itgroup shit

import sys
import os

def panduan(str1):
        reader=open('/etc/passwd')
        line=reader.readline()
        while line!='' and line!=None :
                string=line.split(':',1)[0]
                comm=string
                if str1==comm :
                        break
                else :
                        line=reader.readline()
        return line

def creataccount(str1,gn,comment):
        os.system('useradd -d %s/%s -g %s %s -c %s' %(getminhome(),str1,gn,str1,comment))
        os.system('chmod 750 %s/%s' %(getminhome(),str1))
        abcd4(groupname,name)
        pasdd="SPRD#sciuser"
        os.system('echo %s | /usr/bin/passwd --stdin %s' %(pasdd,str1))
        os.system('echo "zlinux2.spreadtrum.com" | /usr/lib64/yp/ypinit -m')
        os.system('service ypserv restart')

def getminhome():
        os.system("df -h | grep home | awk '{print $4}'> data.txt")
        os.system("df -h | grep home | awk '{print $5}'> dhome.txt")

        infp=open('/home5/helena.zheng/python/creatuser/data.txt')
        outfp=open('/home5/helena.zheng/python/creatuser/date.txt','w')
        infp2=open('/home5/helena.zheng/python/creatuser/dhome.txt')
        outfp2=open('/home5/helena.zheng/python/creatuser/dhome2.txt','w')

        lines=infp.readlines()
        lines2=infp2.readlines() 
        for li in lines :
                if li.split() :
                        outfp.write(li)
        outfp.close()
        infp.close()

        for li2 in lines2 :
                if li2.split() :
                        outfp2.write(li2)
        outfp2.close()
        infp2.close()

        da=[]
        f1=open('/home5/helena.zheng/python/creatuser/date.txt')
        li=f1.read().split("\n")
        li.remove('')

        dh=[]
        f2=open('/home5/helena.zheng/python/creatuser/dhome2.txt')
        di=f2.read().split("\n")
        di.remove('')

        min=li[0]
        for i in li :
                if i<min :
                        min=i

#       print min
#       print di[li.index(min)]
        minhom=di[li.index(min)]
        return minhom
def abcd4(groupname,name):
        os.system('echo $(grep %s /etc/netgroup -c)>/home5/helena.zheng/python/creatuser/t.txt' %(groupname))
        tt=open('/home5/helena.zheng/python/creatuser/t.txt').readline()
        ssd='/etc/netgroup'
        f=open('/etc/netgroup','rw')
        ss=f.readline()
        ss1=groupname+str(int(tt))
        ss2=groupname+str(int(tt)-1)
        ss3=groupname
        if 'itgroup'==groupname :
                os.system("sed -i 's/%s/%s (,%s,) /g' %s" %('itgroup1','itgroup1 (,helena.zheng,)',name,ssd))
        else :
                while ss!='' and ss!=None :
                        if ss1==ss.split(' ',1)[0]:
                                os.system("sed -i 's/%s/%s (,%s,) /g' %s" %(ss1,ss1,name,ssd))
                                break
                        elif ss1==ss.split(' ',1)[0]:
                                os.system("sed -i 's/%s/%s (,%s,) /g' %s" %(ss2,ss2,name,ssd))
                                break
                        elif ss3==ss.split(' ',1)[0]:
                                os.system("sed -i 's/%s/%s (,%s,) /g' %s" %(ss3,ss3,name,ssd))
                                break
                        else :

def tongbu(site) :
        os.system('echo %s | /usr/lib64/yp/ypinit -m' %(site))
        os.system('service ypserv restart')
        os.system('ssh -l root  /usr/lib64/yp/ypinit -s zlinux1.spreadtrum.com')
        os.system('ssh -l root zlinux2 service ypserv restart')
        os.system('ssh -l root %s /usr/lib/yp/ypinit -s zlinux1.spreadtrum.com' %(site))
        os.system('ssh -l root %s service ypserv restart' %(site))
 
str1=sys.argv[1]
gn=sys.argv[2]
comment=sys.argv[3]
groupname=sys.argv[2]
name=sys.argv[1]
site=sys.argv[4]

if panduan(str1).split(':',1)[0]==str1 :
        print "The account exist"
else :
        print "Now creat a new account"
        creataccount(str1,gn,comment)
print panduan(str1)
tongbu(site)
