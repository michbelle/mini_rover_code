cat << EOF2 | sudo tee /usr/sbin/nav2_process
#!/bin/bash

ros2 launch mini_launchpad Rnav2_global.launch.py
PID=\$!
wait "\$PID"
EOF2

sudo chmod +x /usr/sbin/nav2_process


cat << EOF3 | sudo tee /etc/systemd/system/nav2_process.service
[Unit]
Description=navigation pkg
After=can.service
[Service]
Type=simple
Environment=RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
Environment=ROS_DOMAIN_ID=10
User=mini
ExecStart=/bin/bash /usr/sbin/nav2_process
[Install]
WantedBy=multi-user.target
EOF3

sudo systemctl enable nav2_process.service