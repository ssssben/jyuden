FROM ros:foxy-ros-base

RUN apt update && apt install -y \
    rsync \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/ros2_jyuuden_ws

ENV ROS_DOMAIN_ID=0

