#!/usr/bin/python3
#coding=utf-8
import re
#import xlwt
import time
import numpy as np
action_dict={}
action_list=[]
def action_average():
        average_list=[]
        for (k,v) in action_dict.items():
                action_start=v[::2]
                action_finish=v[1::2]
                s = np.array(action_finish)-np.array(action_start)
                L = [k,np.mean(s),len(v)/2]
                average_list.append(L)
        #print average_list
        return average_list
with open('case_log.txt','r') as f:
        for line in f.readlines():
            str = re.search(r'(\d{1,2}/\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}),(\d+)\s:\sACTION\s(\w+)\s.*',line)
            if str:
                #make str to time stamp
                action_time="2018/"+str.group(1)
                time_stamp=time.mktime(time.strptime(action_time,'%Y/%m/%d %H:%M:%S'))
                action_microsec=str.group(2)
                time_stamp= float(action_microsec)/1000000+time_stamp
                action_type=str.group(3)
                #action_list=[time_stamp,action_type]
                if action_type not in action_dict.keys():
                                action_dict[action_type]=[]
                action_dict[action_type].append(time_stamp)
        #print action_dict
        action_average_list = action_average()
        #sorted as count
        L=sorted(action_average_list,key=lambda y:y[2])
        print L
