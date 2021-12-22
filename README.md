# manjaro-setup

## Pacman&Yay

If you live/work in China mainland (we later use CN for short in this simple toturial) , use the following command below  to run a speedtest of mirrors sites in China. 

如果你生活/工作在中国大陆（以下简称CN），我们推荐你使用以下命令对中国的镜像站进行测速，并且换源。

You can replace the parameter [China] with other country's name.

```bash
pacman-mirrors -i -c China -m rank
```



Refresh `pacman`

刷新`pacman`缓存

```
sudo pacman -Sy
```



We recomand `yay` as your main package manager instead of `pacman` (espescially for users in CN).

推荐CN用户使用`yay`作为主要的包管理器。而不是`pacman`

```bash
pacman -S yay
```



For users in CN, adding tsinghua mirror site as your ArchLinux Repo Server would be a better choice.

推荐清华镜像站作ArchLinux中国源。

Manjaro don't have `vim` preinstalled, since `vi` is way too old, we should install `vim` first.

Manjaro只有老旧的`vi`，没有预装`vim`，我们先安装`vim`

```bash
yay vim
```

```bash
vim /etc/pacman.conf
```

```bash
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```



Refresh and add GPG key.

刷新并添加GPG密钥。

```bash
sudo pacman -Sy && sudo pacman -S archlinuxcn-keyring
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

重起生效。



## Font Size

If you are using a high resolution screen (like a 4K one),  we recomand you use tweak to upscale your font size other than upscale resolution. Press the win button, and search tweak, open it, you will find what to do next.



## V2Ray

Install v2ray core first:

```bash
yay v2ray
```



We recomand Qv2ray as you GUI for v2ray.(Although it's no longer under maintenance )

Use `which v2ray` to find where the v2ray core lies, usually the pat would be `usr/bin/v2ray`

the resouce director of v2ray would be `usr/shares/v2ray` usually .



## Quick Launch Your Terminal

Setting->Keyboard->Shortcut->Custom

设置->键盘->键盘快捷键->自定义快捷键



Command: gnome-terminal

Combo: whatever you like, we use `Ctrl + Shift + T`



## Install Utools

```bash
yay -S utools
```



To autostart utools, create a new Empty Desktop File, adding:

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


## 开机启动脚本
### 创建服务
```
sudo vim /etc/systemd/system/rc-local.service
```
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
### 创建脚本执行程序

```
sudo vim /etc/rc.local
```
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
添加执行权限：
```
sudo chmod a+x /etc/rc.local
```
### 创建脚本目录
```
sudo mkdir /etc/rc.local.d
```

所有需要开机执行的脚本放在这个文件夹下就可以了

### 启动服务
下次开机启动
```
systemctl enable rc-local.service
```
本次启动
```
systemctl start rc-local.service
```








