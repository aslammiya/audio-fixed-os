#!/bin/bash

R="$(printf '\033[1;31m')"
G="$(printf '\033[1;32m')"
Y="$(printf '\033[1;33m')"
W="$(printf '\033[1;37m')"
C="$(printf '\033[1;36m')"

package() {
    echo -e "${R} [${W}-${R}]${C} Checking required packages..."${W}
    sudo apt-get update -y
    sudo apt install udisks2 -y
    sudo rm /var/lib/dpkg/info/udisks2.postinst
    echo "" > /var/lib/dpkg/info/udisks2.postinst
    sudo dpkg --configure -a
    sudo apt-mark hold udisks2
    packs=(sudo wget curl nano git keyboard-configuration tzdata xfce4 xfce4-goodies xfce4-terminal firefox menu inetutils-tools dialog exo-utils tigervnc-standalone-server tigervnc-common dbus-x11 fonts-beng fonts-beng-extra vlc gtk2-engines-murrine gtk2-engines-pixbuf)
    for hulu in "${packs[@]}"; do
        type -p "$hulu" &>/dev/null || {
            echo -e "\n${R} [${W}-${R}]${G} Installing package : ${Y}$hulu${C}"${W}
            sudo apt-get install "$hulu" -y --no-install-recommends
        }
    done
    sudo apt-get update -y
    sudo apt-get upgrade -y
    sudo apt-get clean
}

theme() {
    theme=(Bright Xfce-flat Daloa Xfce-kde2 Xfce-kolors Xfce-4.4 Xfce-light Xfce-4.6 Xfce-orange Emacs Xfce-b5 Xfce-redmondxp Xfce-basic Xfce-saltlake Moheli Xfce-cadmium Xfce-smooth Xfce-curve Xfce-stellar Retro Xfce-dawn Xfce-winter Smoke Xfce-dusk)
    for rmi in "${theme[@]}"; do
        type -p "$rmi" &>/dev/null || {
            sudo rm -rf /usr/share/themes/"$rmi"
        }
    done
}

font() {
    fonts=(hicolor LoginIcons ubuntu-mono-light)
    for rmf in "${fonts[@]}"; do
        type -p "$rmf" &>/dev/null || {
            sudo rm -rf /usr/share/icons/"$rmf"
        }
    done
}

refs() {
    sudo apt-get update -y
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
    sudo apt-get upgrade -y
    sudo apt autoremove -y
   
    git clone --depth=1 https://github.com/vinceliuice/Layan-gtk-theme.git $HOME/Layan-gtk-theme
    sudo chmod +x $HOME/Layan-gtk-theme/install.sh
    sudo bash $HOME/Layan-gtk-theme/install.sh

    git clone --depth=1 https://github.com/vinceliuice/Qogir-icon-theme.git $HOME/Qogir-icon-theme
    sudo chmod +x $HOME/Qogir-icon-theme/install.sh
    sudo bash $HOME/Qogir-icon-theme/install.sh

    git clone --depth=1 https://github.com/s-h-3-l-l/katoolin3.git $HOME/katoolin3
    sudo chmod +x $HOME/katoolin3/install.sh
    cd $HOME/katoolin3 && sudo bash install.sh

    sudo apt update -y
    sudo apt autoremove -y

}

vnc() {
    echo -e "${R} [${W}-${R}]${C} Setting up VNC Server..."${W}

    if [[ ! -d "$HOME/.vnc" ]]; then
        mkdir -p "$HOME/.vnc"
    fi

    if [[ -e "$HOME/.vnc/xstartup" ]]; then
        rm -rf $HOME/.vnc/xstartup
    fi
   
    echo "export DISPLAY=":1"" >> /etc/profile
    echo "export PULSE_SERVER=127.0.0.1" >> /etc/profile 
    source /etc/profile

}

note() {
    echo -e " ${G} Successfully Installed !"${W}
}

package
theme
font
refs
vnc
note
