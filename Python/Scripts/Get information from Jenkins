#!/usr/bin/python
#*encoding=utf-8

import requests
import json
import csv
import time
import os
import sys

## Get build number
def getcontent(url,content1,content2):
        page = requests.get(url)
        inp_dict = json.loads(page.content)
        listN = []
        content = inp_dict[content1]
        for dict in content:
                listN.append(dict[content2])
        return listN



##Get detail imformation of each build number
def getBuildcontent(url):
        page = requests.get(url)
        inp_dict = json.loads(page.content)
        slave = inp_dict["builtOn"]
        Btime = inp_dict['id']
        Time = inp_dict["duration"]
        List = inp_dict['actions']
        result = inp_dict["result"]
        BUILD_LIST = ""
        for n in range(len(List)):
                if "parameters" in List[n].keys():
                        for k in range(len(List[n]["parameters"])):
                                if List[n]["parameters"][k]['name'] == 'BUILD_LIST':
                                        BUILD_LIST = List[n]["parameters"][k]['value']
                                else :
                                        pass
                else :
                                        pass
        return result,Time,Btime,BUILD_LIST,slave

def writedatacsv(filename,a1,a2,a3,a4,a5,a6,a7):
        with open(filename,"a+") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([a1, a2, a3, a4, a5, a6, a7])

if __name__ =='__main__':

        TT = time.strftime("%Y-%m-%d", time.localtime())
        url_0 = "http://10.0.1.99:8080/jenkins/"
        url_1 = "api/json?pretty=true"
        url = url_0+url_1
        Job = getcontent(url,'jobs','name')
        filename = "/log/Jenkins/jenkins_"+TT+".csv"
        os.system('rm -rvf %s' %(filename))
        writedatacsv(filename,'Job','Build_number','result','Time','Btime','BUILD_LIST','slave')
        for j in range(len(Job)):
                url_job = url_0+"job/"+Job[j]+"/"+url_1
                BuildN = getcontent(url_job,"builds","number")
                for i in range(len(BuildN)):
                        url_build = url_0+"job/"+Job[j]+"/"+str(BuildN[i])+"/"+url_1
                        a1 = Job[j]
                        a2 = BuildN[i]
                        a3 = getBuildcontent(url_build)[0]
                        a4 = getBuildcontent(url_build)[1]/(1000*60)
                        a5 = getBuildcontent(url_build)[2]
                        a6 = getBuildcontent(url_build)[3]
                        a7 = getBuildcontent(url_build)[4]
                        writedatacsv(filename,a1,a2,a3,a4,a5,a6,a7)
