import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import psutil

class BatteryTalker(Node):
    def __init__(self):
        super().__init__('batterytalker')
        self.pub = self.create_publisher(Int16, 'battery_status', 10)
        self.create_timer(1.0, self.cb)
        self.count = 0

    def cb(self):
        battery = psutil.sensors_battery()
        percent = int(battery.percent) if battery else 0
        self.count += 1
        self.get_logger().info(f"Battery level: {percent}% - Count: {self.count}")
        msg = Int16(data=percent)
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = BatteryTalker()
    try
    rclpy.spin(node)
    except Exception as e:
        node.get_logger().error(f"An error occurred: {str(e)}")
        node.get_logger().info("Shutting down...")
        rclpy.shutdown()
        raise
