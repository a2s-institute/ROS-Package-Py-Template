cmake_minimum_required(VERSION 3.0.2)
project({{ cookiecutter.project_slug }})

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)
catkin_python_setup()


catkin_package()
include_directories(
  ${catkin_INCLUDE_DIRS}
)