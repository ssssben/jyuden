# SPDX-FileCopyrightText: 2025 ben fang
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    batterytalker = launch_ros.actions.Node(
        package='jyuden',
        executable='batterytalker',
        output='screen'
    )
    batterylistener = launch_ros.actions.Node(
        package='jyuden',
        executable='batterylistener',
        output='screen'
    )
    return launch.LaunchDescription([batterytalker, batterylistener])

