#!/bin/bash
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode DVI-I-1 1920x1080_60.00
xrandr --output DVI-I-1 --mode 1920x1080_60.00
xrandr --output DVI-I-1 --mode 1920x1080_60.00 --auto --output VGA-1 --mode 1920x1080 --rotate normal --pos 1920x0 --primary

