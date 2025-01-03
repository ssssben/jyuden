import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import psutil

class BatteryTalker(Node):
    def __init__(self):
        super().__init__('batterytalker')
        self.pub = self.create_publisher(Int32, 'battery_status', 10)
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            self.get_logger().info(f"Battery level: {percent}%")
            msg = Int32()
            msg.data = int(percent)
            self.pub.publish(msg)
        else:
            self.get_logger().warn("Battery information not available.")

def main():
    rclpy.init()
    node = BatteryTalker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}")
