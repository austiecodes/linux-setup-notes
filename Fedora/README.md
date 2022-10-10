**At the very beginning, we suggest install vim/nvim.**

## Basic Adjustments

### Changing the default GNOME session via configuration file

As an alternative, this change can be made by editing a configuration file `/etc/gdm/custom.conf`.

1. Open `/etc/gdm/custom.conf` and uncomment the line:

   ```
   WaylandEnable=false
   ```

2. Add the following line to the `[daemon]` section:

   ```
   DefaultSession=gnome-xorg.desktop
   ```

3. Save the `custom.conf` file.

4. Logout or reboot to enter the new session.



### High-DPI Adaption

```shell
sudo dnf install gnome-tweaks
```

Google Gnome Extension, add gnome-extension for Firefox/Chrome

Search:

"appindicator"  for indicating extensions in tray

"kimpannel" for indicating fcitx5 logo in tray





## DNF&Shell

### Enable RPM fusion

1. To enable the *Free* repository, use:

   ```shell
   $ sudo dnf install \
     https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
   ```

2. Optionally, enable the *Nonfree* repository:

   ```shell
   $ sudo dnf install \
     https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
   ```







## Software

### Basic Ones

```shell
sudo dnf install nvim(or vim)
```

### VSCode

### RHEL, Fedora, and CentOS based distributions[#](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions)

We currently ship the stable 64-bit VS Code in a yum repository, the following script will install the key and repository:

```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```

Then update the package cache and install the package using `dnf` (Fedora 22 and above):

```
dnf check-update
sudo dnf install code
```

Or on older versions using `yum`:

```
yum check-update
sudo yum install code
```

Due to the manual signing process and the system we use to publish, the yum repo may lag behind and not get the latest version of VS Code immediately.

### Input Source

Install Fcitx5

```shell
sudo dnf install fcitx5
sudo dnf install fcitx5-configtool
sudo dnf install fcitx5-autostart
sudo dnf install fcitx5-chinese-addons
sudo dnf install fcitx5-rime
```



