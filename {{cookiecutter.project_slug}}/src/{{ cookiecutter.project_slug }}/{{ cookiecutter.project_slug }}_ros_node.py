import rospy
from {{ cookiecutter.project_slug }}_ros import MyClassROS

def main():
    rospy.init_node('{{ cookiecutter.project_slug }}')
    my_class_ros = MyClassROS()
    my_class_ros.initialize()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        my_class_ros.update()
        rate.sleep()

if __name__ == '__main__':
    main()