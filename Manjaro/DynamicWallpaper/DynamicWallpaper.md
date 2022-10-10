# 自定义壁纸

壁纸分为静态壁纸和动态壁纸，可以通过简单的命令进行设置。

# 静态壁纸

对于Gnome 桌面, 设置静态壁纸可以通过命令:

```bash
gsettings set org.gnome.desktop.background picture-uri "file:/xxx/xxx.png"
```

其中file可以是任意图片，但是不支持动态图片和视频。

# 动态壁纸

Linux下没有很好的动态壁纸，壁纸引擎这类的软件并没有考虑开发Linux版本。
但是，通过一些软件我们可以添加视频动态壁纸。
我们借助于项目[xwinwrap](https://github.com/ujjwal96/xwinwrap)实现动态壁纸。
* 根据项目的引导安装xwinwarp，安装的依赖库可以换成相应的ArchLinux包
* 安装一个视频播放后端，这里推荐mpv播放器，这个播放器性能消耗少，通过pacman或yay安装即可

安装好之后执行命令:

```bash
xwinwrap -g 屏幕位置和宽高 -fdt -ni -b -nf -un -o 1.0 -debug  -- mpv -wid WID --loop --no-audio 视频地址
```

屏幕位置和宽高的格式为: WxH+X+Y, 如果XY都为0可以省略后面的部分。
如果有多个屏幕可以通过xrandr命令查询屏幕的宽高和位置，如“DP-0 connected 3840x2160+0+0”当中的3840x2160+0+0就是上面命令需要填写的内容。
-- mpv 表示使用mpv后端
--loop 表示循环播放
--no-audio 表示不播放声音

注意：
* 这条命令执行后在终端会一直执行并持续打印输出
* 视频的宽高需要与屏幕比例相同，否则会出现黑边(如果能够接受黑边请随意)

附带一个基于python的随机壁纸播放脚本实例。
