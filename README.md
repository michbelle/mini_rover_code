# Rover Mini instruction

**the robot is associated with**:
```
ROS_DOMAIN_ID=10
```
is written inside the `~/.bashrc` file 

## Zenoh
```bash
/home/mini/zenoh-bridge-ros2dds -c /home/mini/navros/src/myTesiCode/zenoh_1_1/zenoh_config_client/zenoh_config_mini_bridge.json5
```

## CAN Troubleshooting
```bash
sudo ip link set can0 type can bitrate 500000
sudo ip link set can0 up
```