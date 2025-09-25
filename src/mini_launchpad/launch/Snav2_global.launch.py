import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from launch.actions import SetEnvironmentVariable

import os
os.environ["ROS_DOMAIN_ID"] = "10"

def generate_launch_description():
    # Create the launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')

    info_domain_id=LogInfo(msg='launching simulation on ROS_DOMAIN_ID : 10'),

    
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    # Include the gz sim launch file  
    launch_folder = get_package_share_directory("mini_launchpad")

    odometry_increase_precision = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "1s_robot_localizationEKF.launch.py")),
        launch_arguments={
        }.items()
    )

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "2s_navigation.launch.py")),
        launch_arguments={
        }.items()
    )

    localization_nav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "3s_Lamcl.launch.py")),
        launch_arguments={
        }.items()
    )    

    rviz_config_dir = os.path.join(
            get_package_share_directory("mini_launchpad"),
            "rviz",
            "mini_nav.rviz")
    
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2_mini_nav",
        arguments=["-d", rviz_config_dir],
        output="screen")

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(info_domain_id)
    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)

    # Launch Gazebo
    ld.add_action(odometry_increase_precision)
    ld.add_action(nav_launch)
    ld.add_action(localization_nav)
    ld.add_action(rviz_node)
    

    return ld
