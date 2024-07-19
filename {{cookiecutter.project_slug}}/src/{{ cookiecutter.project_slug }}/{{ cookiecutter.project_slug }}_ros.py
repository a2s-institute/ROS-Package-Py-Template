import rospy
from {{ cookiecutter.project_slug }} import MyClass

class MyClassROS:
    def __init__(self):
        self.my_class = MyClass()

    def initialize(self):
        self.my_class.initialize()

    def update(self):
        self.my_class.update()
