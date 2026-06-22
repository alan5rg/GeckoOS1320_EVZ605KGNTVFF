#!/bin/bash

DESKTOP=$(echo "$XDG_CURRENT_DESKTOP" | tr '[:upper:]' '[:lower:]')

if [[ "$DESKTOP" == *"xfce"* ]]; then
    # Leer estado actual en XFCE
    ESTADO=$(xfconf-query -c xfwm4 -p /general/use_compositing)
    if [ "$ESTADO" = "true" ]; then
        xfconf-query -c xfwm4 -p /general/use_compositing -s false
    else
        xfconf-query -c xfwm4 -p /general/use_compositing -s true
    fi

elif [[ "$DESKTOP" == *"mate"* ]]; then
    # Leer estado actual en MATE
    ESTADO=$(gsettings get org.mate.Marco.general compositing-manager)
    if [ "$ESTADO" = "true" ]; then
        gsettings set org.mate.Marco.general compositing-manager false
    else
        gsettings set org.mate.Marco.general compositing-manager true
    fi

else
    # X11 genérico con picom/xcompmgr
    if pgrep -x "picom" > /dev/null; then
        killall picom
    elif pgrep -x "xcompmgr" > /dev/null; then
        killall xcompmgr
    else
        picom -b &>/dev/null || xcompmgr -c &>/dev/null &
    fi
fi
