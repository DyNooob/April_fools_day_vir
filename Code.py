import os
import time
import threading
import jsonpath
import requests
import win32api
import win32con
import psutil


status = ''
prog_list = []
title = ''
get_message = ''
POWERPNT_status = ''
POWERPNT_message = ''
Seewo_status = ''
Seewo_message = ''

'''Date time settings'''
# ----- please input like "01" "04"
plan_month = "03"
plan_day = "27"
plan_minutes = "20"
plan_hours = "21"
# ----- 2021-3-27 21:08:59 --------

name_dictionary = {
    "EasiNote.exe": "希沃白版5",
    "SeewoLink": "希沃授课助手",
    "WeChat.exe": "微信",
    "DingTalk.exe": "钉钉",
    "POWERPNT.EXE": "PowerPoint(PPT)"
}



'''Kill func'''
def end_program(pro_name):
    try:
        os.sys.kill('%s%s' % ("taskkill /F /IM ", pro_name))
    except:
        pass


'''check running'''


def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == process_name:
            return pid
        print("done")


'''kill'''


def kill(name):
    for proc in psutil.process_iter():
        if proc.name() == name:
            proc.kill()
        else:
            pass


'''Get Progs'''
def get_data():
    time.sleep(180) # 开机时可能没有网络 等待3min获取网络
    while True:
        global status, prog_list, plan_day, plan_month, plan_hours, plan_minutes, title, get_message, POWERPNT_status, POWERPNT_message, Seewo_status, Seewo_message
        try:
            data = {
                'message': 'april_fools_day',
            }  # Get data

            url = "我的网络api"  # Get license url
            resp = requests.post(url=url, data=data)  # Use post to get license
            resp_json = resp.json()  # Turn json
            print(resp_json)
            # ~~JSON parsing~~
            
            # 根据自己api参数填写
            
            status = 
            prog =
            plan_day = 
            plan_month =
            plan_hours =
            plan_minutes = 
            title = 
            get_message = 
            POWERPNT_status = 
            POWERPNT_message = 
            Seewo_status = 
            Seewo_message = 
            prog_list = prog
        except:
            pass
        time.sleep(1800)




def killing(get_message, month, day, hours, minutes):
    print("Running")
    for prog in prog_list:
        try:
            if isinstance(proc_exist(prog), int):
                kill(prog)
                print("Closed -- ", prog)
                if status == 2:
                    if prog == 填写蹦出提示应用包名:
                        prog_name = name_dictionary[prog]
                        message = get_message.replace("!month!", month).replace("!day!", day).replace("!prog!",prog_name)
                        win32api.MessageBox(0, message, title, win32con.MB_ICONASTERISK)
                    else:
                        pass
            else:
                pass
        except:
            pass


get_web_data=threading.Thread(target=get_data, args=())
get_web_data.start()
time.sleep(200)


'''while-True Check'''
while True:
    # Get now date
    month = time.strftime("%m", time.localtime())
    day = time.strftime("%d", time.localtime())
    hours = time.strftime("%H", time.localtime())
    minutes = time.strftime("%M", time.localtime())
    if status != 0:
        if len(plan_month) == 1:
            plan_month = "0" + str(plan_month)
        if len(plan_day) == 1:
            plan_day = "0" + str(plan_day)
        if month == plan_month and day == str(plan_day):
            if hours < plan_hours:
                killing(get_message, month, day, hours, minutes)
            if hours == plan_hours and minutes < plan_minutes:
                killing(get_message, month, day, hours, minutes)
        else:
            time.sleep(600)
