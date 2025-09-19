
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
        get_package_share_directory('witmotion_ros'),
        'config',
        'wt31n.yml'
        )
    
    print(config)
        
    node=Node(
        package = 'witmotion_ros',
        executable = 'witmotion_ros_node',
        name = "witmotion_ros",
        # prefix=["sudo -E env \"PYTHONPATH=$PYTHONPATH\" \"LD_LIBRARY_PATH=$LD_LIBRARY_PATH\" \"PATH=$PATH\" \"USER=$USER\"  /bin/bash -c "],
        parameters = [config],
        # shell=True
    )

    ld.add_action(node)
    return ld