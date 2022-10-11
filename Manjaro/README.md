# Manjaro Setup



## ArchWiki

If you occur any trouble using Manjaro, go to ArchWiki first:

https://wiki.archlinux.org/

## Pacman&Yay

If you live/work in China mainland (we later use CN for short in this simple toturial) , use the following command below  to run a speedtest of mirrors sites in China. 

You can replace the parameter [China] with other country's name.

```bash
pacman-mirrors -i -c China -m rank
```

Refresh `pacman`

```
sudo pacman -Sy
```
We recomand use `yay` as your main package manager instead of `pacman` 

```bash
pacman -S yay
```



For users in China main land universities, adding tsinghua mirror site as your ArchLinux Repo Server would be a better choice.

For users don't have `vim` pre-installed, install `vim` first.

```bash
yay vim
```

```bash
vim /etc/pacman.conf
```

```bash
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
# Server = https://mirrors.aliyun.com/archlinuxcn/$arch
```

Refresh and add GPG key.

```bash
sudo pacman -Sy && sudo pacman -S archlinuxcn-keyring
```

## **System Update**

```
   yay -Syyu
```

## Adjust Font Size

If you are using a high resolution screen (like a 4K one), using gnome-tweaks to adjust your font-size is a more easy way to adapt hdpi. 

## Base dev tools
Basic dev tool shall be installed and updated first before all software installation behavior.

```
pacman -S base-devel
```

## Quick Launch Your Terminal

Setting->Keyboard->Shortcut->Custom


Command: gnome-terminal
Combo: whatever you like, we use `Ctrl + Shift + T`


## Software
### Chinses Pinyin

```bash
sudo pacman -S fcitx5-im fcitx5-configtool fcitx5-chinese-addons fcitx5-qt fcitx5-gtk 
```

To autostart fcitx5, we recomand using fcitx5-autostart


```bash
yay fcitx5-autostart
```

```bash
sudo vim ~/.xprofile
```

```bash
export GTK_IM_MODULE=fcitx5
export QT_IM_MODULE=fcitx5
export XMODIFIERS="@im=fcitx5"
fcitx5 &
```

To make pinyin work, you should reboot you computer.

### Utools

Utools is an efficiency tool with a rich marketplace of plugins.

```bash
yay -S utools
```

To autostart utools, create a new Empty Desktop File:

Create an new Empty Desktop File in `/home/xxx/.config/autostart`, adding:


```bash
[Desktop Entry]

Name=utools

Comment=utools

Exec=/usr/bin/utools

Type=Application

Terminal=false

X-GNOME-Autostart-enabled=true
```

Don't forget to rename this file!

Follow the steps above you can set other apps to autostart.


## Autostart A Service

### Create Service
```
sudo vim /etc/systemd/system/rc-local.service
```
Add:
写入：

```
[Unit]
Description="/etc/rc.local Compatibility" 

[Service]
Type=oneshot
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardInput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target
```
### Create Script

```
sudo vim /etc/rc.local
```
Add:

```
#!/bin/sh
# /etc/rc.local
if test -d /etc/rc.local.d; then
    for rcscript in /etc/rc.local.d/*.sh; do
        test -r "${rcscript}" && sh ${rcscript}
    done
    unset rcscript
fi
```
Add execution rights:

```
sudo chmod a+x /etc/rc.local
```
### Create script directory
```
sudo mkdir /etc/rc.local.d
```

All scripts that need to be executed on boot can be placed in this folder (don't forget to add .sh)

### Autostart Service 启动服务
Autostart next time

```
systemctl enable rc-local.service
```
Autostart this time

```
systemctl start rc-local.service
```







