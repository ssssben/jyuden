#!/bin/bash
# SPDX-FileCopyrightText: 2024 Ben
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"
cd $dir/ros2_jyuuden_ws || { echo "Workspace not found"; exit 1; }
colcon build --symlink-install || { echo "Build failed"; exit 1; }
source install/setup.bash
ros2 run mypkg batterytalker &
TALKER_PID=$!
ros2 topic echo /battery_status > /tmp/battery_status.log &
ECHO_PID=$!
trap "kill -SIGINT $TALKER_PID $ECHO_PID; exit" SIGINT SIGTERM
tail -f /tmp/battery_status.log
