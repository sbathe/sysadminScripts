#!/bin/bash
libvirtmacid="52:54:00:"
lasttriade=$(dd if=/dev/urandom bs=512 count=1 2>/dev/null | md5sum | sed 's/\(..\)/\1:/g' | cut -d":" -f1,2,3)
echo ${libvirtmacid}${lasttriade}
