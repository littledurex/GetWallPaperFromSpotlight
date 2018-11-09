#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import win32gui
import win32con
import win32api
from PIL import Image


def setWallpaper(imagepath):
    #打开指定注册表路径
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE) 
    #最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "10")
    #最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    #刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, imagepath, win32con.SPIF_SENDWININICHANGE)
    


def listdir(path, list_name): #传入存储的list
 for file in os.listdir(path):
  file_path = os.path.join(path, file)
  if os.path.isdir(file_path): #如果是目录，则递归执行该方法
   listdir(file_path, list_name)
  else:
    list_name.append((file_path,os.path.getctime(file_path))) #把文件路径，文件创建时间加入list中

def newestfile(target_list): #传入包含文件路径，文件创建时间的list
 newest_file = target_list[0] #冒泡算法找出时间最大的
 for i in range(len(target_list)):
  if i < (len(target_list)-1) and newest_file[1] < target_list[i+1][1]:
   newest_file = target_list[i+1]
  else:
   continue
#print('newest file is',newest_file)
 return newest_file



#获取聚焦图片路径
wallpaper_folder = os.getenv('LOCALAPPDATA')+ ('\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
#print(wallpaper_folder)

#获取存放到onedrive的路径

save_folder  = os.getenv('onedrive')+('\图片\Spotlight')
save_folder_Horizontals  = os.getenv('onedrive')+('\图片\Spotlight\Horizontal')
save_folder_Vertical  = os.getenv('onedrive')+('\图片\Spotlight\Vertical')
#save_folder_CopyAssets  = os.getenv('onedrive')+('\图片\Spotlight\CopyAssets')

if not (os.path.exists(save_folder)):
    os.makedirs(save_folder)

if not (os.path.exists(save_folder_Horizontals)):
    os.makedirs(save_folder_Horizontals)

if not (os.path.exists(save_folder_Vertical)):
    os.makedirs(save_folder_Vertical)

#if not (os.path.exists(save_folder_CopyAssets)):
    os.makedirs(save_folder_CopyAssets)


#print(save_folder )


#列出所有的文件

wallpapers = os.listdir(wallpaper_folder)

for wallpaper in wallpapers:

 wallpaper_path = os.path.join(wallpaper_folder, wallpaper)

 # 小于150kb的不是锁屏图片

 if (os.path.getsize(wallpaper_path) / 1024) < 100:
    continue

 wallpaper_name = wallpaper + '.jpg'

 save_path = os.path.join(save_folder, wallpaper_name)

 if (os.path.exists(os.path.join(save_folder_Horizontals, wallpaper_name))):
     continue
 shutil.copyfile(wallpaper_path, save_path)

# print('Save wallpaper ' + save_path)

wallpapers = os.listdir(save_folder)

for wallpaper in wallpapers:
     if wallpaper.endswith(".jpg"): 
        save_path = os.path.join(save_folder, wallpaper)
#        print(save_path)
        img = Image.open(save_path)
        if img.size[0] >= 1920:
             save_path_Horizontals = os.path.join(save_folder_Horizontals, wallpaper)
             img.close()
             shutil.move(save_path,save_path_Horizontals)
        elif  img.size[0] >= 1080:
             save_path_Vertical = os.path.join(save_folder_Vertical, wallpaper)
             img.close()
             shutil.move(save_path,save_path_Vertical)
        else:
            img.close()
            os.remove(save_path)

# 设置壁纸
list = []
listdir(save_folder_Horizontals, list)
new_file = newestfile(list)
#print('from:', new_file[0])
setWallpaper(new_file[0])