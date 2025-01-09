# SPDX-FileCopyrightText: 2025 ben fang
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class BatteryListener(Node):
    def __init__(self):
        super().__init__('batterylistener')
        self.sub = self.create_subscription(Int16, 'battery_status', self.cb, 10)
        self.count = 0

    def cb(self, msg):
        battery_level = msg.data
        self.count += 1
        self.get_logger().info(f"Received battery level: {battery_level}% -- Count: {self.count}")

def main():
    rclpy.init()
    node = BatteryListener()
    rclpy.spin(node)
