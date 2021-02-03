#!/bin/bash
# Backup existing files
mkdir -p ${HOME}/secrets
backup=".bash_profile .bashrc .p10k.zsh .profile .viminfo .zshrc .vim .gnupg .aliases"
tar zcvf ${HOME}/secrets/existing_dot_files.tar.gz -C $HOME --ignore-failed-read $backup

# Install required packges
sudo dnf install git wget curl ruby ruby-devel util-linux-user redhat-rpm-config gcc gcc-c++ make vim-enhanced
# install vim Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# Install Nerd Fonts
git clone --depth=1 https://github.com/ryanoasis/nerd-fonts ~/.nerd-fonts
cd ~/.nerd-fonts
sudo ./install.sh

sudo dnf install fontawesome-fonts
sudo dnf install powerline vim-powerline tmux-powerline powerline-fonts

sudo dnf install fzf bat ripgrep
sudo gem install colorls
#setup powerline with proper theme
mkdir -p ~/.config/powerline
cat <<-'EOF' > ~/.config/powerline/config.json
{
    "ext": {
        "shell": {
            "theme": "default_leftonly"
        }
    }
}
EOF

find ${HOME} -name dot-files.tar.gz -exec tar zxf {} \;
dconf load /org/gnome/terminal/legacy/profiles:/ < ${HOME}/gnome-terminal-profiles.dconf

