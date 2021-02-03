#!/bin/bash
dconf dump /org/gnome/terminal/legacy/profiles:/ > ~/gnome-terminal-profiles.dconf
p_files=".aliases .bash_profile .bashrc .fzf.bash .profile .vimrc gnome-terminal-profiles.dconf"
p_dirs="bin .gnupg .ssh"
mkdir -p ${HOME}/secrets

tar zcvf ${HOME}/secrets/dot-files.tar.gz -C $HOME --ignore-failed-read $p_files $p_dirs  
