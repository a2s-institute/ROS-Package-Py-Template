# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Introduction

This package is a ROS node.

### The available ROS topics
Please, follow this structure:

- `topic_1`
    - **Default:** `/{{ cookiecutter.project_slug }}/topic_1`
    - **Purpose:** the purpose.
    - **Use:**  Send an emply msg.

- `topic_2`
    - **Default:** `/{{ cookiecutter.project_slug }}/topic_2`
    - **Purpose:** the purpose.

### ROS parameters
Please, follow this structure:
- `{{ cookiecutter.project_slug }}_world_frame_name`
    - **Default:** `world`



## Installation

Follow these steps to build and run the package.

### Dependencies
Please, follow this structure:
1. first dependency: `sudo apt install first_dependency`
2. second dependency: `sudo apt install second_dependency`

### Build

```bash
cd ~/catkin_ws
catkin_make
```


## Quality
**requires**
```bash
pip install tox pytest black isort flake8
```
then run 
```bash
tox
```

### Formatting
```bash
tox -e format
tox -e lint
```

### Testing

```bash
tox -e test
```


## Run
```bash
source ~/catkin_ws/devel/setup.bash
roslaunch {{ cookiecutter.project_slug }} example.launch
```

## Update this repository as the template changes overtime
```bash
pip3 install cruft
cruft check
```

in case the template changed and you want to update your repo to the template

```bash
cruft update
```