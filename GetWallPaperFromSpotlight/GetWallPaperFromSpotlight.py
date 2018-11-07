#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import shutil
from PIL import Image  



#获取聚焦图片路径
wallpaper_folder = os.getenv('LOCALAPPDATA')+ ('\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
print(wallpaper_folder)

#获取存放到onedrive的路径
save_folder  = os.getenv('onedrive')+('\图片\Spotlight')
print(save_folder )


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

 print('Save wallpaper ' + save_path)

wallpapers = os.listdir(save_folder)
for wallpaper in wallpapers:
    img = Image.open(wallpaper)
    print img.size
    print img.format 
