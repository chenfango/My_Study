#!/usr/bin/python
#encoding=utf-8

import jenkins
import sys
import os
import time


if __name__ =='__main__':

    # Connect the Jenkins API by username and API password
    username  = 'uername'
    password  = 'passwords'
    # Get the Jenkins Server
    jenkins_server_url = r'http://10.0.1.99:8080/jenkins/'
    try:
        server   = jenkins.Jenkins(jenkins_server_url, username, password)
    except:
        print 'Can not connect to the jenkins server'
        print str(sys.exc_info())

    try:
        f = open('/log/Jenkins/queue_sh.csv','a+')
        cur_time   = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        queue_info = server.get_queue_info()
        queue_num  = len(queue_info)
        print cur_time, ':', 'queue_job_num=', queue_num
        f.write('%s:queue_job_num=%s \n' %(cur_time,queue_num))
        f.close()
        os.system('echo %s":queue_job_num="%s >> /log/Jenkins/queue_sh.csv' %(cur_time,queue_num))
    except:
        print sys.exc_info()
~                            
