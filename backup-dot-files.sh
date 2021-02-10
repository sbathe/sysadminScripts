#!/bin/bash
dconf dump /org/gnome/terminal/legacy/profiles:/ > ~/gnome-terminal-profiles.dconf
p_files=".aliases .bash_profile .bashrc .fzf.bash .profile .vimrc gnome-terminal-profiles.dconf"
p_dirs="bin .gnupg .ssh"
squid_files="/etc/squid/squid.conf /etc/squid/squidGuard.conf /etc/cron.daily/squidGuard /etc/profile.d/proxy.sh /etc/dnf/dnf.conf"
mkdir -p ${HOME}/secrets

tar zcvf ${HOME}/secrets/dot-files.tar.gz -C $HOME --ignore-failed-read ${p_files} ${p_dirs} ${squid_files} 
