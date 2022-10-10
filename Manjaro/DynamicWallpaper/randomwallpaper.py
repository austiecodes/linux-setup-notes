import os
import time
import random
import subprocess
import re

wallpaperpath = '图片或视频地址，可以放在一起'
wallpaperlist = os.listdir(wallpaperpath)
# 使用两个进程管理，因为有两个屏幕，其他情况可以增加或减少进程数量。
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
q = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
pattern = re.compile(r'[0-9]+x[0-9]+\+[0-9]+\+[0-9]+')
while True:
    if p.poll() is None:
        p.kill()
    if q.poll() is None:
        q.kill()

    r = random.randint(0, len(wallpaperlist) - 1)
    wallpaper = wallpaperlist[r]

    if os.path.splitext(wallpaper)[-1] in ['.jpg', '.jpeg', '.JPG', '.png', '.PNG']:
        p = subprocess.Popen(f'gsettings set org.gnome.desktop.background picture-uri "file:{os.path.join(wallpaperpath,wallpaper)}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        xrandr = subprocess.Popen('xrandr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        outlog = xrandr.stdout.read().decode()
        screens = pattern.findall(outlog)
        p = subprocess.Popen(f'xwinwrap -g {screens[0]} -fdt -ni -b -nf -un -o 1.0 -debug  -- mpv -wid WID --loop --no-audio {os.path.join(wallpaperpath,wallpaper)}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        q = subprocess.Popen(f'xwinwrap -g {screens[1]} -fdt -ni -b -nf -un -o 1.0 -debug  -- mpv -wid WID --loop --no-audio {os.path.join(wallpaperpath,wallpaper)}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time.sleep(60)