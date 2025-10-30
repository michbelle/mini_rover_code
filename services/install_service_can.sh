cat << EOF4 | sudo tee /usr/sbin/enablecan
#!/bin/bash
# sudo ip link set can0 type can bitrate 500000 sjw 2 dbitrate 2000000 dsjw 15 berr-reporting on fd on
sudo ip link set can0 type can bitrate 500000
sudo ip link set up can0
EOF4

sudo chmod +x /usr/sbin/enablecan

cat << EOF5 | sudo tee /etc/systemd/system/can.service
[Service]
Type=simple
User=root
ExecStart=/usr/sbin/enablecan
[Install]
WantedBy=multi-user.target
EOF5

sudo systemctl enable can.service

# sudo ip link set can0 type can bitrate 500000 sjw 2 dbitrate 2000000 dsjw 15 berr-reporting on fd on
sudo ip link set can0 type can bitrate 500000
sudo ip link set up can0