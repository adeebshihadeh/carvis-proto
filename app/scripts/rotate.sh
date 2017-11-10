#!/bin/sh

#portrait (left)

xrandr -o left
xinput set-prop "ILITEK ILITEK Multi-Touch" --type=float "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
