#! {{ cookiecutter.python_interpreter_location}}
import rospy
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}_ros import MyClassROS

def main():
    """
    Main function to initialize and run the ROS node.

    This function initializes the ROS node, creates an instance of MyClassROS,
    and enters a loop that updates the instance at a specified rate.
    """
    rospy.init_node('{{ cookiecutter.project_slug }}')
    my_class_ros = MyClassROS()
    my_class_ros.initialize()

    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        my_class_ros.update()
        rate.sleep()

if __name__ == '__main__':
    main()