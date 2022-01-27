#!/bin/bash
wget "http://ccrma.stanford.edu/planetccrma/mirror/fedora/linux/planetccrma/$(rpm -E %fedora)/x86_64/planetccrma-repo-1.1-3.fc$(rpm -E %fedora).ccrma.noarch.rpm" -O /tmp/planetccrma-repo.rpm
sudo dnf install -y /tmp/planetccrma-repo.rpm
sudo dnf install -y jack-audio-connection-kit qjackctl kernel-rt jack-mixer.x86_64 jack-keyboard.x86_64
sudo usermod -a -G jackuser sb
sudo usermod -a -G jackuser shardool
sudo usermod -a -G jackuser shubhangi


