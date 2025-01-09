# SPDX-FileCopyrightText: 2025 ben fang
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import psutil

class BatteryTalker(Node):
    def __init__(self):
        super().__init__('batterytalker')
        self.pub = self.create_publisher(Int16, 'battery_status', 10)
        self.create_timer(1.0, self.cb)

    def cb(self):
        battery = psutil.sensors_battery()
        percent = int(battery.percent) if battery else 0
        #self.get_logger().debug(f"{percent}%")
        msg = Int16(data=percent)
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = BatteryTalker()
    rclpy.spin(node)
