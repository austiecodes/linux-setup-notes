# Manjaro Setup



## ArchWiki

If you occur any trouble using Manjaro, go to ArchWiki first:
在使用中遇到任何问题，优先查询

https://wiki.archlinux.org/

## Pacman&Yay

If you live/work in China mainland (we later use CN for short in this simple toturial) , use the following command below  to run a speedtest of mirrors sites in China. 
如果你生活/工作在中国大陆（以下简称 CN），我们推荐你使用以下命令对中国的镜像站进行测速，并且换源。

You can replace the parameter [China] with other country's name.

```bash
pacman-mirrors -i -c China -m rank
```



Refresh `pacman`
刷新`pacman`缓存

```
sudo pacman -Sy
```



We recomand use `yay` as your main package manager instead of `pacman` (espescially for users in CN).
推荐 CN 用户使用`yay`作为主要的包管理器。而不是`pacman`

```bash
pacman -S yay
```



For users in CN universities, adding tsinghua mirror site as your ArchLinux Repo Server would be a better choice.
For other users, we recommand Aliyun.
推荐教育网用户使用清华镜像站作 ArchLinux 中国源。其他用户推荐阿里云。

For users don't have `vim` pre-installed, install `vim` first.
没装 `vim` 的话，先装 `vim`

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
刷新并添加 GPG 密钥。

```bash
sudo pacman -Sy && sudo pacman -S archlinuxcn-keyring
```

## **System Update**

```
   yay -Syyu
```

## Chinse Pinyin

```bash
sudo pacman -S fcitx-im
sudo pacman -S fcitx-configtool
sudo pacman -S fcitx-googlepinyin
```

```bash
sudo vim ~/.xprofile
```

```bash
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
```

To make pinyin work, you should reboot you computer.
重启生效。

## Adjust Font Size

If you are using a high resolution screen (like a 4K one),  we recomand you use tweak to upscale your font size other than upscale resolution. Press the win button, and search tweak, open it, you will find what to do next.
如果你使用高分辨率屏幕，我们推荐你增加字体大小而不是整体缩放，在抽屉里直接搜索 `tweak` 可以找到此款优化工具。



## Dual System Time Sync

If you use dual system( Windows + Linux)，time sync between these two system is necessary
双系统用户需要同步双系统时间

Launch your powershell as admin
以管理员身份启动 powershell

```
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG/QWORD /f 
```



## Software

Basic dev tool shall be installed and updated first before all software installation behavior.
在安装其他软件之前，先安装/更新所有的编译工具。

```
pacman -S base-devel
```

To install Chrome, you should add `google-` 
安装`chrome`记得加上前缀`google-`

```
yay google-chrome
```

### WPS

Install WPS office and it's fonts:
安装 WPS 和字体

```
yay wps-office
yay ttf-wps-fonts
```

### WeChat

```
yay deepin-wine-wechat 
```

### V2Ray

Install v2ray core first:

```bash
yay v2ray
```

We recomand Qv2ray as you GUI for v2ray.(Although it's no longer under maintenance )

Use `which v2ray` to find where the v2ray core lies, usually the pat would be `usr/bin/v2ray`

the resouce director of v2ray would be `usr/shares/v2ray` usually .

### Utools

Utools is an efficiency tool with a rich marketplace of plugins.
Utools 是一款有丰富插件市场的效率工具。

```bash
yay -S utools
```

To autostart utools, create a new Empty Desktop File:
设置 utools开机自启动：

Create an new Empty Desktop File in `/home/xxx/.config/autostart`, adding:
在`/home/xxx/.config/autostart`目录下新建Empty Desktop File,用编辑器打开，写入：

```bash
[Desktop Entry]

Name=utools

Comment=utools

Exec=utools

Type=Application

Terminal=false

X-GNOME-Autostart-enabled=true
```

Don't forget to rename this file!
不要忘记对这个文件重命名哟！

### Filezilla

```
yay filezilla
```



## Quick Launch Your Terminal

Setting->Keyboard->Shortcut->Custom
设置->键盘->键盘快捷键->自定义快捷键



Command: gnome-terminal
Combo: whatever you like, we use `Ctrl + Shift + T`


## Autostart Script
### Create Service 创建服务
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
### Create Script 创建脚本执行程序 

```
sudo vim /etc/rc.local
```
Add:
写入：

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
添加执行权限：

```
sudo chmod a+x /etc/rc.local
```
### Create script directory 创建脚本目录
```
sudo mkdir /etc/rc.local.d
```

All scripts that need to be executed on boot can be placed in this folder (don't forget to add .sh)
所有需要开机执行的脚本放在这个文件夹下就可以了（不要忘记 .sh 后缀）

### Autostart Service 启动服务
Autostart next time
下次开机启动

```
systemctl enable rc-local.service
```
Autostart this time
本次启动

```
systemctl start rc-local.service
```







