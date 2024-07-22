import rospy
from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import MyClass

class MyClassROS:
    """
    ROS interface for MyClass.

    This class provides the ROS-specific interface for the MyClass class, including
    initialization and update methods that are called in a ROS node.
    """

    def __init__(self):
        """
        Initialize the MyClassROS instance.

        This constructor initializes an instance of the MyClass class.
        """
        self.my_class = MyClass()

    def initialize(self):
        """
        Initialize the MyClass instance.

        This method initializes the underlying MyClass instance.
        """
        self.my_class.initialize()

    def update(self):
        """
        Update the MyClass instance.

        This method updates the underlying MyClass instance.
        """
        self.my_class.update()
