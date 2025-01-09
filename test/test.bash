#!/bin/bash
# SPDX-FileCopyrightText: 2025 ben fang
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch jyuden talk_listen.launch.py > /tmp/jyuden.log

cat /tmp/jyuden.log |
grep 'Count: 9'
