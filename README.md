# Univesal Setup

这里是常见的 Linux 发行版通用的几个设置。

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

## Others
### Spotify Upscale
Try using "ctrl" and "+"
### Steam Upscale

### WeChat (For China mainland Users)
We recommend using wine and install wechat.exe using wine.
