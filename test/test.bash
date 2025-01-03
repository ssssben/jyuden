#!/bin/bash
# SPDX-FileCopyrightText: 2024 Ben
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
ros2 run mypkg batterytalker > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Battery level'
