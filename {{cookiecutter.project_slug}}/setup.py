from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    license="{{ cookiecutter.license }}",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "rospy",
        "std_msgs",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "isort",
            "flake8",
        ],
    },
)
