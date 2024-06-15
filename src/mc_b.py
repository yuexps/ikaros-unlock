import os
import sys
import ctypes
import shutil
import hashlib
import time


ctypes.windll.kernel32.SetConsoleTitleW("Minecraft过验证[win10]")

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
    file1 = resource_path("resouces/win10/System32/Windows.ApplicationModel.Store.dll")
    file2 = "C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll"

    hash1 = system32_file_hash(file1) 

    hash2 = system32_file_hash(file2) 

    if hash1 == hash2: 
        time.sleep(1)
        print("伊卡洛斯：你已解锁过了，无需重复解锁！！！")
        os.system("pause")
        sys.exit()
    else:
        time.sleep(1)
        print("伊卡洛斯：System32 DLL 检查通过~")
except Exception as h:
    print(h)
    print("错误：System32 DLL 检查失败！")
    os.system("pause")
    sys.exit()


def SystemWOW64_file_hash(file_path, hash_algorithm="sha256"):
    '''对比SystemWOW64 DLL sha256'''
    hash_obj = hashlib.new(hash_algorithm)

    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break

            hash_obj.update(data)

    return hash_obj.hexdigest() 

try:
    file1 = resource_path("resouces/win10/SystemWOW64/Windows.ApplicationModel.Store.dll")
    file2 = "C:\\Windows\\SystemWOW64\\Windows.ApplicationModel.Store.dll"

    hash1 = SystemWOW64_file_hash(file1) 

    hash2 = SystemWOW64_file_hash(file2) 

    if hash1 == hash2: 
        print("伊卡洛斯：你已解锁过了，无需重复解锁！！！")
        os.system("pause")
        sys.exit()
    else:
        time.sleep(1)
        print("伊卡洛斯：SystemWOW64 DLL 检查通过~")
except Exception as i:
    print(h)
    print("错误：SystemWOW64 DLL 检查失败！")
    os.system("pause")
    sys.exit()


def welcome():
    time.sleep(1)
    print("伊卡洛斯：欢迎使用Minecraft For Windows解锁工具~")
    time.sleep(1)
    print("------------------ELUA-----------------")
    print("此程序仅供学习研究，严禁用于其他用途！！！")
    print("解锁原理涉及修改系统文件，需使用管理员权限")
    print("解锁后可能会导致Microsoft Store异常..等！")
    print("禁止滥用，有能力请支持Minecraft正版！！！")
    print("仅支持Windows10，仅支持Windows10 ！！！")
    print("Minecraft官网：https://minecraft.net")
    print("---------------------------------------")

    time.sleep(3)
    elua = input("你是否已了解并同意上述条款？y/n: ")
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
        print("夺取System32 DLL文件所有者...")
        os.system('takeown /a /f %windir%\System32\Windows.ApplicationModel.Store.dll')
        print("System32 DLL文件所有者夺取成功！")

        print("获取System32 DLL文件权限...")
        os.system('icacls %windir%\System32\Windows.ApplicationModel.Store.dll /c /grant Administrators:F')
        print("System32 DLL文件权限获取成功！")

        print("备份原System32 DLL...")
        old_path_32 = 'C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll'
        new_path_32 = 'C:\\Windows\\System32\\Windows.ApplicationModel.Store.dll.backup'
        os.rename(old_path_32,new_path_32)
        print("System32 DLL 备份成功！")

        print("替换新System32 DLL...")
        src_path_32 = resource_path("resouces/win10/System32/Windows.ApplicationModel.Store.dll")
        dst_path_32 = 'C:\\Windows\\System32'
        shutil.copy(src_path_32, dst_path_32)
        time.sleep(1)
        print(">伊卡洛斯：System32 DLL 处理完成！<")
    except Exception as m:
        print(m)
        print("错误：System32 DLL 处理失败")
        os.system("pause")
        sys.exit()

system32()


def SystemWOW64():
    try:
        '''处理 SystemWOW64 DLL'''
        print("夺取SystemWOW64 DLL文件所有者...")
        os.system('takeown /a /f %windir%\SystemWOW64\Windows.ApplicationModel.Store.dll')
        print("SystemWOW64 DLL文件所有者夺取成功！")

        print("获取SystemWOW64 DLL文件权限...")
        os.system('icacls %windir%\SystemWOW64\Windows.ApplicationModel.Store.dll /c /grant Administrators:F')
        print("SystemWOW64 DLL文件权限获取成功！")

        print("备份原SystemWOW64 DLL...")
        old_path_64 = 'C:\\Windows\\SystemWOW64\\Windows.ApplicationModel.Store.dll'
        new_path_64 = 'C:\\Windows\\SystemWOW64\\Windows.ApplicationModel.Store.dll.backup'
        os.rename(old_path_64,new_path_64)
        print("SystemWOW64 DLL 备份成功！")

        print("替换新SystemWOW64 DLL...")
        src_path_64 = resource_path("resouces/win10/SystemWOW64/Windows.ApplicationModel.Store.dll")
        dst_path_64 = 'C:\\Windows\\SystemWOW64'
        shutil.copy(src_path_64, dst_path_64)
        time.sleep(1)
        print(">伊卡洛斯：SystemWOW64 DLL 处理完成！<")
    except Exception as n:
        print(n)
        print("错误：SystemWOW64 DLL 处理失败")
        os.system("pause")
        sys.exit()

SystemWOW64()

time.sleep(1)
print(">伊卡洛斯：Minecraft处理结束！！！<")

os.system("pause")