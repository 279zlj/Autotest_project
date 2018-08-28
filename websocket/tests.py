from django.test import TestCase
from client.c_client import Client
# Create your tests here.
import json
import sqlite3
import time

# def save_data(data_response):
#     con = sqlite3.connect("D:\Autotestproject\Autotest_project\db.sqlite3")
#     cur = con.cursor()
#     cur.execute('insert into \
#                 auto_config_infos \
#                 (server_num,board,cpu,fc_card,gpu,hard_disk,hba,inspect_time,memory_bank,net_card,raid,status,vga) \
#                 values\
#                 ({},{},{},{},{},{},{},{},{},{},{},{},{})'.format(data_response["server_num"], data_response["board"],
#                                                                  data_response["cpu"], data_response["fc_card"],
#                                                                  data_response["gpu"], data_response["hard_disk"],
#                                                                  data_response["hba"], data_response["inspect_time"],
#                                                                  data_response["memory_bank"], data_response["net_card"], data_response["raid"],
#                                                                  data_response["status"], data_response["vga"]))
#     cur.execute('select * from auto_config_infos')
#     print(cur.fetchall())
#     con.commit()
#     cur.close()


# d = {"raid": "", "fc_card": "", "status": 1, "checkstate": 0, "server_num": "23dfgtr", "ip_info": "127.0.0.1",
#      "state": "success", "cpu": "CpuNum:1/CpuCore:4/CpuInfo:8Intel(R)Xeon(R)CPUE3-1230v3@3.30GHz",
#      "inspect_time": 1534484708.3386865, "vga": "Graphics:LeadTekResearchInc.GK107[GeForceGT640][107d:2737]\r\n",
#      "memory_bank": "MemInfo:*ASRock*Intel*Transcend/MemSize:4096MB/MemFreq:1600MT/s", "gpu": "", "hba": "",
#      "hard_disk": "DiskInfo:WDCWD10EURX-73C/DiskNum:1/DiskVer:/01.01A01",
#      "net_card": "NetBoardInfo:IntelCorporationEthernetConnection(2)I218-V",
#      "board": "BoardName:Z97Pro3/BisoVersion:P1.20"}

d = {"board": "BoardName:Z97Pro3/BisoVersion:P1.20", "hba": "",
     "net_card": "NetBoardInfo:IntelCorporationEthernetConnection(2)I218-V", "raid": "dash_raid",
     "vga": "Graphics:LeadTekResearchInc.GK107[GeForceGT640][107d:2737]\r\n", "ip_info": "127.0.0.1", "checkstate": 0,
     "memory_bank": "MemInfo:*ASRock*Intel*Transcend/MemSize:4096MB/MemFreq:1600MT/s", "state": "success",
     "hard_disk": "DiskInfo:WDCWD10EURX-73C/DiskNum:1/DiskVer:/01.01A01",
     "cpu": "CpuNum:1/CpuCore:4/CpuInfo:8Intel(R)Xeon(R)CPUE3-1230v3@3.30GHz", "gpu": "", "status": 1,
     "inspect_time": 1534486359.491127, "server_num": "23dfgtr", "fc_card": ""}


def save_data(data_response):
    print(data_response)
    con = sqlite3.connect("D:\Autotestproject\Autotest_project\db.sqlite3")
    cur = con.cursor()
    params = [data_response["server_num"], data_response["board"], data_response["cpu"], data_response["memory_bank"],
              data_response["hard_disk"], data_response["raid"], data_response["vga"], data_response["gpu"],
              data_response["hba"], data_response["net_card"], data_response["fc_card"], data_response["inspect_time"],
              data_response["ip_info"], data_response["checkstate"], data_response["state"], data_response["status"]]
    cur.execute('insert into auto_config_infos \
            (server_num,board,cpu,memory_bank,hard_disk,raid,vga,gpu,hba,net_card,fc_card,inspect_time,ip_info,checkstate,state,status) \
             values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', params)
    con.commit()
    cur.execute('select * from auto_config_infos')
    cur.close()


save_data(d)
