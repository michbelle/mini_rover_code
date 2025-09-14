#!/usr/bin/env python3

import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from math import pi
from nav2_common.launch import RewrittenYaml
# from launch_ros.parameter_descriptions import RewrittenYaml


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation/Gazebo clock')

    bringup_dir = get_package_share_directory('mini_launchpad')
    namespace = LaunchConfiguration('namespace')
    declare_namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='')

    # Start robot localization using an Extended Kalman filter
    # robot_localization_file_path = Path(bringup_dir, 'config','odom_filtered_localization','Rlocalization_ekf.yaml')

    params_file = LaunchConfiguration('params_file')
    declare_param_file = DeclareLaunchArgument(
            'params_file',
            default_value=Path(bringup_dir, 'config','odom_filtered_localization','localization_ekf.yaml'),
            description='Full path to the ROS2 parameters file to use'),
    
    # remappings = [('/tf', 'tf'),
    #               ('/tf_static', 'tf_static')]

    # Create our own temporary YAML files that include substitutions
    param_substitutions = {
        'use_sim_time': use_sim_time}

    configured_params = RewrittenYaml(
        source_file=params_file,
        root_key=namespace,
        param_rewrites=param_substitutions,
        convert_types=True)
    
    localization_node = Node(
    	package='robot_localization',
    	executable='ekf_node',
    	name='ekf_filter_node',
    	output='screen',
    	parameters=[configured_params]
    	)
    
    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_namespace)
    ld.add_action(declare_param_file)
    ld.add_action(localization_node)

    
    return ld

