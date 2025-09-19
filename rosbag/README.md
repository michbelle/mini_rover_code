save topic to simulate beahaviours


avaible topics
```bash
/amcl_pose
/arduino/imu_data_raw
/battery
/battery_capacity
/bond
/cmd_vel
/covariance
/current
/diagnostics
/hardware_status
/jobot_driver_ros2/transition_event
/joint_states
/joy
/joy/set_feedback
/odom
/parameter_events
/robot_description
/rosout
/scan
/serial_status
/set_leds
/special
/status_recharge
/temperature
/tf
/tf_static
/uls
/uls_debug
```


record
```bash
ros2 bag record \
    -o jobot_record_003 \
    /amcl_pose \
    /arduino/imu_data_raw \
    /battery \
    /battery_capacity \
    /bond \
    /cmd_vel \
    /covariance \
    /current \
    /diagnostics \
    /hardware_status \
    /jobot_driver_ros2/transition_event \
    /joint_states \
    /odom \
    /parameter_events \
    /robot_description \
    /scan \
    /serial_status \
    /set_leds \
    /special \
    /status_recharge \
    /temperature \
    /tf \
    /tf_static \
    /uls \
    /uls_debug

```


play
```bash
ros2 bag play \
    record_001 \
    --topics \
    <topic 1> \ ...
    --clock
    -r 1
```

playing with simulation time
```
ros2 bag play record_001 --clock -r 5
```

## dowload bag file from:

https://drive.elettra.eu/d/1a9e39e6003d4f65b171/
