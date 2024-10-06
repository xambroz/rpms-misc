#!/bin/bash

for I in $(ldd minecraft-launcher) ; do
    echo "$I" | grep -e '^/' >/dev/null
    if [ $? -eq 0 ] ; then
        rpm -qf "$I"
    fi
done |
sed -e 's/-[0-9.]*-.*x86_64//' |
sort -u |
xargs -i echo "Requires:" "{}"



