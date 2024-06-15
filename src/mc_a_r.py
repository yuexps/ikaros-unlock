import os
import sys
import ctypes
import hashlib
import time


ctypes.windll.kernel32.SetConsoleTitleW("Minecraft恢复[win11]")

time.sleep(1)
print("伊卡洛斯：正在检查相关文件...")

def resource_path(relative_path):
    """获取程序中所需文件资源的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def system32_file_hash(file_path, hash_algorithm="sha256"):
    '''对比System32 DLL sha256'''
    hash_obj = hashlib.new(hash_algorithm)

    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break

            hash_obj.update(data)

    return hash_obj.hexdigest() 

try:
    file1 = resource_path("resouces/win11/System32/Windows.ApplicationModel.Store.dll")
    file2 = "C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll"

    hash1 = system32_file_hash(file1) 

    hash2 = system32_file_hash(file2) 

    if hash1 == hash2: 
        time.sleep(1)
        print("伊卡洛斯：System32 DLL 检查通过~")
    else:
        print("伊卡洛斯：检查未通过！")
        os.system("pause")
        sys.exit()

except Exception as h:
    print(h)
    print("错误：System32 DLL 检查失败！")
    os.system("pause")
    sys.exit()


def SysWOW64_file_hash(file_path, hash_algorithm="sha256"):
    '''对比SysWOW64 DLL sha256'''
    hash_obj = hashlib.new(hash_algorithm)

    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break

            hash_obj.update(data)

    return hash_obj.hexdigest() 

try:
    file1 = resource_path("resouces/win11/SysWOW64/Windows.ApplicationModel.Store.dll")
    file2 = "C:\\Windows\\SysWOW64\\Windows.ApplicationModel.Store.dll"

    hash1 = SysWOW64_file_hash(file1) 

    hash2 = SysWOW64_file_hash(file2) 

    if hash1 == hash2: 
        time.sleep(1)
        print("伊卡洛斯：SysWOW64 DLL 检查通过~")
    else:
        print("伊卡洛斯：检查未通过！")
        os.system("pause")
        sys.exit()

except Exception as i:
    print(h)
    print("错误：SysWOW64 DLL 检查失败！")
    os.system("pause")
    sys.exit()


def welcome():
    time.sleep(1)
    print("----------------------------")
    print("伊卡洛斯：请先了解此操作~")
    print("还原‘过验证’时修改的系统文件！")
    print("解除过验证状态，恢复正版验证！")
    print("仅支持Windows11，严禁混用！！")
    print("涉及恢复系统文件，需管理员权限")
    print("---------------------------")

    time.sleep(3)
    elua = input("你是否已了解并执行还原？y/n: ")
    if elua == 'y':
        time.sleep(1)
        print("开始处理...")
    else:
        time.sleep(1)
        sys.exit()

welcome()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print(">权限检查通过！<")
else:
    print("权限不足，请使用管理员权限运行！")
    os.system("pause")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
    sys.exit()


def system32():
    try:
        '''处理 System32 DLL'''

        print("删除过验证文件System32 DLL...")
        os.remove('C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll')
        print("System32 DLL 删除成功！")

        print("恢复System32 DLL备份...")
        old_path_32 = 'C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll'
        new_path_32 = 'C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll.backup'
        os.rename(new_path_32,old_path_32)
        time.sleep(1)
        print(">伊卡洛斯：System32 DLL 恢复完成！<")
    except Exception as m:
        print(m)
        print("错误：System32 DLL 处理失败")
        os.system("pause")
        sys.exit()

system32()


def SysWOW64():
    try:
        '''处理 SysWOW64 DLL'''

        print("删除过验证文件SysWOW64 DLL...")
        os.remove('C:\\Windows\\SysWOW64\\Windows.ApplicationModel.Store.dll')
        print("SysWOW64 DLL 删除成功！")

        print("恢复SysWOW64 DLL备份...")
        old_path_32 = 'C:\\Windows\\SysWOW64\\Windows.ApplicationModel.Store.dll'
        new_path_32 = 'C:\\Windows\\SysWOW64\\Windows.ApplicationModel.Store.dll.backup'
        os.rename(new_path_32,old_path_32)
        time.sleep(1)
        print(">伊卡洛斯：SysWOW64 DLL 恢复完成！<")
    except Exception as n:
        print(n)
        print("错误：SysWOW64 DLL 处理失败")
        os.system("pause")
        sys.exit()

SysWOW64()

time.sleep(1)
print(">伊卡洛斯：Minecraft还原结束！！！<")

os.system("pause")
sys.exit()