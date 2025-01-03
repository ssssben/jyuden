# SPDX-FileCopyrightText: 2024 Ben
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    batterytalker = launch_ros.actions.Node(
        package='mypkg',
        executable='batterytalker',
        output='screen'
    )
    batterylistener = launch_ros.actions.Node(
        package='mypkg',
        executable='batterylistener',
        output='screen'
    )
    return launch.LaunchDescription([batterytalker, batterylistener])

