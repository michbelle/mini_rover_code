import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Create the launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time')

    
    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')
        
    launchpad_folder = get_package_share_directory("mini_launchpad")

    ##sensor launch
    #imu and laser scan
    imu_laser_sensor = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launchpad_folder, "launch", "0.1r_sensorLaunch.launch.py")),
        launch_arguments={
        }.items()
    )

    #can communication
    mini_can = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launchpad_folder, "launch", "0.2r_mini.launch.py")),
        launch_arguments={
        }.items()
    )

    ##locEKF
    locEKF = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launchpad_folder, "launch", "real", "1r_robot_localizationEKF.launch.py")),
        launch_arguments={
        }.items()
    )

    ##locAMCL
    locAMCL = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launchpad_folder, "launch", "real", "3r_Lamcl.launch.py")),
        launch_arguments={
        }.items()
    )

    #nav2
    call_nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(launchpad_folder, "launch", "real", "2r_navigation_launch.py")),
        launch_arguments={
        }.items()
    )



    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_use_sim_time_cmd)

    # Launch real control
    ld.add_action(imu_laser_sensor)
    ld.add_action(mini_can)
    ld.add_action(locEKF)
    ld.add_action(locAMCL)
    ld.add_action(call_nav2)

    return ld