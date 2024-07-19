cmake_minimum_required(VERSION 3.0.2)
project({{ cookiecutter.project_slug }})

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  src/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}_ros_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
