#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import subprocess
import time
import hashlib

'''
执行shell命令
'''
def execShell(cmd):
    output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

'''
字符串格式的时间转时间戳

'''
def timestr_to_stamp(time_str, time_format):
    time_array = time.strptime(time_str, time_format)
    time_stamp  = time.mktime(time_array)
    return time_stamp

'''
时间戳转字符串格式时间
'''
def stamp_to_timestr(time_stamp,time_format):
    time_array = time.localtime(time_stamp)
    return time.strftime(time_format, time_array)
'''
获取偏移时间
'''
def get_ago_later_stamp(years=0,months=0,days=0,minutes=0,seconds=0):
    now = datetime.datetime.now()
    # print(now)
    now += datetime.timedelta(days=days)
    now += datetime.timedelta(minutes=minutes)
    now += datetime.timedelta(seconds=seconds)
    time_str = str(now)[:-7]
    # print(time_str)
    time_tuple = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    time_list = list(time_tuple)
    year = int(months/12)
    years += year
    # print(years)
    if(months > 0):
        months %= 12
    else:
        months %= 12*-1

    # print(months)
    time_list[0] += years
    time_list[1] += months
    #return time.strftime('%Y-%m-%d %H:%M:%S',tuple(time_list))
    return time.mktime(tuple(time_list))


'''
计算文件的MD5
'''
def file_md5(filepath):
    m = hashlib.md5()
    f = open(filepath, 'rb')
    while True:
        data = f.read(102400)
        if not data:
            break
        m.update(data)
    f.close()
    return m.hexdigest()
if __name__ == '__main__':
    print(get_ago_later_stamp(years=-29))
    print(timestr_to_stamp('1990-03-27 14:15:18','%Y-%m-%d %H:%M:%S'))


