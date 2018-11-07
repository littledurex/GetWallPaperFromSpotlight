#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
from PIL import Image



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
