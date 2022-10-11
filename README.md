# Univesal Setup

Universal setup for popular linux distros.

## HiDPI
Find Fractional Scaling option in your settings for ubuntu family.

For Manjaro users, detail in Manjaro folders.

## Basics
```shell
#using your package manager to install some basic software, we here using ubuntu as exmaple

sudo apt update
sudo apt install zsh vim git curl wget -y
```

## zsh & oh-my-zsh

### Oh-my-zsh

| Method    | Command                                                      |
| --------- | ------------------------------------------------------------ |
| **curl**  | `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |
| **wget**  | `sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |
| **fetch** | `sh -c "$(fetch -o - https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"` |



### Oh-my-zsh plugins

Syntax-highlighting and autosuggestions are two must haves.


``` shell
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

#Add plugins in ~/.zshrc:

vim ./.zshrc

plugins=(git zsh-syntax-highlighting zsh-autosuggestions)

#Reload zshrc configuration
source ./.zshrc

```


## Dual System Time Sync

If you use dual system( Windows + Linux)，time sync between these two system is necessary


Launch your powershell as admin in windows

```
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG/QWORD /f 
```

## Others

### For China mainland users, Clash is now a better choice on Linux than qv2ray or other proxy apps
We recommand you to use clash-for-windows(cfw) linux version, cfw was originally built for windows, but now it has macOS and linux distros.

Search `clash for windows` in GitHub then download its linux version.

Extract the tar.gz file to you home directory, we recommand that rename it as clash for convenience.

Run the file named `cfw`, you will see the GUI. Go to Profiles tab, paste the link that your V2Ray or SS service providers offerd, then click download.

To autostart CFW, activate start with linux option in its dashborad.



### Install Wine to use Windows Apps

Install Wine using your package manager or following instrustions on Wine's website.

https://wiki.winehq.org/Ubuntu

To make wine adapted to hidpi, use winecfg
```shell
winecfg
```


### Spotify Upscale
Try using "ctrl" and "+". If not working, try this: https://community.spotify.com/t5/Desktop-Linux/Linux-client-barely-usable-on-HiDPI-displays/td-p/1067272

### Steam Upscale
Details in this issue
https://github.com/ValveSoftware/steam-for-linux/issues/5460#issuecomment-627668987

If the method above didn't work, try launch steam in BigPicture Mod, and quit BigPicture Mod after launching.



###
### WeChat (For China mainland Users)
you can use scripts to install deepin-wine-wechat. Details in this repo:
https://github.com/zq1997/deepin-wine

Or you can use wine to install wechat.exe
```
# Install some dependencies
winetricks fakechinese corefonts gdiplus riched20 riched30

# Get WechatSetup.exe
wget https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe

# using wine to install this exe file
wine WineChatSetup.exe
```


