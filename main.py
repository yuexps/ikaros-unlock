import time
import ctypes
import os
import sys
import shutil
import hashlib
import subprocess
import requests
import json
import webbrowser


ctypes.windll.kernel32.SetConsoleTitleW("ikaros-unlock")
time.sleep(1)
print("欢迎使用伊卡洛斯过验证~")

def resource_path(relative_path):
        """获取程序中所需文件资源的绝对路径"""
        try:
        # PyInstaller创建临时文件夹,将路径存储于_MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


def read_config():
    config_file=resource_path('data/config.json')
    with open(config_file,encoding='utf-8') as config:
        config_data = json.load(config)

        global version
        version = config_data.get('version')
        global check_updata
        check_updata = config_data.get('check_updata')

read_config()


def updata():
    if check_updata == 'true':
          try:
               response = requests.get('https://baidu.com')
               if response.status_code == 200:
                    print("检查更新中...")
          except:
               print("貌似您的网络在摸鱼呢~")
               print("请检查网络是否正常！")
               os.system("pause")
               sys.exit()
          else:
               updtat_url = "https://gitee.com/xjhw/ikaros-tools/raw/master/check/ikaros-unlock_updata.json"
               updata = requests.get(updtat_url).text
               updata_json = json.loads(updata)

               updata_version = updata_json.get('version')
               updata_log = updata_json.get('updata_log')
               updata_url = updata_json.get('updata_url')

               if version == updata_version:
                    print("伊卡洛斯：已是最新版！")
               else:
                    print("伊卡洛斯：检测到更新，请为我升级哒~")
                    print("更新内容：",updata_log)
                    print("下载：",updata_url)
                    os.system("pause")
                    webbrowser.open(updata_url)
                    sys.exit()
    else:
         print("伊卡洛斯：已关闭更新检查~")

updata()


time.sleep(1)
print("--------功能-------")
print("(a).Minecraft安装")
print("(b).Minecraft过验证")
print("(c).Minecraft还原")
print("------------------")

time.sleep(1)
function = input("选择a/b/c：")

if function == 'a':
     print("前往微软商店安装Minecraft免费试用版~")
     os.system("pause")
     webbrowser.open('https://www.xbox.com/zh-CN/games/store/minecraft-for-windows/9NBLGGH2JHXJ/0010')
     sys.exit()

elif function == 'b':

     ctypes.windll.kernel32.SetConsoleTitleW("Minecraft过验证")
     time.sleep(1)
     print("请选择符合您条件的系统!")
     print("---操作系统---")
     print("(a).Windows11")
     print("(b).Windows10")
     print("-------------")
     time.sleep(1)
     windows = input("选择a/b：")
     if windows == 'a':
          file_a = resource_path('src/mc_a.py')
          exec(open(file_a,encoding='utf-8').read())
     elif windows == 'b':
          file_b = resource_path('src/mc_b.py')
          exec(open(file_b,encoding='utf-8').read())
     else:
          print("未知编号!")
          os.system("pause")
          sys.exit()

elif function == 'c':

     ctypes.windll.kernel32.SetConsoleTitleW("Minecraft还原")
     time.sleep(1)
     print("请选择符合您条件的系统!")
     print("---操作系统---")
     print("(a).Windows11")
     print("(b).Windows10")
     print("-------------")
     time.sleep(1)
     windows = input("选择a/b：")
     if windows == 'a':
          file_a = resource_path('src/mc_a_r.py')
          exec(open(file_a,encoding='utf-8').read())
     elif windows == 'b':
          file_b = resource_path('src/mc_b_r.py')
          exec(open(file_b,encoding='utf-8').read())
     else:
          print("未知编号!")
          os.system("pause")
          sys.exit()

else:
     print("未知编号!")
     os.system("pause")
     sys.exit()
