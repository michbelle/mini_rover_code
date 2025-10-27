cat << EOF2 | sudo tee /usr/sbin/roverrobotics
#!/bin/bash

ros2 launch mini_launchpad Rnav2_global.launch.py
PID=\$!
wait "\$PID"
EOF2

sudo chmod +x /usr/sbin/roverrobotics


cat << EOF3 | sudo tee /etc/systemd/system/roverrobotics.service
[Service]
Type=simple
User=$USER
ExecStart=/bin/bash /usr/sbin/roverrobotics
[Install]
WantedBy=multi-user.target
EOF3

sudo systemctl enable roverrobotics.service