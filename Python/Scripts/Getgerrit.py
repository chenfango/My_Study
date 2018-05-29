#!/usr/bin/python
#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com
import requests
import json
import os
import csv
import datetime

def getpage(authurl,user,passwd):
        cookies = dict()
        rsp = requests.get(authurl, auth=(user, passwd))

        for resp in rsp.history:
                if resp.status_code == 302:
                        cookiestr = resp.headers["Set-Cookie"].split(';')[0]
                        name = cookiestr.split('=')[0]
                        value = cookiestr.split('=')[1]
                        cookies[name] = value
        openchanges=url + "changes/"
        page = requests.get(openchanges, cookies=cookies)
        return page.text
def opencsv(filename,list):
        with open(filename,"a+") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(list)
def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

if __name__ =='__main__':
        #Time = time.strftime("%Y-%m-%d", time.localtime()) 
        Time = str(getYesterday())
        url = 'http://review.source.spreadtrum.com/gerrit/'
        authurl=url+"login"
        user="username"
        passwd="passwords"
        result = getpage(authurl,user,passwd).encode('utf-8')
        page1 = result.strip(")]}'")
        os.system('rm -rvf /tmp/a1_%s' %(Time))
        with open('/tmp/a1_'+Time ,'a+') as f:
                f.write(page1)
        os.system("sed -i '/^$/d' /tmp/a1_%s" %(Time))
        page = json.loads(page1)
        filename = "/log/Gerrit/gerrit_"+Time+".csv"
        list_f = ["project","branch","hashtags","change_id","subject","status","created","updated","submit_type","mergeable","insertions","deletions","unresolved_comment_count","_number","owner"]
        opencsv(filename,list_f)
        for i in range(len(page)):
                a1 = page[i]["project"].encode('utf-8')
                a2 = page[i]["branch"].encode('utf-8')
                a3 = page[i]["hashtags"]
                a4 = page[i]["change_id"].encode('utf-8')
                a5 = page[i]["subject"].encode('utf-8')
                a6 = page[i]["status"].encode('utf-8')
                a7 = page[i]["created"].encode('utf-8')
                a8 = page[i]["updated"].encode('utf-8')
                a9 = page[i]["submit_type"].encode('utf-8')
                b1 = page[i]["mergeable"]
                b2 = page[i]["insertions"]
                b3 = page[i]["deletions"]
                b4 = page[i]["unresolved_comment_count"]
                b5 = page[i]["_number"]
                b6 = page[i]["owner"]
                list_f2 = [a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6]
                opencsv(filename,list_f2)
