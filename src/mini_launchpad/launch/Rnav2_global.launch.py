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

    
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')

    # Include the gz sim launch file  
    launch_folder = get_package_share_directory("mini_launchpad")

    sensor_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "real", "0.1r_sensorLaunch.launch.py")),
        launch_arguments={
        }.items()
    )

    communication_mini_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "0.2r_mini.launch.py")),
        launch_arguments={
        }.items()
    )


    odometry_increase_precision = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "1r_robot_localizationEKF.launch.py")),
        launch_arguments={
            'use_sim_time' : use_sim_time
        }.items()
    )

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "2r_navigation_launch.py")),
        launch_arguments={
            'use_sim_time' : use_sim_time
        }.items()
    )

    localization_nav = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launch_folder, "launch", "sim", "3r_Lamcl.launch.py")),
        launch_arguments={
            'use_sim_time' : use_sim_time
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

    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)

    ld.add_action(sensor_launch)
    ld.add_action(communication_mini_launch)

    # Launch Gazebo
    ld.add_action(odometry_increase_precision)
    ld.add_action(nav_launch)
    ld.add_action(localization_nav)
    ld.add_action(rviz_node)


    return ld
